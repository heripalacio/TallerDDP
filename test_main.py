import requests

def test_hello():
    response = requests.get("http://localhost:8000/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI"}

def test_is_prime():
    response = requests.get("http://localhost:8000/IsPrime/7")
    assert response.status_code == 200
    assert response.json() == {"IsPrime": True}

    response = requests.get("http://localhost:8000/IsPrime/10")
    assert response.status_code == 200
    assert response.json() == {"IsPrime": False}

def test_fibonacci():
    response = requests.get("http://localhost:8000/fibonacci/5")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 5}

    response = requests.get("http://localhost:8000/fibonacci/10")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 55}
