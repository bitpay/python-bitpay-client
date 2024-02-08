"""
MinerFees
"""

from pydantic import Field

from .miner_fees_item import MinerFeesItem
from bitpay.utils.model_util import ModelUtil
from ..bitpay_model import BitPayModel


class MinerFees(BitPayModel):
    """
    The total amount of fees that the purchaser will pay to cover BitPay's
     UTXO sweep cost for an invoice. The key is the currency and the value
     is an amount in satoshis. This is referenced as "Network Cost" on an
     invoice,see this support article for more information
    """

    btc: MinerFeesItem = Field(alias="BTC", default=MinerFeesItem())
    bch: MinerFeesItem = Field(alias="BCH", default=MinerFeesItem())
    eth: MinerFeesItem = Field(alias="ETH", default=MinerFeesItem())
    usdc: MinerFeesItem = Field(alias="USDC", default=MinerFeesItem())
    gusd: MinerFeesItem = Field(alias="GUSD", default=MinerFeesItem())
    pax: MinerFeesItem = Field(alias="PAX", default=MinerFeesItem())
    doge: MinerFeesItem = Field(alias="DOGE", default=MinerFeesItem())
    ltc: MinerFeesItem = Field(alias="LTC", default=MinerFeesItem())
    busd: MinerFeesItem = Field(alias="BUSD", default=MinerFeesItem())
    xrp: MinerFeesItem = Field(alias="XRP", default=MinerFeesItem())
    dai: MinerFeesItem = Field(alias="DAI", default=MinerFeesItem())
    wbtc: MinerFeesItem = Field(alias="WBTC", default=MinerFeesItem())
    matic: MinerFeesItem = Field(alias="MATIC", default=MinerFeesItem())
    usdc_m: MinerFeesItem = Field(alias="USDC_m", default=MinerFeesItem())
