import pytest

from bitpay.models.payout.payout_recipient import PayoutRecipient


@pytest.mark.unit
def test_constructor():
    email = "some@email.com"
    guid = "someGuid"
    payout_recipient = PayoutRecipient(email=email, guid=guid)

    assert email == payout_recipient.email
    assert guid == payout_recipient.guid
