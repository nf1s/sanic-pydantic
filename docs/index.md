# Getting Started

A library for parsing and validating http requests for sanic web-framework using pydantic library 

Full code on github [here](https://github.com/ahmednafies/sanic_pydantic)

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
from sanic_pydantic import webargs

from sanic import Sanic
from sanic.response import json
from pydantic import BaseModel

app = Sanic("new app")


class BodyModel(BaseModel):
    age: int


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```
