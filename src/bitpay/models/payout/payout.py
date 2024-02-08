"""
Payout
"""

from datetime import datetime
from typing import List, Union, Dict
from pydantic import Field, field_serializer
from .payout_transaction import PayoutTransaction
from ..bitpay_model import BitPayModel


class Payout(BitPayModel):
    """
    Payout
    """

    amount: float = 0.0
    code: Union[int, None] = None
    id: Union[str, None] = None
    token: Union[str, None] = None
    currency: Union[str, None] = None
    effective_date: Union[datetime, None] = None
    reference: Union[str, None] = None
    notification_email: Union[str, None] = None
    notification_url: Union[str, None] = Field(alias="notificationURL", default=None)
    ledger_currency: Union[str, None] = None
    shopper_id: Union[str, None] = None
    recipient_id: Union[str, None] = None
    exchange_rates: Union[Dict[str, Dict[str, float]], None] = None
    email: Union[str, None] = None
    ignore_emails: Union[bool, None] = None
    label: Union[str, None] = None
    status: Union[str, None] = None
    message: Union[str, None] = None
    request_date: Union[datetime, None] = None
    date_executed: Union[datetime, None] = None
    transactions: Union[List[PayoutTransaction], None] = None
    account_id: Union[str, None] = None
    group_id: Union[str, None] = None

    @field_serializer("effective_date", "request_date", "date_executed")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        data = super().to_json()
        if "notificationUrl" in data:
            data["notificationURL"] = data.pop("notificationUrl")

        return data
