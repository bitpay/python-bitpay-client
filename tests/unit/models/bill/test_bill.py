import pytest

from bitpay.models.bill.bill import Bill
from bitpay.models.bill.item import Item


@pytest.mark.unit
def test_constructor():
    city = "Rzeszow"
    country = "PL"
    items = [Item()]
    bill = Bill(
        "bill1234-ABCD",
        "USD",
        "some@email.com",
        **{"city": city, "country": country, "items": items}
    )

    assert city == bill.get_city()
    assert country == bill.get_country()
    assert items == bill.get_items()


@pytest.mark.unit
def test_to_json():
    city = "Rzeszow"
    country = "PL"
    items = [Item()]
    bill = Bill(
        "bill1234-ABCD",
        "USD",
        "some@email.com",
        **{"city": city, "country": country, "items": items}
    )
    to_json = bill.to_json()

    assert city == to_json.get("city")
    assert country == to_json.get("country")
    assert len(items) == len(to_json.get("items"))


@pytest.mark.unit
def test_modify_address1():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_address1(value)

    assert value == bill.get_address1()


@pytest.mark.unit
def test_modify_address2():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_address2(value)

    assert value == bill.get_address2()


@pytest.mark.unit
def test_modify_cc():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = ["someValue"]
    bill.set_cc(value)

    assert value == bill.get_cc()


@pytest.mark.unit
def test_modify_city():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_city(value)

    assert value == bill.get_city()


@pytest.mark.unit
def test_modify_country():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_country(value)

    assert value == bill.get_country()


@pytest.mark.unit
def test_modify_created_date():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_created_date(value)

    assert value == bill.get_created_date()


@pytest.mark.unit
def test_modify_currency():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "BCH"
    bill.set_currency(value)

    assert value == bill.get_currency()


@pytest.mark.unit
def test_modify_due_date():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_due_date(value)

    assert value == bill.get_due_date()


@pytest.mark.unit
def test_modify_email():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_email(value)

    assert value == bill.get_email()


@pytest.mark.unit
def test_modify_email():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "some@email.com"
    bill.set_email_bill(value)

    assert value == bill.get_email()


@pytest.mark.unit
def test_modify_id():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_id(value)

    assert value == bill.get_id()


@pytest.mark.unit
def test_modify_items():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = [Item()]
    bill.set_items(value)

    assert value == bill.get_items()


@pytest.mark.unit
def test_modify_merchant():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_merchant(value)

    assert value == bill.get_merchant()


@pytest.mark.unit
def test_modify_name():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_name(value)

    assert value == bill.get_name()


@pytest.mark.unit
def test_modify_number():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_number(value)

    assert value == bill.get_number()


@pytest.mark.unit
def test_modify_pass_processing_fee():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = False
    bill.set_pass_processing_fee(value)

    assert value == bill.get_pass_processing_fee()


@pytest.mark.unit
def test_modify_phone():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_phone(value)

    assert value == bill.get_phone()


@pytest.mark.unit
def test_modify_state():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_state(value)

    assert value == bill.get_state()


@pytest.mark.unit
def test_modify_status():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_status(value)

    assert value == bill.get_status()


@pytest.mark.unit
def test_modify_token():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_token(value)

    assert value == bill.get_token()


@pytest.mark.unit
def test_modify_url():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_url(value)

    assert value == bill.get_url()


@pytest.mark.unit
def test_modify_zip():
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    value = "someValue"
    bill.set_zip(value)

    assert value == bill.get_zip()
