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
        amount=amount,
        currency=currency,
        ledger_currency=ledger_currency,
        notification_url=notification_url,
        account=account,
        transactions=transactions
    )

    assert amount == payout.amount
    assert currency == payout.currency
    assert ledger_currency == payout.ledger_currency
    assert transactions == payout.transactions
