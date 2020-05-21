from sanic_pydantic import async_webargs

from sanic import Sanic
from sanic.response import json
from pydantic import BaseModel

app = Sanic("new app")


class User(BaseModel):
    id: int
    name: str


@app.route("/")
@async_webargs(User)
async def test(request, **kwargs):
    print(kwargs)
    response = json({"hello": "world"})
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
