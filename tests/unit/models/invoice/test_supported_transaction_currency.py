import pytest

from bitpay.models.invoice.supported_transaction_currency import (
    SupportedTransactionCurrency,
)


@pytest.mark.unit
def test_constructor():
    enabled = True
    reason = "someReason"

    supported_transaction_currency = SupportedTransactionCurrency(
        **{"enabled": enabled, "reason": reason}
    )

    assert enabled == supported_transaction_currency.get_enabled()
    assert reason == supported_transaction_currency.get_reason()


@pytest.mark.unit
def test_modify_enabled():
    supported_transaction_currency = SupportedTransactionCurrency()
    value = True
    supported_transaction_currency.set_enabled(value)

    assert value == supported_transaction_currency.get_enabled()


@pytest.mark.unit
def test_modify_reason():
    supported_transaction_currency = SupportedTransactionCurrency()
    value = "someValue"
    supported_transaction_currency.set_reason(value)

    assert value == supported_transaction_currency.get_reason()
