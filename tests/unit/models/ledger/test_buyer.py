import pytest

from bitpay.models.ledger.buyer import Buyer


@pytest.mark.unit
def test_constructor():
    address1 = "someAddress"
    state = "someState"
    buyer = Buyer(**{"address1": address1, "state": state})

    assert address1 == buyer.get_address1()
    assert state == buyer.get_state()


@pytest.mark.unit
def test_modify_name():
    buyer = Buyer()
    value = "someValue"
    buyer.set_name(value)

    assert value == buyer.get_name()


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
def test_modify_city():
    buyer = Buyer()
    value = "someValue"
    buyer.set_city(value)

    assert value == buyer.get_city()


@pytest.mark.unit
def test_modify_state():
    buyer = Buyer()
    value = "someValue"
    buyer.set_state(value)

    assert value == buyer.get_state()


@pytest.mark.unit
def test_modify_zip():
    buyer = Buyer()
    value = "someValue"
    buyer.set_zip(value)

    assert value == buyer.get_zip()


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
def test_modify_phone():
    buyer = Buyer()
    value = "someValue"
    buyer.set_phone(value)

    assert value == buyer.get_phone()


@pytest.mark.unit
def test_modify_notify():
    buyer = Buyer()
    value = "someValue"
    buyer.set_notify(value)

    assert value == buyer.get_notify()
