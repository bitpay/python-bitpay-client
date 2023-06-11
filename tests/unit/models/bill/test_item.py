import pytest

from bitpay.models.bill.item import Item


@pytest.mark.unit
def test_constructor():
    id = "123"
    price = 45.3
    quantity = 23
    item = Item(**{"id": id, "price": price, "quantity": quantity})

    assert id == item.get_id()
    assert price == item.get_price()
    assert quantity == item.get_quantity()


@pytest.mark.unit
def test_to_json():
    id = "123"
    price = 45.3
    quantity = 23
    item = Item(**{"id": id, "price": price, "quantity": quantity}).to_json()

    assert id == item.get("id")
    assert price == item.get("price")
    assert quantity == item.get("quantity")


@pytest.mark.unit
def test_modify_description():
    item = Item()
    value = "someValue"
    item.set_description(value)

    assert value == item.get_description()


@pytest.mark.unit
def test_modify_id():
    item = Item()
    value = "someValue"
    item.set_id(value)

    assert value == item.get_id()


@pytest.mark.unit
def test_modify_price():
    item = Item()
    value = 12.45
    item.set_price(value)

    assert value == item.get_price()


@pytest.mark.unit
def test_modify_quantity():
    item = Item()
    value = 1
    item.set_quantity(value)

    assert value == item.get_quantity()
