import pytest

from bitpay.models.invoice.supported_transaction_currencies import (
    SupportedTransactionCurrencies,
)
from bitpay.models.invoice.supported_transaction_currency import (
    SupportedTransactionCurrency,
)


@pytest.mark.unit
def test_constructor():
    btc = SupportedTransactionCurrency(enabled=True)
    pax = SupportedTransactionCurrency(enabled=False)
    supported_transaction_currencies = SupportedTransactionCurrencies(btc=btc, pax=pax)

    assert True is supported_transaction_currencies.btc.enabled
    assert False is supported_transaction_currencies.pax.enabled
