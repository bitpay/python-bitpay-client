"""
RefundInfo: Object containing information about the refund executed for the invoice
"""
from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class RefundInfo(BitPayModel):
    """
    Information about refund
    """

    support_request: Union[str, None] = None
    currency: Union[str, None] = None
    amounts: Union[dict, None] = None
    refund_request_eid: Union[str, None] = None
