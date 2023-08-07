import pytest

from bitpay.models.settlement.payout_info import PayoutInfo
from bitpay.models.settlement.settlement import Settlement
from bitpay.models.settlement.settlement_ledger_entry import SettlementLedgerEntry
from bitpay.models.settlement.with_holdings import WithHoldings


@pytest.mark.unit
def test_constructor():
    account_id = "1234"
    currency = "USD"
    payout_info = PayoutInfo()
    withholdings = [WithHoldings()]

    settlement = Settlement(
        **{
            "accountId": account_id,
            "currency": currency,
            "payoutInfo": payout_info,
            "withholdings": withholdings,
        }
    )

    assert settlement.get_account_id() == account_id
    assert settlement.get_currency() == currency
    assert settlement.get_payout_info() == payout_info
    assert settlement.get_withholdings() == withholdings

    withholdings_amount = 12.34
    settlement = Settlement(**{"withholdings": {"amount": withholdings_amount}})

    assert len(settlement.get_withholdings()) == 1
    assert settlement.get_withholdings()[0].get_amount() == withholdings_amount


@pytest.mark.unit
def test_modify_id():
    settlement = Settlement()
    value = "someValue"
    settlement.set_id(value)

    assert settlement.get_id()


@pytest.mark.unit
def test_modify_account_id():
    settlement = Settlement()
    value = "someValue"
    settlement.set_account_id(value)

    assert settlement.get_account_id()


@pytest.mark.unit
def test_modify_currency():
    settlement = Settlement()
    value = "someValue"
    settlement.set_currency(value)

    assert settlement.get_currency()


@pytest.mark.unit
def test_modify_payout_info():
    settlement = Settlement()
    value = PayoutInfo()
    settlement.set_payout_info(value)

    assert settlement.get_payout_info()


@pytest.mark.unit
def test_modify_status():
    settlement = Settlement()
    value = "someValue"
    settlement.set_status(value)

    assert settlement.get_status()


@pytest.mark.unit
def test_modify_date_created():
    settlement = Settlement()
    value = "someValue"
    settlement.set_date_created(value)

    assert settlement.get_date_created()


@pytest.mark.unit
def test_modify_date_executed():
    settlement = Settlement()
    value = "someValue"
    settlement.set_date_executed(value)

    assert settlement.get_date_executed()


@pytest.mark.unit
def test_modify_date_completed():
    settlement = Settlement()
    value = "someValue"
    settlement.set_date_completed(value)

    assert settlement.get_date_completed()


@pytest.mark.unit
def test_modify_opening_date():
    settlement = Settlement()
    value = "someValue"
    settlement.set_opening_date(value)

    assert settlement.get_opening_date()


@pytest.mark.unit
def test_modify_closing_date():
    settlement = Settlement()
    value = "someValue"
    settlement.set_closing_date(value)

    assert settlement.get_closing_date()


@pytest.mark.unit
def test_modify_opening_balance():
    settlement = Settlement()
    value = 12
    settlement.set_opening_balance(value)

    assert settlement.get_opening_balance()


@pytest.mark.unit
def test_modify_ledger_entries_sum():
    settlement = Settlement()
    value = 13
    settlement.set_ledger_entries_sum(value)

    assert settlement.get_ledger_entries_sum()


@pytest.mark.unit
def test_modify_withholdings():
    settlement = Settlement()
    value = [WithHoldings()]
    settlement.set_withholdings(value)

    assert settlement.get_withholdings()


@pytest.mark.unit
def test_modify_withholdings_sum():
    settlement = Settlement()
    value = 15
    settlement.set_withholdings_sum(value)

    assert settlement.get_withholdings_sum()


@pytest.mark.unit
def test_modify_total_amount():
    settlement = Settlement()
    value = 8
    settlement.set_total_amount(value)

    assert settlement.get_total_amount()


@pytest.mark.unit
def test_modify_ledger_entries():
    settlement = Settlement()
    value = [SettlementLedgerEntry()]
    settlement.set_ledger_entries(value)

    assert settlement.get_ledger_entries()


@pytest.mark.unit
def test_modify_token():
    settlement = Settlement()
    value = "someValue"
    settlement.set_token(value)

    assert settlement.get_token()
