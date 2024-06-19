from fastapi import APIRouter

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

from src.config import (
    MONGODB_SINGLE_HOST,
    MONGODB_SINGLE_PORT,
    MONGODB_SINGLE_USER,
    MONGODB_SINGLE_PASSWORD,
    MONGODB_EXAMPLE_HOST,
    MONGODB_EXAMPLE_PORT,
    MONGODB_EXAMPLE_USER,
    MONGODB_EXAMPLE_PASSWORD,
)

router = APIRouter()


def _check_mongodb_service(mongo_uri: str) -> dict:
    mongo_client = MongoClient(mongo_uri)

    try:
        # The ismaster command is cheap and does not require auth.
        res = mongo_client.admin.command("hello")
        if res.get("ok") != 1:
            return {
                "ok": False,
                "error": "MongoDB hello command ok is not 1",
                "payload": None,
            }
    except ConnectionFailure as e:
        return {
            "ok": False,
            "error": "MongoDB connection failure",
            "payload": str(e),
        }
    except OperationFailure as e:
        return {
            "ok": False,
            "error": "MongoDB operation failure",
            "payload": str(e),
            "test": mongo_uri,
        }

    return {
        "ok": True,
        "error": None,
        "payload": None,
    }


@router.get("/mongodb-single")
def route_mongodb_single() -> dict:
    if MONGODB_SINGLE_USER is None:
        return {
            "ok": False,
            "error": "MONGODB_SINGLE_USER is not set",
            "payload": None,
        }

    if MONGODB_SINGLE_PASSWORD is None:
        return {
            "ok": False,
            "error": "MONGODB_SINGLE_PASSWORD is not set",
            "payload": None,
        }

    if MONGODB_SINGLE_HOST is None:
        return {
            "ok": False,
            "error": "MONGODB_SINGLE_HOST is not set",
            "payload": None,
        }

    mongo_uri = f"mongodb://{MONGODB_SINGLE_USER}:{MONGODB_SINGLE_PASSWORD}"
    mongo_uri += f"@{MONGODB_SINGLE_HOST}:{MONGODB_SINGLE_PORT}"
    mongo_uri += "/?replicaSet=rs0&readPreference=primaryPreferred"

    return _check_mongodb_service(mongo_uri)


@router.get("/mongodb-example")
def route_mongodb_example() -> dict:
    if MONGODB_EXAMPLE_USER is None:
        return {
            "ok": False,
            "error": "MONGODB_EXAMPLE_USER is not set",
            "payload": None,
        }

    if MONGODB_EXAMPLE_PASSWORD is None:
        return {
            "ok": False,
            "error": "MONGODB_EXAMPLE_PASSWORD is not set",
            "payload": None,
        }

    if MONGODB_EXAMPLE_HOST is None:
        return {
            "ok": False,
            "error": "MONGODB_EXAMPLE_HOST is not set",
            "payload": None,
        }

    mongo_uri = f"mongodb://{MONGODB_EXAMPLE_USER}:{MONGODB_EXAMPLE_PASSWORD}"
    mongo_uri += f"@{MONGODB_EXAMPLE_HOST}:{MONGODB_EXAMPLE_PORT}"

    return _check_mongodb_service(mongo_uri)
