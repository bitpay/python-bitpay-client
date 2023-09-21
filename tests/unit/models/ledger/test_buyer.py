import pytest

from bitpay.models.ledger.buyer import Buyer


@pytest.mark.unit
def test_constructor():
    address1 = "someAddress"
    state = "someState"
    buyer = Buyer(address1=address1, state=state)

    assert address1 == buyer.address1
    assert state == buyer.state
