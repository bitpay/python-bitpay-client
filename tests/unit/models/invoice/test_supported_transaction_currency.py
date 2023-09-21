import pytest

from bitpay.models.invoice.supported_transaction_currency import (
    SupportedTransactionCurrency,
)


@pytest.mark.unit
def test_constructor():
    enabled = True
    reason = "someReason"

    supported_transaction_currency = SupportedTransactionCurrency(enabled=enabled, reason=reason)

    assert enabled == supported_transaction_currency.enabled
    assert reason == supported_transaction_currency.reason
