from datetime import datetime
from typing import Union

from pydantic import field_serializer

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
    reference: Union[str, None] = None
    guid: Union[str, None] = None
    refund_address: Union[str, None] = None
    type: Union[str, None] = None
    txid: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    transaction_amount: Union[float, None] = None
    transaction_refund_fee: Union[float, None] = None

    @field_serializer("request_date", "last_refund_notification")
    def serialize_datetime(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
