from datetime import datetime
from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class RefundWebhook(BitPayModel):
    amount: Union[float, None] = None
    buyer_pays_refund_fee: Union[bool, None] = None
    currency: Union[str, None] = None
    id: Union[str, None] = None
    immediate: Union[bool, None] = None
    invoice: Union[str, None] = None
    last_refund_notification: Union[datetime, None] = None
    refund_fee: Union[float, None] = None
    request_date: Union[datetime, None] = None
    status: Union[str, None] = None
    support_request: Union[str, None] = None
