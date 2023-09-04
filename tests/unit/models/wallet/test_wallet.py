import pytest

from bitpay.models.wallet.currencies import Currencies
from bitpay.models.wallet.wallet import Wallet


@pytest.mark.unit
def test_constructor():
    currencies = [Currencies()]
    pay_pro = True
    key = "someKey"

    wallet = Wallet(currencies=currencies, pay_pro=pay_pro, key=key)
    assert currencies == wallet.currencies
    assert pay_pro == wallet.pay_pro
    assert key == wallet.key

    wallet = Wallet(currencies=[Currencies(code="USD"), Currencies(code="BCH")])
    assert len(wallet.currencies) == 2
    assert wallet.currencies[1].code == "BCH"
