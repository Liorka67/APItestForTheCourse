import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

def test001_post():
    #for the json file
    file = open("C:\\Users\\liorkat\\Documents\\LiorComp\\python\\data\\createUser.json","r")
    json_input = file.read()
    response_json = json.loads(json_input)
    print(response_json)

    #make post request with json input body
    response = requests.post(url,response_json)
    print(response.content)

    #validating response code
    assert response.status_code == 201
    #fetch header from response
    print(response.headers.get('Connection'))

    #parse response to json format
    response_json = json.loads(response.text)

    #pick id using json path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])