import requests
from payload_login_pass import payload

URL = 'https://thinking-tester-contact-list.herokuapp.com'
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", f"{URL}/users/login", headers=headers, json=payload)
response_json = response.json()
TOKEN = response_json.get('token')
HEADERS = headers
AUTH = {
  'Authorization': f'Bearer {TOKEN}'
}
