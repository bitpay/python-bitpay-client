"""
Currency Qr
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class CurrencyQr(BitPayModel):
    """
    Currency Qr
    """

    type: Union[str, None] = None
    collapsed: Union[bool, None] = False
