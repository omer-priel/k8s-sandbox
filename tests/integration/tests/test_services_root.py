import requests


def test_root_of_nginx_example() -> None:
    response = requests.get("http://nginx-example.test/index.json")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "nginx-example"
    assert isinstance(data["version"], str)


def test_root_of_express_example() -> None:
    response = requests.get("http://express-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "express-example"
    assert isinstance(data["version"], str)


def test_root_of_fastapi_example() -> None:
    response = requests.get("http://fastapi-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "fastapi-example"
    assert isinstance(data["version"], str)


def test_root_of_flask_example() -> None:
    response = requests.get("http://flask-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "flask-example"
    assert isinstance(data["version"], str)


def test_root_of_fastify_example() -> None:
    response = requests.get("http://fastify-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "fastify-example"
    assert isinstance(data["version"], str)


def test_root_of_gohttp_example() -> None:
    response = requests.get("http://gohttp-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "gohttp-example"
    assert isinstance(data["version"], str)


def test_root_of_gin_example() -> None:
    response = requests.get("http://gin-example.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data["service"] == "gin-example"
    assert isinstance(data["version"], str)
