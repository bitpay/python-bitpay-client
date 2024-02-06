"""
Refund
"""

from datetime import datetime
from typing import Union

from pydantic import Field, field_serializer

from bitpay.models.bitpay_model import BitPayModel


class Refund(BitPayModel):
    """
    Refund an invoice
    """

    id: Union[str, None] = None
    guid: Union[str, None] = None
    amount: float = 0.0
    currency: Union[str, None] = None
    request_date: Union[datetime, None] = None
    status: Union[str, None] = None

    preview: bool = False
    immediate: bool = False
    reference: Union[str, None] = None
    buyer_pays_refund_fee: bool = False
    refund_fee: Union[float, None] = None
    last_refund_notification: Union[datetime, None] = None
    invoice: Union[str, None] = None
    notification_url: Union[str, None] = Field(alias="notificationURL", default=None)
    refund_address: Union[str, None] = None
    support_request: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    transaction_amount: Union[float, None] = None
    transaction_refund_fee: Union[float, None] = None
    txid: Union[str, None] = None
    type: Union[str, None] = None

    @field_serializer("request_date", "last_refund_notification")
    def serialize_datetime(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
