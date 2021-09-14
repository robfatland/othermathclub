
# debug: include 'print(d)' and use the Monitoring tab to find/read the log
import json

def lambda_handler(event, context):
    print('a')
    if event.get('queryStringParameters') == None:
        return { "statusCode": 200, "body": 'add ?x=4.&y=3.&z=1 to request (any x/y/z coordinates are fine)'}
    print('b')
    rs = ''
    print('c')
    d = event['queryStringParameters']
    print('d')   
    # determine if this is a request for 'hard' mode (narrower spikes)
    verbose = False
    if d.get('verbose') != None:
        if d['verbose'].lower() == 'true': verbose = True
        
    # determine if this is a request for 'hard' mode (narrower spikes)
    hardMode = False
    if d.get('setting') != None:
        if d['setting'] == 'hard': hardMode = True

    # check to see if the coordinates have at least been mentioned
    if d.get('x') == None: rs += 'your request is missing the x coordinate: for example x=4.\n'
    if d.get('y') == None: rs += 'your request is missing the y coordinate: for example y=3.\n'
    if d.get('z') == None: rs += 'your request is missing the z coordinate: for example z=1.\n'
    
    if len(rs) > 0: return { "statusCode": 200, "body": rs }

    if not d['x']: rs += 'request mentions x but please set it to something, for example x=4.\n'       
    if not d['y']: rs += 'request mentions y but please set it to something, for example y=3.\n'       
    if not d['z']: rs += 'request mentions z but please set it to something, for example z=1.\n'       
        
    
    if len(rs) > 0: return { "statusCode": 200, "body": rs }
        
    x = float(d['x'])
    y = float(d['y'])
    z = float(d['z'])
    
    rs += str(x + y + z)
    
    if hardMode: rs += ' (hard)'
    if verbose: rs += ' ({}, {}, {})'.format(str(x), str(y), str(z))
    return { "statusCode": 200, "body": rs }

