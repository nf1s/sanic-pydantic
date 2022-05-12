# Getting Started
[![CircleCI](https://circleci.com/gh/nf1s/sanic-pydantic.svg?style=shield)](https://circleci.com/gh/nf1s/sanic-pydantic) ![CircleCI](https://img.shields.io/circleci/build/github/nf1s/sanic-pydantic/master) [![codecov](https://codecov.io/gh/nf1s/sanic-pydantic/branch/master/graph/badge.svg)](https://codecov.io/gh/nf1s/sanic-pydantic) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/nf1s/sanic-pydantic) ![GitHub top language](https://img.shields.io/github/languages/top/nf1s/sanic-pydantic) ![PyPI](https://img.shields.io/pypi/v/sanic-pydantic) [![Downloads](https://pepy.tech/badge/sanic-pydantic)](https://pepy.tech/project/sanic-pydantic) ![license](https://img.shields.io/badge/license-MIT-green)
 ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/nf1s/sanic-pydantic) ![GitHub issues](https://img.shields.io/github/issues/nf1s/sanic-pydantic) ![GitHub closed issues](https://img.shields.io/github/issues-closed/nf1s/sanic-pydantic)

A library for parsing and validating http requests for sanic web-framework using pydantic library 

Full code on github [here](https://github.com/nf1s/sanic-pydantic)

## Requirements

	python >= 3.8

## How to install

```bash
pip install sanic-pydantic
```

## Dependencies

	pydantic

## Example

```python
from sanic_pydantic import webargs

from sanic import Sanic
from sanic.response import json
from pydantic import BaseModel

app = Sanic("new app")


class BodyModel(BaseModel):
    age: int


class QueryModel(BaseModel):
    name: str


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```
