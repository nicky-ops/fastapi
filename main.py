from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated, Literal, List, Union


# Pydantic models
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300, examples=["A very nice Item", "A very nice Item with a long description"]
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'Foo',
                    'description': 'A very nice Item',
                    'price': 35.4,
                    'tax': 3.2,
                }
            ] 
        }
    }


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item1(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = []
    image: List[Image] | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


fake_items_db = [{'item_name': 'Foo', 'id': 1}, {'item_name': 'Bar', 'id': 2}, {'item_name': 'Baz', 'id': 3}]


@app.get("/")
async def root():
    return {'message': 'Hello World'}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get("/users/me")
async def read_user_me():
    return {'user_id': 'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


# query parameters
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Optional query parameters
@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': 'This is an amazing item that has a long description'})
    return item

# Required query parameter
@app.get('/itms/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item


# Request body
@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


# Request body + path parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}

# Request body + path + query parameters
@app.put("/iems/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title='The ID of the item to get', gt=0, le=1000)],
     size: Annotated[float, Query(gt=0, lt=10.5)],
    item: Item, q: str | None = None,
    ):
    item_dict = {'item_id': item_id, **item.dict()}
    if q:
        item_dict.update({'q': q})
    return item_dict

# Query parameters + string validations
@app.get('/itemss/')
async def read_items(q: Annotated[str | None, Query(max_length=50, min_length=3, pattern='^fixedquery$')] = 'fixedquery'):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}, {'item_id': 'Baz'}]}
    if q:
        results.update({'q': q})
    return results

# Query parameter list
@app.get('/itmss/')
async def read_items(
    q: Annotated[
        list[str] | None, 
        Query(
            title="Query String",
            description='Query string fo the items to search in the database that have a good match',
            min_length=3,
            deprecated=True,
            ),
            ] = None,
    ):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}, {'item_id': 'Baz'}]}
    if q:
        results.update({'q': q})
    return results

# Query parameters with a Pydantic Model
@app.get('/newitems/')
async def get_new_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


# Multiple body parameters
@app.put('/putitems/{item_id}')
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results