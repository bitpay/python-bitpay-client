import pytest

from bitpay.models.wallet.currencies import Currencies
from bitpay.models.wallet.currency_qr import CurrencyQr


@pytest.mark.unit
def test_constructor():
    code = "USD"
    pay_pro = True
    qr = CurrencyQr()
    wallet_connect = True
    currencies = Currencies(code=code, pay_pro=pay_pro, qr=qr, walletConnect=wallet_connect
    )

    assert code == currencies.code
    assert pay_pro == currencies.pay_pro
    assert qr == currencies.qr
    assert wallet_connect == currencies.wallet_connect

    currency_type = "BIP72b"
    currencies = Currencies(qr=CurrencyQr(type=currency_type))

    assert currencies.qr.type == currency_type
