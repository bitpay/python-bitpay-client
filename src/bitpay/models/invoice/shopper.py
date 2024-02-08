"""
Shopper
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class Shopper(BitPayModel):
    """
    shopper
    """

    user: Union[str, None] = None
