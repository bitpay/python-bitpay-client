"""
PayoutTransaction
"""

from datetime import datetime
from pydantic import field_serializer
from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class PayoutTransaction(BitPayModel):
    """
    PayoutTransaction
    """

    txid: Union[str, None] = None
    amount: Union[float, None] = None
    date: Union[datetime, None] = None
    confirmations: Union[int, None] = None

    @field_serializer("date")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
