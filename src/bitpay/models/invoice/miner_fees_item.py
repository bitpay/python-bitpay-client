"""
MinerFeesItem
"""
from typing import Union
from bitpay.models.bitpay_model import BitPayModel
from bitpay.utils.model_util import ModelUtil


class MinerFeesItem(BitPayModel):
    """
    The total amount of fees that the purchaser will pay to cover BitPay's
     UTXO sweep cost for an invoice. The key is the currency and the value is
      an amount in satoshis. This is referenced as "Network Cost" on an invoice,
    see this support article for more information
    """

    satoshis_per_byte: Union[float, None] = None
    total_fee: Union[float, None] = None
    fiat_amount: Union[float, None] = None
