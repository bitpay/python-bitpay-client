"""
Rate
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class Rate(BitPayModel):
    """
    Rate
    """

    name: Union[str, None] = None
    code: Union[str, None] = None
    rate: Union[float, None] = None
