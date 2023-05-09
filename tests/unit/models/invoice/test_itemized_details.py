import pytest

from bitpay.models.invoice.itemized_details import ItemizedDetails


@pytest.mark.unit
def test_constructor():
    amount = 12.45
    description = "someDescription"
    is_fee = True
    itemized_details = ItemizedDetails(**{"amount": amount, "description": description, "isFee": is_fee})

    assert amount == itemized_details.get_amount()
    assert description == itemized_details.get_description()
    assert is_fee == itemized_details.get_is_fee()


@pytest.mark.unit
def test_modify_amount():
    itemized_details = ItemizedDetails()
    value = 12.45
    itemized_details.set_amount(value)

    assert value == itemized_details.get_amount()


@pytest.mark.unit
def test_modify_description():
    itemized_details = ItemizedDetails()
    value = "someValue"
    itemized_details.set_description(value)

    assert value == itemized_details.get_description()


@pytest.mark.unit
def test_modify_is_fee():
    itemized_details = ItemizedDetails()
    value = True
    itemized_details.set_is_fee(value)

    assert value == itemized_details.get_is_fee()
