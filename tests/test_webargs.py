from examples.server import app
import json


def test_sanic_webargs_query():
    params = dict(name="ahmed")
    request, response = app.test_client.get("/get-request", params=params)
    expected_response = dict(payload=None, query=params)
    assert response.status == 200
    assert response.json == expected_response


def test_sanic_webargs_payload():
    data = dict(age=29)
    params = dict(name="ahmed")
    request, response = app.test_client.post(
        "/post-request", params=params, data=json.dumps(data)
    )
    expected_response = dict(payload=data, query=params)
    assert response.status == 200
    assert response.json == expected_response


def test_async_sanic_webargs_query():
    params = dict(name="ahmed")
    request, response = app.test_client.get(
        "/async-get-request", params=params
    )
    expected_response = dict(payload=None, query=params)
    assert response.status == 200
    assert response.json == expected_response


def test_async_sanic_webargs_payload():
    data = dict(age=29)
    params = dict(name="ahmed")
    request, response = app.test_client.post(
        "/async-post-request", params=params, data=json.dumps(data)
    )
    expected_response = dict(payload=data, query=params)
    assert response.status == 200
    assert response.json == expected_response


def test_sanic_webargs_payload_invalid():
    data = dict(invalid_body_param=29)
    params = dict(invalid_query_param="ahmed")
    request, response = app.test_client.post(
        "/post-request", params=params, data=json.dumps(data)
    )
    assert response.status == 422
