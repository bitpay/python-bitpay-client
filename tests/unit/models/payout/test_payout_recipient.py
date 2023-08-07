import pytest

from bitpay.models.payout.payout_recipient import PayoutRecipient


@pytest.mark.unit
def test_constructor():
    email = "some@email.com"
    guid = "someGuid"
    payout_recipient = PayoutRecipient(**{"email": email, "guid": guid})

    assert email == payout_recipient.get_email()
    assert guid == payout_recipient.get_guid()


@pytest.mark.unit
def test_modify_email():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_email(value)

    assert value == payout_recipient.get_email()


@pytest.mark.unit
def test_modify_label():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_label(value)

    assert value == payout_recipient.get_label()


@pytest.mark.unit
def test_modify_notification_url():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_notification_url(value)

    assert value == payout_recipient.get_notification_url()


@pytest.mark.unit
def test_modify_data():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_data(value)

    assert value == payout_recipient.get_data()


@pytest.mark.unit
def test_modify_status():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_status(value)

    assert value == payout_recipient.get_status()


@pytest.mark.unit
def test_modify_id():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_id(value)

    assert value == payout_recipient.get_id()


@pytest.mark.unit
def test_modify_shopper_id():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_shopper_id(value)

    assert value == payout_recipient.get_shopper_id()


@pytest.mark.unit
def test_modify_token():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_token(value)

    assert value == payout_recipient.get_token()


@pytest.mark.unit
def test_modify_guid():
    payout_recipient = PayoutRecipient()
    value = "someValue"
    payout_recipient.set_guid(value)

    assert value == payout_recipient.get_guid()
