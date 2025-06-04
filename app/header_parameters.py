from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel


app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
    

# Duplicate headers
@app.get("/duplicate")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

# Header parameter models
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []
    model_config = {"extra": "forbid"}

@app.get("/models")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers