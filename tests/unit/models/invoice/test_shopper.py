import pytest

from bitpay.models.invoice.shopper import Shopper


@pytest.mark.unit
def test_constructor():
    user = "someUser"
    shopper = Shopper(**{"user": user})

    assert user == shopper.get_user()


@pytest.mark.unit
def test_modify_user():
    shopper = Shopper()
    value = "someUser"
    shopper.set_user(value)

    assert value == shopper.get_user()
