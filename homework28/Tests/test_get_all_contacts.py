import requests
from homework28.Data.url_token_headers_auth import UrlHeaders as uh


def test_get_page():
    response = requests.get(f'{uh.URL}/contacts', headers=uh.AUTH)
    assert response.status_code == 200


def test_unauthorized_get_page():
    response = requests.get(f'{uh.URL}/contacts', headers=uh.HEADERS)
    assert response.status_code == 401
    assert response.text == '{"error":"Please authenticate."}'
