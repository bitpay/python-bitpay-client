"""
RefundInfo
"""
from typing import List, Union
from bitpay.models.bitpay_model import BitPayModel


class RefundInfo(BitPayModel):
    """
    Information about refund
    """

    support_request: Union[str, None] = None
    currency: Union[str, None] = None
    amounts: Union[List[dict], None] = None
