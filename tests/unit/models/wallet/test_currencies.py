import pytest

from bitpay.models.wallet.currencies import Currencies
from bitpay.models.wallet.currency_qr import CurrencyQr


@pytest.mark.unit
def test_constructor():
    code = "USD"
    pay_pro = True
    qr = CurrencyQr()
    wallet_connect = True
    currencies = Currencies(**{"code": code, "payPro": pay_pro, "qr": qr, "walletConnect": wallet_connect})

    assert code == currencies.get_code()
    assert pay_pro == currencies.get_pay_pro()
    assert qr == currencies.get_qr()
    assert wallet_connect == currencies.get_wallet_connect()

    currency_type = "BIP72b"
    currencies = Currencies(**{"qr": {"type": currency_type}})

    assert currencies.get_qr().get_type() == currency_type


@pytest.mark.unit
def test_modify_code():
    currencies = Currencies()
    value = "someValue"
    currencies.set_code(value)

    assert currencies.get_code() == value


@pytest.mark.unit
def test_modify_p2p():
    currencies = Currencies()
    value = True
    currencies.set_p2p(value)

    assert currencies.get_p2p() == value


@pytest.mark.unit
def test_modify_dapp_browser():
    currencies = Currencies()
    value = True
    currencies.set_dapp_browser(value)

    assert currencies.get_dapp_browser() == value


@pytest.mark.unit
def test_modify_pay_pro():
    currencies = Currencies()
    value = True
    currencies.set_pay_pro(value)

    assert currencies.get_pay_pro() == value


@pytest.mark.unit
def test_modify_qr():
    currencies = Currencies()
    value = CurrencyQr()
    currencies.set_qr(value)

    assert currencies.get_qr() == value


@pytest.mark.unit
def test_modify_image():
    currencies = Currencies()
    value = "someValue"
    currencies.set_image(value)

    assert currencies.get_image() == value


@pytest.mark.unit
def test_modify_withdrawal_fee():
    currencies = Currencies()
    value = "someValue"
    currencies.set_withdrawal_fee(value)

    assert currencies.get_withdrawal_fee() == value


@pytest.mark.unit
def test_modify_wallet_connect():
    currencies = Currencies()
    value = True
    currencies.set_wallet_connect(value)

    assert currencies.get_wallet_connect() == value
