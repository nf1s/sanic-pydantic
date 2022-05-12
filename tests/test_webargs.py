import json

from examples.server import app


def test_sanic_webargs_query():
    params = dict(name="ahmed")
    headers = dict(api_key="hello")
    _, response = app.test_client.get(
        "/get-request", params=params, headers={"x-api-key": "hello"}
    )
    expected_response = dict(payload=None, query=params, headers=headers)
    assert response.status == 200
    assert response.json == expected_response


def test_sanic_webargs_path():
    _, response = app.test_client.get("/get/1")
    expected_response = dict(payload=None, query=None, id=1, headers=None)
    assert response.status == 200
    assert response.json == expected_response


def test_sanic_webargs_payload():
    data = dict(age=29)
    params = dict(name="ahmed")
    _, response = app.test_client.post(
        "/post-request", params=params, data=json.dumps(data)
    )
    expected_response = dict(payload=data, query=params, headers=None)
    assert response.status == 200
    assert response.json == expected_response


def test_async_sanic_webargs_query():
    params = dict(name="ahmed")
    _, response = app.test_client.get("/async-get-request", params=params)
    expected_response = dict(payload=None, query=params, headers=None)
    assert response.status == 200
    assert response.json == expected_response


def test_async_sanic_webargs_payload():
    data = dict(age=29)
    params = dict(name="ahmed")
    _, response = app.test_client.post(
        "/async-post-request", params=params, data=json.dumps(data)
    )
    expected_response = dict(payload=data, query=params, headers=None)
    assert response.status == 200
    assert response.json == expected_response


def test_sanic_webargs_payload_invalid():
    data = dict(invalid_body_param=29)
    params = dict(invalid_query_param="ahmed")
    _, response = app.test_client.post(
        "/post-request", params=params, data=json.dumps(data)
    )
    assert response.status == 422
