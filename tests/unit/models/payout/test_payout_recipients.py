import pytest

from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients


@pytest.mark.unit
def test_constructor():
    guid = "1234"
    recipients = [PayoutRecipient(), PayoutRecipient()]
    payout_recipients = PayoutRecipients(**{"guid": guid, "recipients": recipients})

    assert guid == payout_recipients.get_guid()
    assert recipients == payout_recipients.get_recipients()

@pytest.mark.unit
def test_modify_guid():
    payout_recipients = PayoutRecipients()
    value = "someValue"
    payout_recipients.set_guid(value)

    assert payout_recipients.get_guid() == value


@pytest.mark.unit
def test_modify_recipients():
    payout_recipients = PayoutRecipients()
    value = [PayoutRecipient(), PayoutRecipient()]
    payout_recipients.set_recipients(value)

    assert payout_recipients.get_recipients() == value


@pytest.mark.unit
def test_modify_token():
    payout_recipients = PayoutRecipients()
    value = "someValue"
    payout_recipients.set_token(value)

    assert payout_recipients.get_token() == value

