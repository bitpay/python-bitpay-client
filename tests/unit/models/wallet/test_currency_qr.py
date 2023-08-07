import pytest

from bitpay.models.wallet.currency_qr import CurrencyQr


@pytest.mark.unit
def test_constructor():
    type = "someType"
    collapsed = True
    qr = CurrencyQr(**{"type": type, "collapsed": collapsed})

    assert type == qr.get_type()
    assert collapsed == qr.get_collapsed()


@pytest.mark.unit
def test_modify_type():
    qr = CurrencyQr()
    value = "someValue"
    qr.set_type(value)

    assert value == qr.get_type()


@pytest.mark.unit
def test_modify_collapsed():
    qr = CurrencyQr()
    value = True
    qr.set_collapsed(value)

    assert value == qr.get_collapsed()
