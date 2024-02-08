"""
Item
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class Item(BitPayModel):
    """
    List of line items
    """

    id: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    quantity: Union[int, None] = None
