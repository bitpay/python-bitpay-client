import pytest

from bitpay.models.invoice.itemized_details import ItemizedDetails


@pytest.mark.unit
def test_constructor():
    amount = 12.45
    description = "someDescription"
    is_fee = True
    itemized_details = ItemizedDetails(amount=amount, description=description, is_fee=is_fee)

    assert amount == itemized_details.amount
    assert description == itemized_details.description
    assert is_fee == itemized_details.is_fee
