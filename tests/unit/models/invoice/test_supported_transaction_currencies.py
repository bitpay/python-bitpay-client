import pytest

from bitpay.models.invoice.supported_transaction_currencies import SupportedTransactionCurrencies
from bitpay.models.invoice.supported_transaction_currency import SupportedTransactionCurrency


@pytest.mark.unit
def test_constructor():
    btc = SupportedTransactionCurrency(**{"enabled": True})
    pax = {"enabled": False}
    supported_transaction_currencies = SupportedTransactionCurrencies(**{"BTC": btc, "PAX": pax})

    assert True is supported_transaction_currencies.get_btc().get_enabled()
    assert False is supported_transaction_currencies.get_pax().get_enabled()


@pytest.mark.unit
def test_modify_btc():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_btc(value)

    assert value == supported_transaction_currencies.get_btc()


@pytest.mark.unit
def test_modify_bch():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_bch(value)

    assert value == supported_transaction_currencies.get_bch()


@pytest.mark.unit
def test_modify_eth():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_eth(value)

    assert value == supported_transaction_currencies.get_eth()


@pytest.mark.unit
def test_modify_usdc():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_usdc(value)

    assert value == supported_transaction_currencies.get_usdc()


@pytest.mark.unit
def test_modify_gusd():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_gusd(value)

    assert value == supported_transaction_currencies.get_gusd()


@pytest.mark.unit
def test_modify_busd():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_busd(value)

    assert value == supported_transaction_currencies.get_busd()


@pytest.mark.unit
def test_modify_pax():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_pax(value)

    assert value == supported_transaction_currencies.get_pax()


@pytest.mark.unit
def test_modify_xrp():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_xrp(value)

    assert value == supported_transaction_currencies.get_xrp()


@pytest.mark.unit
def test_modify_doge():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_doge(value)

    assert value == supported_transaction_currencies.get_doge()


@pytest.mark.unit
def test_modify_ltc():
    supported_transaction_currencies = SupportedTransactionCurrencies()
    value = SupportedTransactionCurrency(**{"enabled": True})
    supported_transaction_currencies.set_ltc(value)

    assert value == supported_transaction_currencies.get_ltc()
