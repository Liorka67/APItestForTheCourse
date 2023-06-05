import json
import jsonpath
import requests

url = "https://reqres.in/api/users/2"

def test001_delete():
    #for the json file
    file = open("C:\\Users\\liorkat\\Documents\\LiorComp\\python\\data\\createUserUpdate.json","r")

    json_input = file.read()

    response_json = json.loads(json_input)
    print('this is the response_json')
    print(response_json)

    #make PUT request with json input body
    response = requests.put(url,response_json)
    print('this is the response_content')
    print(response.content)

    #validating response code different response code
    assert response.status_code == 200

    #parse response content
    response_json = json.loads(response.text)
    print(response_json)
    update_li = jsonpath.jsonpath(response_json,'updatedAt')
    print('this is the update_li message')
    print(update_li)
