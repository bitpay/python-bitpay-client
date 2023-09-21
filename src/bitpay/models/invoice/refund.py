"""
Refund
"""
from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class Refund(BitPayModel):
    """
    Refund an invoice
    """

    id: Union[str, None] = None
    guid: Union[str, None] = None
    amount: float = 0.0
    currency: Union[str, None] = None
    token: Union[str, None] = None
    request_date: Union[str, None] = None
    status: Union[str, None] = None

    preview: bool = False
    immediate: bool = False
    reference: Union[str, None] = None
    buyer_pays_refund_fee: bool = False
    refund_fee: Union[float, None] = None
    last_refund_notification: Union[str, None] = None
    invoice: Union[str, None] = None
    notification_url: Union[str, None] = None
    refund_address: Union[str, None] = None
    support_request: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    transaction_amount: Union[float, None] = None
    transaction_refund_fee: Union[float, None] = None
