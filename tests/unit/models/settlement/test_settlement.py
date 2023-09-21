import pytest

from bitpay.models.settlement.payout_info import PayoutInfo
from bitpay.models.settlement.settlement import Settlement
from bitpay.models.settlement.with_holdings import WithHoldings


@pytest.mark.unit
def test_constructor():
    account_id = "1234"
    currency = "USD"
    payout_info = PayoutInfo()
    withholdings = [WithHoldings()]

    settlement = Settlement(
        account_id=account_id,
        currency=currency,
        payoutInfo=payout_info,
        withholdings=withholdings,

    )

    assert settlement.account_id == account_id
    assert settlement.currency == currency
    assert settlement.payout_info == payout_info
    assert settlement.withholdings == withholdings

    withholdings_amount = 12.34
    settlement = Settlement(withholdings=[WithHoldings(amount=withholdings_amount)])

    assert len(settlement.withholdings) == 1
    assert settlement.withholdings[0].amount == withholdings_amount
