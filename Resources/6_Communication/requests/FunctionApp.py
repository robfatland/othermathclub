#
# This is Azure Function App (Python) code for a serverless cloud function.
# For more detail and a link to the "how to build" lessons see the nexus
# site page: https://github.com/robfatland/nexus/blob/gh-pages/data/api.md
# 
# This code supports a small collection of routes intended for student use:
#   bumpkin: simple test
#   lookup: data from the Periodic Table of Elements
#   gargutron: a simple guessing game
#   kirstetrommeron: another game; under construction
#
# The underlying purpose of the nexus website is to provide construction 
# details and context for learning how to serve data on the cloud. This
# copy of the Function App code is really just a safe backup; it has no
# direct use.
#


import azure.functions as func
import datetime, json, logging, os
import azure.cosmos.cosmos_client as cosmos_client
import random

# Load database keys from the working environment
try:
  HOST = os.environ['ACCOUNT_HOST']
  MASTER_KEY = os.environ['ACCOUNT_KEY']
except KeyError:
  logging.error("Get your database's account URL and key and set them in the ACCOUNT_HOST / ACCOUNT_KEY environment variables")

# Identify the database and container we want to read from
DATABASE_ID = "periodic-db"
CONTAINER_ID = "elements"

app = func.FunctionApp()

@app.route(route="bumpkin", auth_level=func.AuthLevel.ANONYMOUS)
def bumpkin(req: func.HttpRequest) -> func.HttpResponse:
    """Test route"""
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Gargutron here, saying it is time for you to take a break.",
        status_code=200
    )

def stripPrivateKeys(structure):
    """
    NoSQL database entry: remove internal data with names that begin with underscore.
    This function searches through nested dictionaries and lists. It modifies the
    'structure' input in-place. For us this means the copy of the data in Python world 
    gets changed (and the copy in the database stays the same).
    """
    if hasattr(structure, "keys"):
        for key in list(structure.keys()):
            if hasattr(key, "startswith") and key.startswith("_"):
                del structure[key]
            else:
                stripPrivateKeys(structure[key])
    elif hasattr(structure, "__iter__") and not isinstance(structure, str):
        for elem in structure:
            stripPrivateKeys(elem)

# API route "lookup" pulls an element's information by its name
@app.route(route="lookup", auth_level=func.AuthLevel.ANONYMOUS)
def lookup(req: func.HttpRequest) -> func.HttpResponse:
    # Get the "name" input from the URL (or request body, if it's not in the url):
    element = req.params.get('name')
    if not element:
        try:               req_body = req.get_json()
        except ValueError: pass
        else:              element = req_body.get('name')
            
    if element:
        client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})
        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)
        
        # Data structure is a list of dictionaries, one per element.
        # In practice most likely only one element dictionary is returned.
        items = list(container.query_items(query="SELECT * FROM r WHERE r.id=@id",
            parameters=[{"name": "@id", "value": element}],
            enable_cross_partition_query=True))

        # Strip out internal database keys unrelated to chemical data
        stripPrivateKeys(items)

        # Turn the element data into a json string; and return this
        items_json = json.dumps(items)
        return func.HttpResponse(
            items_json,
            mimetype="application/json",
            status_code=200
        )
    else: return func.HttpResponse("Provide an element, honey..", status_code=404)



def is_prime(n):
    # n is presumed of type int: Evaluates prime(n) for Gargutron
    from math import sqrt
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True


def is_integer(string):
  try:
    int(string)
    return True
  except ValueError:
    return False


def is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False



# "Gargutron" is a route for an easy interactive puzzle. The player is attempting to feed
#    Gargutron some food. The key 'food' has a value that should be interpretable as a
#    number.
@app.route(route="Gargutron", auth_level=func.AuthLevel.ANONYMOUS)
def Gargutron(req: func.HttpRequest) -> func.HttpResponse:
    # Get the "food" value from the URL or request body
    Gargfood = req.params.get('food')
    if not Gargfood:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            Gargfood = req_body.get('food')
            
    if Gargfood:
        # msg = 'feed Gargutron; payload = ' + Gargfood
        if is_float(Gargfood):
            if is_integer(Gargfood):
                f = int(Gargfood)
                if f < 1:
                    msg = 'Good number... but Gargutron eats only positive integers'
                elif f == 1:
                    msg = 'Good number... but too small for hungry Gargutron'
                else:
                    if is_prime(f):
                        if f < 30:
                            msg = 'Yummy Gargutron food but... too small... need bigger'
                        elif f < 101:
                            msg = 'Mmmm EXCELLENT Gargutron food but just a bit larger'
                        elif f > 200:
                            msg = 'Super Gargutron food but way too much of it'
                        elif f > 101:
                            msg = 'Fantastic Gargutron food but a bit too much... smaller?'
                        else: 
                            msg = 'Gargutron enjoy perfect-size meal (101), thank you!!'
                            msg += ' ...now maybe go talk to Gargutron sister Kirstetrommeron'
                    else:
                        msg = 'Gargutron unable to eat this... not good type of number'
            else: msg = 'Numbers are yummy! Gargutron can eat only integers though...'
        else:
            msg = 'No, sorry, Gargutron unable to eat ' + Gargfood + '\n'
            r = random.randint(0,2)
            if r == 0:   msg += 'Hint for you: Gargutron unable to eat words.'
            elif r == 1: msg += 'Hint for you: Gargutron fond of calculators.'
            else:        msg += 'Hint for you: Gargutron can not count on things like ' + Gargfood
        return func.HttpResponse(msg, status_code=200)
    else:
        return func.HttpResponse(
             "Gargutron want food!!! (try adding ?food=somefoodyoulike)",
             status_code=404
        )


# Kirstetrommeron is a next game; not built yet
@app.route(route="Kirstetrommeron", auth_level=func.AuthLevel.ANONYMOUS)
def Kirstetrommeron(req: func.HttpRequest) -> func.HttpResponse:
    shot = req.params.get('shot')
    food = req.params.get('food')
    if food: 
        msg = 'Kirstetrommeron is not hungry, just had lunch. Time for pickleball!'
        return func.HttpResponse(msg, status_code=200)
    if not shot:
        try:               req_body = req.get_json()
        except ValueError: pass
        else:              shot = req_body.get('shot')   
    if shot:
        msg = 'Kirstetrommeron returns the pickle ball back across the net...'
        return func.HttpResponse(msg, status_code=200)
    else:
        msg = 'Kirstetrommeron wants to play pickleball!\n'
        msg += '...but this game is not finished yet...\n'
        msg += '      Thanks for checking!'
        return func.HttpResponse(msg, status_code=404)