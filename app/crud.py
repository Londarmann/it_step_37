from app.models import Item
from app.schemas import ItemCreate


async def creat_item(item_data: ItemCreate) -> Item:
    item = await Item.create(**item_data.dict())
    return item


async def get_items() -> list[Item]:
    return await Item.all()


async def get_item_by_id(item_id: int) -> Item:
    return await Item.get(id=item_id)


async def delete_item(item_id: int) -> None:
    item = await Item.get(id=item_id)
    await item.delete()


async def update_item(item_id: int, item_data: ItemCreate) -> Item:
    item = await Item.get(id=item_id)
    item.name = item_data.name
    item.description = item_data.description
    item.price = item_data.price
    item.tax = item_data.tax
    await item.save()
    return item