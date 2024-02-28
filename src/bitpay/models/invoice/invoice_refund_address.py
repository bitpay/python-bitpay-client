"""
InvoiceRefundAddress
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class InvoiceRefundAddress(BitPayModel):
    type: str
    date: str
    tag: Union[int, None] = None
    email: Union[str, None] = None
