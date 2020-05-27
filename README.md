# Sanic Pyndatic

A library for parsing and validating http requests for sanic web-framework using pydantic library 

Full documentation [here](https://ahmednafies.github.io/sanic_pydantic/)

## Requirements

	python >= 3.7

## How to install

```bash
pip install sanic-pydantic
```

## Dependencies

	pydantic

## Example

```python

from sanic_pydantic import webargs, async_webargs

from sanic import Sanic
from sanic.response import json
from pydantic import BaseModel

app = Sanic("new app")


class QueryModel(BaseModel):
    name: str


class BodyModel(BaseModel):
    age: int

@app.route("/get-request", methods=["GET"])
@webargs(query=QueryModel)
def example_get_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


@app.route("/async-get-request", methods=["GET"])
@async_webargs(query=QueryModel)
async def async_example_get_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


@app.route("/async-post-request", methods=["POST"])
@async_webargs(query=QueryModel, body=BodyModel)
async def async_example_post_endpoint(request, **kwargs):
    prit(kwargs)
    response = json(kwargs)
    return responsen

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```
