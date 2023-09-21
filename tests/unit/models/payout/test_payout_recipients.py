import pytest

from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients


@pytest.mark.unit
def test_constructor():
    guid = "1234"
    recipients = [PayoutRecipient(), PayoutRecipient()]
    payout_recipients = PayoutRecipients(guid=guid, recipients=recipients)

    assert guid == payout_recipients.guid
    assert recipients == payout_recipients.recipients
