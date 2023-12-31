import requests
from homework28.Data.url_token_headers_auth import UrlHeaders as uh


def test_delete_existing_contact(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.delete(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH)
    assert response.status_code == 200
    assert 'deleted' in response.text


def test_delete_without_authentication(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.delete(f'{uh.URL}/contacts/{ID}', headers=uh.HEADERS)
    assert response.status_code == 401
    assert response.text == '{"error":"Please authenticate."}'


def test_delete_non_existing_contact(create_contact_and_get_id):
    ID = create_contact_and_get_id
    response = requests.delete(f'{uh.URL}/contacts/{ID}', headers=uh.AUTH)
    assert response.status_code == 404
