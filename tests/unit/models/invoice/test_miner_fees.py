import pytest

from bitpay.models.invoice.miner_fees import MinerFees
from bitpay.models.invoice.miner_fees_item import MinerFeesItem


@pytest.mark.unit
def test_constructor():
    busd = MinerFeesItem()
    busd.set_total_fee(12.34)
    gusd = MinerFeesItem()
    doge_as_dict = {"totalFee": 34.56}
    miner_fees = MinerFees(**{"BUSD": busd, "DOGE": doge_as_dict, "gusd": gusd})

    assert busd == miner_fees.get_busd()
    assert gusd == miner_fees.get_gusd()
    assert 34.56 == miner_fees.get_doge().get_total_fee()


@pytest.mark.unit
def test_modify_bch():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_bch(value)

    assert value == miner_fees.get_bch()


@pytest.mark.unit
def test_modify_btc():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_btc(value)

    assert value == miner_fees.get_btc()


@pytest.mark.unit
def test_modify_busd():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_busd(value)

    assert value == miner_fees.get_busd()


@pytest.mark.unit
def test_modify_doge():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_doge(value)

    assert value == miner_fees.get_doge()


@pytest.mark.unit
def test_modify_eth():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_eth(value)

    assert value == miner_fees.get_eth()


@pytest.mark.unit
def test_modify_gusd():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_gusd(value)

    assert value == miner_fees.get_gusd()


@pytest.mark.unit
def test_modify_ltc():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_ltc(value)

    assert value == miner_fees.get_ltc()


@pytest.mark.unit
def test_modify_pax():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_pax(value)

    assert value == miner_fees.get_pax()


@pytest.mark.unit
def test_modify_usdc():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_usdc(value)

    assert value == miner_fees.get_usdc()


@pytest.mark.unit
def test_modify_xrp():
    miner_fees = MinerFees()
    value = MinerFeesItem()
    value.set_total_fee(12.34)
    miner_fees.set_xrp(value)

    assert value == miner_fees.get_xrp()
