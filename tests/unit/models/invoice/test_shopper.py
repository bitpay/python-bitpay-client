import pytest

from bitpay.models.invoice.shopper import Shopper


@pytest.mark.unit
def test_constructor():
    user = "someUser"
    shopper = Shopper(user=user)

    assert user == shopper.user
