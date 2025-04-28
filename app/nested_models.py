from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


# Nested Models
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = []
    images: list[Image] | None = None


class Profile(BaseModel):
    name: str
    bio: str
    email: str
    age: int
    tags: set[str] = set()
    images: list[Image] | None = None

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]