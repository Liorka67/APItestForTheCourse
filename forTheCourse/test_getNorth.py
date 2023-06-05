import json
import jsonpath
import requests

url = "https://northwind.netcore.io/customers.json"
def test_001():
    response = requests.get(url)
    json_response = json.loads(response.text)
    companyName = jsonpath.jsonpath(json_response,'results[1].companyName')

    print(companyName)
    assert companyName == ['Ana Trujillo Emparedados y helados']
