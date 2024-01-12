"""
PayoutTransaction
"""
from datetime import datetime
from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class PayoutTransaction(BitPayModel):
    """
    PayoutTransaction
    """

    txid: Union[str, None] = None
    amount: Union[float, None] = None
    date: Union[datetime, None] = None
    confirmations: Union[str, None] = None
