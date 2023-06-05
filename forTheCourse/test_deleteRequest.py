import requests

url = "https://reqres.in/api/users/2"

def test001_delete():
    #Define the request
    response = requests.delete(url)

    print(response.status_code)
    #Test response code
    assert response.status_code == 20