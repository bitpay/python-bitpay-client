import pytest

from bitpay.models.invoice.buyer import Buyer


@pytest.mark.unit
def test_constructor():
    address1 = "someAddress"
    country = "PL"
    buyer_email = "someEmail"
    buyer = Buyer(
        **{"address1": address1, "country": country, "buyerEmail": buyer_email}
    )

    assert address1 == buyer.get_address1()
    assert country == buyer.get_country()
    assert buyer_email == buyer.get_buyer_email()


@pytest.mark.unit
def test_to_json():
    address1 = "someAddress"
    country = "PL"
    buyer_email = "someEmail"
    json = Buyer(
        **{"address1": address1, "country": country, "buyerEmail": buyer_email}
    ).to_json()

    assert address1 == json.get("address1")
    assert country == json.get("country")
    assert buyer_email == json.get("buyerEmail")


@pytest.mark.unit
def test_modify_address1():
    buyer = Buyer()
    value = "someValue"
    buyer.set_address1(value)

    assert value == buyer.get_address1()


@pytest.mark.unit
def test_modify_address2():
    buyer = Buyer()
    value = "someValue"
    buyer.set_address2(value)

    assert value == buyer.get_address2()


@pytest.mark.unit
def test_modify_buyer_email():
    buyer = Buyer()
    value = "someValue"
    buyer.set_buyer_email(value)

    assert value == buyer.get_buyer_email()


@pytest.mark.unit
def test_modify_country():
    buyer = Buyer()
    value = "someValue"
    buyer.set_country(value)

    assert value == buyer.get_country()


@pytest.mark.unit
def test_modify_email():
    buyer = Buyer()
    value = "someValue"
    buyer.set_email(value)

    assert value == buyer.get_email()


@pytest.mark.unit
def test_modify_locality():
    buyer = Buyer()
    value = "someValue"
    buyer.set_locality(value)

    assert value == buyer.get_locality()


@pytest.mark.unit
def test_modify_name():
    buyer = Buyer()
    value = "someValue"
    buyer.set_name(value)

    assert value == buyer.get_name()


@pytest.mark.unit
def test_modify_notify():
    buyer = Buyer()
    value = True
    buyer.set_notify(value)

    assert value == buyer.get_notify()


@pytest.mark.unit
def test_modify_phone():
    buyer = Buyer()
    value = "someValue"
    buyer.set_phone(value)

    assert value == buyer.get_phone()


@pytest.mark.unit
def test_modify_postal_code():
    buyer = Buyer()
    value = "someValue"
    buyer.set_postal_code(value)

    assert value == buyer.get_postal_code()


@pytest.mark.unit
def test_modify_region():
    buyer = Buyer()
    value = "someValue"
    buyer.set_region(value)

    assert value == buyer.get_region()
