###############
#
# Python to query the periodic table API
#   Uses the requests HTTP library to get information about a single element
#   Uses the json library to help parse the return value
#
###############

import requests, json

url_base = 'https://naomila-atomic-test.azurewebsites.net/api/http_trigger'
element = 'Gold'
url = url_base + '?element=' + element

print()
print('using url', url)
print()

r = requests.put(url)       # .get() also works
                            # no user/pass authentication necessary

'''
print(type(r)) yields requests.models.Response

print(dir(r)) yields

'apparent_encoding', 'close', 'connection', 'content', 'cookies',
'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect',
'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next',
'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code',
'text', 'url']

print(r.headers) yields dictionary-like metadata
print(r.headers['content-type']) yields 'application/json'

r.text is a json-format string, the "return value" of the put()

'''

element_info = json.loads(r.text)[0] # .loads() produces a list with 1 element
                                     #   this (element [0]) is a dictionary with information
                                     #   about the requested element 'Gold'

print()
print('return information:\n')
print(element_info)
print()
print('Variable `element_info` is of type', type(element_info), 'and it has',
      len(element_info), 'entries')
print()

if element_info['Radioactive'] == 'true': print(element, 'is radioactive')
else: print(element, 'is NOT radioactive')
print()

element_keys = list(element_info.keys())
print('we have the keys of this dictionary as type', type(element_keys))
print()
print('dictionary key 1 is', element_keys[1])
print('the corresponding value is', element_info[element_keys[1]])
print()
print('dictionary key 3 is', element_keys[3])
print('the corresponding value is', element_info[element_keys[3]], 'Da')
print()
