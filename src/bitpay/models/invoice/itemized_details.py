"""
ItemizedDetails
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class ItemizedDetails(BitPayModel):
    """
    object containing line item details for display
    """

    amount: Union[float, None] = None
    description: Union[str, None] = None
    is_fee: bool = False
