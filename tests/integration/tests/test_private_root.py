import requests


def test_root_of_tests_private() -> None:
    response = requests.get("http://tests-private.test/")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert len(data) == 3
    assert data["service"] == "tests-private"
    assert isinstance(data["version"], str)
    assert data["tests"] is True


def test_root_of_mongodb_single() -> None:
    response = requests.get("http://tests-private.test/mongodb/mongodb-single")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "ok" in data
    assert data["ok"]


def test_root_of_mongodb_example() -> None:
    response = requests.get("http://tests-private.test/mongodb/mongodb-example")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "ok" in data
    assert data["ok"]


def test_root_of_mongodb_sharded_cluster() -> None:
    response = requests.get("http://tests-private.test/mongodb/mongodb-sharded-cluster")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "ok" in data
    assert data["ok"]
