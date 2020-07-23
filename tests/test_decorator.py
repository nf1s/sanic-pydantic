import pytest
from typing import NamedTuple

from sanic_pydantic import InvalidOperation
from sanic_pydantic import validate
from examples.server import BodyModel, QueryModel, PathModel


class MockRequest(NamedTuple):
    method: str = "GET"
    json: dict = None
    args: dict = None


def test_webargs_invalid_method():
    request = MockRequest()
    with pytest.raises(InvalidOperation):
        validate(request, QueryModel, BodyModel, PathModel)


def test_webargs_query():
    query = dict(name=["ahmed"])
    request = MockRequest(method="GET", args=query)
    expected_data = dict(payload=None, query=dict(name="ahmed"))
    data = validate(request, QueryModel, None, None)
    assert data == expected_data


def test_webargs_payload():
    query = dict(name=["ahmed"])
    body = dict(age=29)
    request = MockRequest(method="POST", args=query, json=body)
    expected_data = dict(payload=dict(age=29), query=dict(name="ahmed"))
    data = validate(request, QueryModel, BodyModel, None)
    assert data == expected_data
