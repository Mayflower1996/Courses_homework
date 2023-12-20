import requests
from homework28.Data.url_token_headers_auth import UrlHeaders as uh


def test_get_contact_card(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.get(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH)
    assert response.status_code == 200


def test_unauthorized_get_contact_card(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.get(f'{uh.URL}/contacts/{ID}', headers=uh.HEADERS)
    assert response.status_code == 401
