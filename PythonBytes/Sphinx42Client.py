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
