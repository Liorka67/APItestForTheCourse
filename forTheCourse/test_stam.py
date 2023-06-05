import json
import jsonpath
import requests

url = 'https://reqres.in/api/users?page=2'

def test_stam():
    getResponse = requests.get(url)
    print(getResponse.text)
    jsonResponse = json.loads(getResponse.text)

    email = jsonpath.jsonpath(jsonResponse,'data[0].email')

    print(email)