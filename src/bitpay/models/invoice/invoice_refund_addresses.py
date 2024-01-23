from datetime import datetime
from pydantic import field_serializer
from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class InvoiceRefundAddresses(BitPayModel):
    date: Union[datetime, None]
    email: Union[str, None]
    tag: Union[int, None] = None
    type: Union[str, None] = None

    @field_serializer("date")
    def serialize_datetime(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
