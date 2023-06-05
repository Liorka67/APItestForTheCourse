import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

def test_001():
    resRequest = requests.get(url)
    print(resRequest.text)

    resJason = json.loads(resRequest.text)
    first_name = jsonpath.jsonpath(resJason,'data[1].first_name')
    print(first_name)
    assert first_name == ['Michael']



