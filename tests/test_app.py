import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_get_tasks(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = response.get_json()
    # Fixed: Check if 'data' key contains the list
    assert isinstance(data['data'], list)
    assert data['success'] is True

def test_add_task(client):
    response = client.post('/api/tasks', 
                          json={'title': 'Test Task'})
    assert response.status_code == 201
    data = response.get_json()
    # Fixed: Access the 'data' wrapper first
    assert data['success'] is True
    assert data['data']['title'] == 'Test Task'