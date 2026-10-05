# sphinx 42


This is a riddle game that emphasizes...


- input from the User (strings)
- formatting a web request = a base address + some details
- an infinite loop with an escape clause (conditional logic)
- using a library to do something interesting. (The library is called `requests`.)


## step 1: Create an Azure Function App


An Azure Function App is some Python code that runs somewhere on the internet. We do not
worry about where it lives; and building it is a coach activity (not a student activity).
Once this is done we can go to step 2, a student activity, which is writing more Python 
code to talk to this Function App.


### Some notes for coach-builders


- The Function App is built in the Azure console. Although one could also use the CLI; and possibly ARM/bicep
- Chose a nearby region e.g. 'US WEST 2' for Washington state
- The name 'Sphinx42' invokes riddles and the ultimate answer to Life, the Universe and Everything


The code will define 2 routes: `test` and `sphinx42`. The latter is the actual puzzle game.


- `test` returns a mention of sphinx42
- `sphinx42` evaluates two arguments: `riddle` and `guess`
    - `riddle` is a label for a particular puzzle. The first one is `1` but they are not all numbers.
    - `guess` is a guess at a solution
        - To start with these are one-word or one-number answers so no issue with spaces for the Client
        - URLs are finicky in how they deal with spaces and plus signs 


Notes on setting up the Function App.


- On the console: Create a dummy Function App that allows you to verify it runs by pasting the URL
- You go to your laptop and use VS Code to build a Function App within a dedicated folder
    - You will need the Azure extensions installed in VS Code
    - At some point it will have you authenticate a login to Azure
- You write and then test the Function App on localhost...
    - you will need to install Azure Function Core Tools to get the command `func`. (This runs in powershell.)
        - It may be necessary to stop and re-start VS Code after this install
    - you use `func start` from the Function App folder to get the server running
    - this uses port 7071 by default
    - You place the following URLs in a browser address bar to test


```
http://localhost:7071/api/test
http://localhost:7071/api/sphinx42?riddle=1&guess=Wednesday
```

- Once this is working: Deploy the Function App to the Azure dummy Function App created above
    - In VS Code: `File > Open Folder > foldername` to include the Function App folder in the Workspace
    - Chose the Azure icon on the Activity Bar (left side)
    - Navigate to the Function App folder > right click > Deploy Function App > confirm
    - Takes a coupld minutes
- Use the browser with now the full IP address to test the deployed Function App
    - `https://sphinx42-<idstring>.westus2-01.azurewebsites.net/api/sphinx42?riddle=1&guess=Wednesday`


## step 2: Create a Python client


This code will not work until the idstring (below: `ffff...ff`) is corrected to the actual value. We don't put that
here because this text will be openly visible on the web. Get the correct value from a coach.


This 11-line program is enough to get a guess from the User, send it to the riddle game, and print the response.


```
import requests

base_url = "https://sphinx42-d8cfhfg8fhe6bxd0.westus2-01.azurewebsites.net/api/sphinx42?"

while True:
    riddle_name = input("\nRiddle name (or 'quit' to exit): ")
    if riddle_name.lower() == 'quit': break 
    my_guess = input("\nEnter guess: ")
    message_to_the_internet = base_url + "riddle=" + riddle_name + "&guess=" + my_guess
    print("\nHere is what is sent:\n\n" + message_to_the_internet)
    internet_reply          = requests.get(message_to_the_internet)
    text_reply              = internet_reply.text
    print("\nHere is what came back:\n\n" + text_reply)
```


Here is what this program is doing: 


- `import requests` opens up the `requests` library that we use to talk to the internet
- `base_url` is an address on the internet where the puzzle game lives
- `while True:` will run a loop that never stops. All the remaining code is indented: We say it is *inside* this loop.
- `riddle_game = input(...)` gets User input, the *name* or *label* of a riddle. There are several in the game.
- `if riddle...:` checks to see if the User wants to quit. This is **Conditional Logic**
- `    break` is what happens when the User wants to quit: It means `fall out of this loop instantly`
    - Notice that this `break` overcomes the infinite loop we saw above: `while True:`. So `break` is stronger.
- `my_guess = input(...)` gets a guess for this riddle.
    - Now we have all the information we need to send a message on the internet to the puzzle game
- `message_to_the_internet = ...` glues together all the pieces that make up the message
- `internet_reply = requests.get(message_to_the_internet)` uses the `requests` library to send the message and store the answer back as `internet_reply`.
- `text_reply` gets just the text part of the response. There is other information in the response that we are going to ignore for now.
- `print(text_reply)` lets the User see what that response was
    - This is the end of the `while True:` loop so now it will begin all over again
 

## appendix: Function App code


Here is the main program `function_app.py`. There is a small finesse of dealing with "+" characters
which are converted to space characters " " in the return message; so the code compensates for this
but not in the most elegant manner possible.


```
import azure.functions as func
import logging
from riddles import riddles

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="test")
def test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('test request received')
    return func.HttpResponse("The test route worked; now try route = 'sphinx42'", status_code=400)

@app.route(route="sphinx42")
def sphinx42(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('sphinx42 request received')
    available_riddles = ", ".join(riddles.keys())
    
    riddle_id = req.params.get('riddle')
    guess = req.params.get('guess')
    
    if not riddle_id:
        return func.HttpResponse("Choose the first riddle by adding '?riddle=1'", status_code=400)
    
    if riddle_id not in riddles:
        return func.HttpResponse(f"There is no riddle called {riddle_id}.", status_code=404)
        
    prompt, solution, success_message = riddles[riddle_id]

    replymsg = prompt + '\n\n'
    
    if not guess:
        replymsg +="To guess an answer add '&guess=youranswer'\n\n" 
        return func.HttpResponse(replymsg, status_code=400)

    print(guess)
    print(solution)

    # Handle URL decoding of + characters
    if guess == solution or guess.replace(' ', '+') == solution:
        return func.HttpResponse(success_message)
    else:
        return func.HttpResponse(f"Nope, try again!\n\nRiddle {riddle_id}: {prompt}")
```


The other code file is `riddles.py` containing of course the information for the riddles. 
I have given the code below in redacted form. The idea is to set up a dictionary `riddles` where the 
key is the riddle ID and the value is a tuple: 


- A prompt (stating the riddle)
- The correct solution
- A correct-guess response message


The response message passes the User along to the next riddle.


```
riddles = {
    "1": ("I would like ...text...", 
          "answer", 
          "Right on! You have passed on to try riddle 101."),
    "101": ("What is the ...text...?", 
            "answer", 
            "Excellent! Now you can try riddle 'halfway'"),
    "halfway": ("Where does ...text...?", 
                  "answer", 
                  "We text. You can now attempt the riddle called 'chaos'."),
    "chaos": ("In the chaos game what is ...text...?",
              "answer",
              "Very nice! Now finally try riddle 42."),
    "42": ("What is ...text...?", 
           "answer", 
           "congratulations, you have completed the sphinx42 game.")
}
```
 
