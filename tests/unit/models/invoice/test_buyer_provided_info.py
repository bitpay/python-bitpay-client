import pytest

from bitpay.models.invoice.buyer_provided_info import BuyerProvidedInfo


@pytest.mark.unit
def test_constructor():
    name = "someName"
    phone_number = "1234"
    buyer_provided_info = BuyerProvidedInfo(name=name, phoneNumber=phone_number)

    assert name == buyer_provided_info.name
    assert phone_number == buyer_provided_info.phone_number
