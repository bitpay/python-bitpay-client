import pytest

from bitpay.models.invoice.buyer import Buyer


@pytest.mark.unit
def test_constructor():
    address1 = "someAddress"
    country = "PL"
    buyer_email = "someEmail"
    buyer = Buyer(address1=address1, country=country, email=buyer_email)

    assert address1 == buyer.address1
    assert country == buyer.country
    assert buyer_email == buyer.email


@pytest.mark.unit
def test_to_json():
    address1 = "someAddress"
    country = "PL"
    buyer_email = "someEmail"
    json = Buyer(address1=address1, country=country, email=buyer_email).to_json()

    assert address1 == json.get("address1")
    assert country == json.get("country")
    assert buyer_email == json.get("email")
