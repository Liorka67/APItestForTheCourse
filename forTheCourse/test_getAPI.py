import json
import jsonpath
import requests

url = 'https://reqres.in/api/users?page=2'

def test_tc004():
    resposeAPI = requests.get(url)
    print(resposeAPI.text)
    responseJson = json.loads(resposeAPI.text)
    email = jsonpath.jsonpath(responseJson,'data[3].email')
    print(email)
    assert email == ['byron.fields@reqres.in']



