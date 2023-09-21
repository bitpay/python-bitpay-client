import pytest

from bitpay.models.bill.item import Item


@pytest.mark.unit
def test_constructor():
    id = "123"
    price = 45.3
    quantity = 23
    item = Item(id=id, price=price, quantity=quantity)

    assert id == item.id
    assert price == item.price
    assert quantity == item.quantity


@pytest.mark.unit
def test_to_json():
    id = "123"
    price = 45.3
    quantity = 23
    item = Item(id=id, price=price, quantity=quantity).to_json()

    assert id == item.get("id")
    assert price == item.get("price")
    assert quantity == item.get("quantity")
