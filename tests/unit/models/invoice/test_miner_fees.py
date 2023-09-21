import pytest

from bitpay.models.invoice.miner_fees import MinerFees
from bitpay.models.invoice.miner_fees_item import MinerFeesItem


@pytest.mark.unit
def test_constructor():
    busd = MinerFeesItem()
    busd.total_fee = 12.34
    gusd = MinerFeesItem()
    doge_as_dict = {"totalFee": 34.56}
    miner_fees = MinerFees(busd=busd, doge=doge_as_dict, gusd=gusd)

    assert busd == miner_fees.busd
    assert gusd == miner_fees.gusd
    assert 34.56 == miner_fees.doge.total_fee
