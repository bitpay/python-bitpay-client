import pytest

from bitpay.models.bill.bill import Bill
from bitpay.models.bill.item import Item


@pytest.mark.unit
def test_constructor():
    city = "Rzeszow"
    country = "PL"
    items = [Item()]
    bill = Bill(city=city, country=country, items=items)

    assert city == bill.city
    assert country == bill.country
    assert items == bill.items


@pytest.mark.unit
def test_to_json():
    city = "Rzeszow"
    country = "PL"
    items = [Item()]
    bill = Bill(city=city, country=country, items=items)
    to_json = bill.to_json()

    assert city == to_json.get("city")
    assert country == to_json.get("country")
    assert len(items) == len(to_json.get("items"))
