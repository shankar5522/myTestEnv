from collections.abc import MutableMapping
import requests
import json


username = 'shankar5522'
token = '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'
# login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))


# Create an API request
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code: ", response.status_code)
# In a variable, save the API response.
response_dict = response.json()
# Evaluate the results.
print(response_dict.keys())

# # Create an API request
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# response = requests.get(url)
# print("Status code: ", response.status_code)
# # In a variable, save the API response.
# response_dict = response.json()
# # Evaluate the results.
# print(response_dict.keys())



# repo = 'some_repo'
# description = 'Created with api'
#
# payload = {'name': repo, 'description': description, 'auto_init': 'true'}
#
# login = requests.post('https://api.github.com/' + 'user/repos', auth=(username,token), data=json.dumps(payload))
