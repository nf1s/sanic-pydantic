from typing import NamedTuple, Union

import pytest

from examples.server import BodyModel, HeadersModel, PathModel, QueryModel
from sanic_pydantic import InvalidOperation, validate


class MockRequest(NamedTuple):
    method: str = "GET"
    json: Union[dict, None] = None
    args: Union[dict, None] = None
    headers: Union[dict, None] = None


def test_webargs_invalid_method():
    request = MockRequest()
    with pytest.raises(InvalidOperation):
        validate(request, QueryModel, BodyModel, PathModel, HeadersModel)


def test_webargs_query():
    query = dict(name=["ahmed"])
    request = MockRequest(method="GET", args=query)
    expected_data = dict(payload=None, query=dict(name="ahmed"), headers=None)
    data = validate(request, QueryModel, None, None, None)
    assert data == expected_data


def test_webargs_payload():
    query = dict(name=["ahmed"])
    body = dict(age=29)
    request = MockRequest(method="POST", args=query, json=body)
    expected_data = dict(
        payload=dict(age=29), query=dict(name="ahmed"), headers=None
    )
    data = validate(request, QueryModel, BodyModel, None, None)
    assert data == expected_data
