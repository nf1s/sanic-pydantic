# -*- coding: utf-8 -*-
from functools import wraps

from pydantic import ValidationError
from sanic.response import json

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "0.1.0"


BODY_METHODS = ["POST", "PUT", "PATCH"]


def validate(request, obj):

    payload = None
    query = None

    if request.method in BODY_METHODS:
        payload = obj(**request.json).dict()

    params = request.args
    params = {k: v[0] for k, v in params.items()}
    query = obj(**params).dict()

    return dict(payload=payload, query=query)


def async_webargs(obj):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            try:
                result = validate(request, obj)
            except ValidationError as e:
                return json(e.errors())
            kwargs.update(result)
            response = await f(request, *args, **kwargs)
            return response

        return decorated_function

    return decorator


def webargs(obj):
    def decorator(f):
        @wraps(f)
        def decorated_function(request, *args, **kwargs):
            try:
                result = validate(request, obj)
            except ValidationError as e:
                return json(e.errors())
            kwargs.update(result)
            response = f(request, *args, **kwargs)
            return response

        return decorated_function

    return decorator
