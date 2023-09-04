import pytest

from bitpay.models.invoice.miner_fees_item import MinerFeesItem


@pytest.mark.unit
def test_constructor():
    amount = 12.34
    satoshis = "123.45"
    total_fee = 43.54
    miner_fees_item = MinerFeesItem(fiat_amount=amount, satoshis_per_byte=satoshis, total_fee=total_fee)

    assert amount == miner_fees_item.fiat_amount
    assert 123.45 == miner_fees_item.satoshis_per_byte
    assert total_fee == miner_fees_item.total_fee
