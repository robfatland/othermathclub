# sphinx 42


This is a riddle game that emphasizes...


- basic input of strings
- formatting a web request (http POST)
- an infinite loop with an escape clause (conditional logic)
- using the `requests` library


## step 1: Create an Azure Function App


- This is done in the Azure console. One could also use the CLI; or possibly ARM/bicep
- I chose region 'US WEST 2': Washington state
- Sphinx refers to riddles and 42 refers to the ultimate answer to Life, the Universe and Everything


We begin by planning for 2 routes: `test` and `sphinx42`


- `test` returns a pointer to sphinx42
- `sphinx42` evaluates two arguments: `riddle` and `guess`


Here are a couple notes on setting up the Function App.


- You set up a dummy Function App that allows you to verify it is running by pasting the URL
- You go to VS Code to build a Function App in a folder
- You test that by installing Azure Function Core Tools. This gives us the command `func`.
    - It may be necessary to stop and re-start VS Code after the install.
- Running `func` allows us to debug on localhost. This uses port 7071.


```
http://localhost:7071/api/test
http://localhost:7071/api/sphinx42?riddle=1&guess=Wednesday
```

- To publish to Azure first (in VS Code) do File > Open Folder > sphinx42 to include it in the Workspace
- Once it publishes on Azure it takes a couple of minutes to actually work


- `https://sphinx42-<longhexstring>.westus2-01.azurewebsites.net/api/test` und so weiter

 
