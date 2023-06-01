import pytest

from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_transaction import PayoutTransaction


@pytest.mark.unit
def test_constructor():
    amount = 12.34
    currency = "USD"
    ledger_currency = "BCH"
    account = "1234"
    notification_url = "https://url.com"
    transactions = [PayoutTransaction()]
    payout = Payout(
        amount,
        currency,
        ledger_currency,
        **{
            "notificationURL": notification_url,
            "account": account,
            "transactions": transactions,
        }
    )

    assert amount == payout.get_amount()
    assert currency == payout.get_currency()
    assert ledger_currency == payout.get_ledger_currency()
    assert transactions == payout.get_transactions()


@pytest.mark.unit
def test_modify_token():
    payout = Payout()
    value = "someValue"
    payout.set_token(value)

    assert value == payout.get_token()


@pytest.mark.unit
def test_modify_amount():
    payout = Payout()
    value = 12
    payout.set_amount(value)

    assert value == payout.get_amount()


@pytest.mark.unit
def test_modify_currency():
    payout = Payout()
    value = "USD"
    payout.set_currency(value)

    assert value == payout.get_currency()


@pytest.mark.unit
def test_modify_effective_date():
    payout = Payout()
    value = "someValue"
    payout.set_effective_date(value)

    assert value == payout.get_effective_date()


@pytest.mark.unit
def test_modify_reference():
    payout = Payout()
    value = "someValue"
    payout.set_reference(value)

    assert value == payout.get_reference()


@pytest.mark.unit
def test_modify_notification_email():
    payout = Payout()
    value = "someValue"
    payout.set_notification_email(value)

    assert value == payout.get_notification_email()


@pytest.mark.unit
def test_modify_notification_url():
    payout = Payout()
    value = "someValue"
    payout.set_notification_url(value)

    assert value == payout.get_notification_url()


@pytest.mark.unit
def test_modify_redirect_url():
    payout = Payout()
    value = "someValue"
    payout.set_redirect_url(value)

    assert value == payout.get_redirect_url()


@pytest.mark.unit
def test_modify_ledger_currency():
    payout = Payout()
    value = "BCH"
    payout.set_ledger_currency(value)

    assert value == payout.get_ledger_currency()


@pytest.mark.unit
def test_modify_id():
    payout = Payout()
    value = "someValue"
    payout.set_id(value)

    assert value == payout.get_id()


@pytest.mark.unit
def test_modify_shopper_id():
    payout = Payout()
    value = "someValue"
    payout.set_shopper_id(value)

    assert value == payout.get_shopper_id()


@pytest.mark.unit
def test_modify_recipient_id():
    payout = Payout()
    value = "someValue"
    payout.set_recipient_id(value)

    assert value == payout.get_recipient_id()


@pytest.mark.unit
def test_modify_exchange_rates():
    payout = Payout()
    value = []
    payout.set_exchange_rates(value)

    assert value == payout.get_exchange_rates()


@pytest.mark.unit
def test_modify_account():
    payout = Payout()
    value = "someValue"
    payout.set_account(value)

    assert value == payout.get_account()


@pytest.mark.unit
def test_modify_email():
    payout = Payout()
    value = "someValue"
    payout.set_email(value)

    assert value == payout.get_email()


@pytest.mark.unit
def test_modify_label():
    payout = Payout()
    value = "someValue"
    payout.set_label(value)

    assert value == payout.get_label()


@pytest.mark.unit
def test_modify_support_phone():
    payout = Payout()
    value = "someValue"
    payout.set_support_phone(value)

    assert value == payout.get_support_phone()


@pytest.mark.unit
def test_modify_status():
    payout = Payout()
    value = "someValue"
    payout.set_status(value)

    assert value == payout.get_status()


@pytest.mark.unit
def test_modify_message():
    payout = Payout()
    value = "someValue"
    payout.set_message(value)

    assert value == payout.get_message()


@pytest.mark.unit
def test_modify_request_date():
    payout = Payout()
    value = "someValue"
    payout.set_request_date(value)

    assert value == payout.get_request_date()


@pytest.mark.unit
def test_modify_date_executed():
    payout = Payout()
    value = "someValue"
    payout.set_date_executed(value)

    assert value == payout.get_date_executed()


@pytest.mark.unit
def test_modify_transactions():
    payout = Payout()
    value = []
    payout.set_transactions(value)

    assert value == payout.get_transactions()


@pytest.mark.unit
def test_modify_account_id():
    payout = Payout()
    value = "someValue"
    payout.set_account_id(value)

    assert value == payout.get_account_id()
