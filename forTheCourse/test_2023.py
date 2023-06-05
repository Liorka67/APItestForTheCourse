import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

def test_getRequests():
    responseGetRequest = requests.get(url)
    print(responseGetRequest.text)
    responseJson = json.loads(responseGetRequest.text)
    first_name = jsonpath.jsonpath(responseJson,'data[1].first_name')
    print(first_name)
