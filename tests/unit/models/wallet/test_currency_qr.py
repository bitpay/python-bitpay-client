import pytest

from bitpay.models.wallet.currency_qr import CurrencyQr


@pytest.mark.unit
def test_constructor():
    type = "someType"
    collapsed = True
    qr = CurrencyQr(type=type, collapsed=collapsed)

    assert type == qr.type
    assert collapsed == qr.collapsed
