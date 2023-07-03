# Path: test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

# Path: test_main.py
def test_read_dataset():
    response = client.get("/dataset")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Dataset!"}

# Path: test_main.py
def test_get_dataset():
    response = client.get("/dataset/1")
    assert response.status_code == 200
    assert response.json() == {
        "@context": "https://schema.org/",
        "@type": "Dataset",
        "name": "Test Dataset",
        "description": "This is a test dataset",
        "url": "http://example.com/datasets/1",
        "sameAs": "http://example.com/datasets/1",
        "version": "1.0",
        "isAccessibleForFree": True,
        "keywords": ["test", "dataset"],
        "identifier": {"identifier": "doi:10.1000/test"},
        "variableMeasured": "Test variable"
    }
