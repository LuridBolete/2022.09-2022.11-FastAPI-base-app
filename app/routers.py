from fastapi import APIRouter

from app import contracts

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World!"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/users/")
async def read_user(user_id: str, q: str | None = None):
    """Description.

    Args:
        user_id (str): user_id
        q (str | None, optional): some q. Defaults to None.
    """
    if q:
        return {"user_id": user_id, "q": q}
    return {"user_id": user_id}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


@router.post("/items/")
async def create_item(item: contracts.Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
