from server import app_server
import pytest
import threading
import requests


@pytest.fixture(autouse=True, scope="session")
def start_server():
    t = threading.Thread(target=app_server.app.run)
    t.start()
    yield
    requests.post("http://127.0.0.1:5000/shutdown")

