import pytest

from bitpay.models.wallet.currencies import Currencies
from bitpay.models.wallet.wallet import Wallet


@pytest.mark.unit
def test_constructor():
    currencies = [Currencies()]
    pay_pro = True
    key = "someKey"

    wallet = Wallet(**{"currencies": currencies, "payPro": pay_pro, "key": key})
    assert currencies == wallet.get_currencies()
    assert pay_pro == wallet.get_pay_pro()
    assert key == wallet.get_key()

    wallet = Wallet(**{"currencies": [{"code": "USD"}, {"code": "BCH"}]})
    assert len(wallet.get_currencies()) == 2
    assert wallet.get_currencies()[1].get_code() == "BCH"


@pytest.mark.unit
def test_modify_key():
    wallet = Wallet()
    value = "someValue"
    wallet.set_key(value)

    assert wallet.get_key() == value


@pytest.mark.unit
def test_modify_display_name():
    wallet = Wallet()
    value = "someValue"
    wallet.set_display_name(value)

    assert wallet.get_display_name() == value


@pytest.mark.unit
def test_modify_avatar():
    wallet = Wallet()
    value = "someValue"
    wallet.set_avatar(value)

    assert wallet.get_avatar() == value


@pytest.mark.unit
def test_modify_pay_pro():
    wallet = Wallet()
    value = True
    wallet.set_pay_pro(value)

    assert wallet.get_pay_pro() == value


@pytest.mark.unit
def test_modify_currencies():
    wallet = Wallet()
    value = [Currencies()]
    wallet.set_currencies(value)

    assert wallet.get_currencies() == value


@pytest.mark.unit
def test_modify_image():
    wallet = Wallet()
    value = "someValue"
    wallet.set_image(value)

    assert wallet.get_image() == value
