"""
RefundInfo: Object containing information about the refund executed for the invoice
"""

from typing import Union, Dict
from bitpay.models.bitpay_model import BitPayModel


class RefundInfo(BitPayModel):
    """
    Information about refund
    """

    support_request: Union[str, None] = None
    currency: Union[str, None] = None
    amounts: Union[Dict[str, float], None] = None
