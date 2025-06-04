from typing import Annotated
from pydantic import BaseModel

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


# with pydantic model
class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

    model_config = {"extra": "forbid"}


@app.get("/items/item")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies