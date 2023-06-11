import pytest

from bitpay.models.invoice.miner_fees_item import MinerFeesItem


@pytest.mark.unit
def test_constructor():
    amount = 12.34
    satoshis = "123.45"
    total_fee = 43.54
    miner_fees_item = MinerFeesItem(
        **{"fiatAmount": amount, "satoshisPerByte": satoshis, "totalFee": total_fee}
    )

    assert amount == miner_fees_item.get_fiat_amount()
    assert 123.45 == miner_fees_item.get_satoshis_per_byte()
    assert total_fee == miner_fees_item.get_total_fee()


@pytest.mark.unit
def test_modify_fiat_amount():
    miner_fees_item = MinerFeesItem()
    value = 12
    miner_fees_item.set_fiat_amount(value)

    assert value == miner_fees_item.get_fiat_amount()


@pytest.mark.unit
def test_modify_satoshis_per_byte():
    miner_fees_item = MinerFeesItem()
    value = 51
    miner_fees_item.set_satoshis_per_byte(value)

    assert value == miner_fees_item.get_satoshis_per_byte()


@pytest.mark.unit
def test_modify_total_fee():
    miner_fees_item = MinerFeesItem()
    value = 16
    miner_fees_item.set_total_fee(value)

    assert value == miner_fees_item.get_total_fee()
