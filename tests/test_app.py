from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Project Alpha' in response.data


def test_item_details_success():
    client = app.test_client()
    response = client.get('/item/1')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['id'] == 1
    assert payload['title'] == 'Project Alpha'


def test_item_details_not_found():
    client = app.test_client()
    response = client.get('/item/999')
    assert response.status_code == 404
    payload = response.get_json()
    assert payload['error'] == 'Item not found'


def test_contact_validation_errors():
    client = app.test_client()
    response = client.post(
        '/contact',
        data={'name': 'A', 'email': 'bad-email', 'message': 'short'},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b'Please enter a valid email address.' in response.data


def test_toggle_theme_validation_and_success():
    client = app.test_client()

    invalid_response = client.post('/toggle-theme', json={'theme': 'blue'})
    assert invalid_response.status_code == 400

    valid_response = client.post('/toggle-theme', json={'theme': 'dark'})
    assert valid_response.status_code == 200
    payload = valid_response.get_json()
    assert payload['status'] == 'success'
    assert payload['theme'] == 'dark'
