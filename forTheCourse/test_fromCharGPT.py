import json
import requests

# API endpoint URL
base_url = "https://simple-books-api.glitch.me"
headers = {}


def test_status():
    response = requests.get(f'{base_url}/status')
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_list_books():
    response = requests.get(f'{base_url}/books', params={"type": "fiction", "limit": 10})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 10


def test_get_book():
    response = requests.get(f'{base_url}/books/1')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_submit_order():
    client_data = {
        "clientName": "My API Client",
        "clientEmail": "myemail@example.com"
    }
    response = requests.post(f'{base_url}/api-clients', json=client_data)
    access_token = response.json()["access_token"]
    headers["Authorization"] = f"Bearer {access_token}"

    order_data = {
        "bookId": 1,
        "customerName": "John"
    }
    response = requests.post(f'{base_url}/orders', json=order_data, headers=headers)
    assert response.status_code == 201
    assert "orderId" in response.json()


def test_get_orders():
    response = requests.get(f'{base_url}/orders', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_order():
    response = requests.get(f'{base_url}/orders/1', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_update_order():
    update_data = {"customerName": "Jane"}
    response = requests.patch(f'{base_url}/orders/1', json=update_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["customerName"] == "Jane"


def test_delete_order():
    response = requests.delete(f'{base_url}/orders/1', headers=headers)
    assert response.status_code == 200
