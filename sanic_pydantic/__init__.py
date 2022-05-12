# -*- coding: utf-8 -*-
import asyncio
from functools import wraps

from pydantic import ValidationError
from sanic.response import json

__author__ = "Ahmed Nafies <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies"
__license__ = "MIT"
__version__ = "1.3.0"


BODY_METHODS = ["POST", "PUT", "PATCH"]


class Error(Exception):
    def __init__(self, message):
        self.message = message


class InvalidOperation(Error):
    pass


def validate(request, query, body, path, headers):

    payload = None
    query_params = None
    path_params = None
    header_params = None

    if body and request.method not in BODY_METHODS:
        raise InvalidOperation(
            f"Http method '{request.method}' does not contain a payload,"
            "yet a `Pyndatic` model for body was supplied"
        )

    if body:
        payload = body(**request.json).dict()

    if query:
        params = request.args
        params = {k: v[0] for k, v in params.items()}
        query_params = query(**params).dict()

    if path:
        path_params = path(**request.match_info).dict()

    if headers:
        header_params = headers(**request.headers).dict()

    return dict(
        payload=payload,
        query=query_params,
        headers=header_params,
        **path_params if path_params else {},
    )


def webargs(query=None, body=None, path=None, headers=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(request, *args, **kwargs):
            try:
                result = validate(request, query, body, path, headers)
            except ValidationError as e:
                return json(e.errors(), status=422)
            kwargs.update(result)
            if not asyncio.iscoroutinefunction(f):
                response = f(request, *args, **kwargs)
                return response
            else:

                async def temp_():
                    response = await f(request, *args, **kwargs)
                    return response

                return temp_()

        return decorated_function

    return decorator
