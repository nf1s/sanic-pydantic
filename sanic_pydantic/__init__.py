# -*- coding: utf-8 -*-
import asyncio
from functools import wraps

from pydantic import ValidationError
from sanic.response import json

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "1.2.1"


BODY_METHODS = ["POST", "PUT", "PATCH"]


class Error(Exception):
    def __init__(self, message):
        self.message = message


class InvalidOperation(Error):
    pass


def validate(request, query, body, path):

    payload = None
    query_params = None
    path_params = None

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

    return dict(
        payload=payload,
        query=query_params,
        **path_params if path_params else {},
    )


def webargs(query=None, body=None, path=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(request, *args, **kwargs):
            try:
                result = validate(request, query, body, path)
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
