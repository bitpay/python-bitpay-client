from datetime import datetime
from pydantic import field_serializer
from typing import Union, Dict, List

from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.payout.payout_transaction import PayoutTransaction


class PayoutWebhook(BitPayModel):
    id: Union[str, None] = None
    recipient_id: Union[str, None] = None
    shopper_id: Union[str, None] = None
    price: Union[float, None] = None
    currency: Union[str, None] = None
    ledger_currency: Union[str, None] = None
    exchange_rates: Union[Dict[str, Dict[str, float]], None] = None
    email: Union[str, None] = None
    reference: Union[str, None] = None
    label: Union[str, None] = None
    notification_url: Union[str, None] = None
    notification_email: Union[str, None] = None
    effective_date: Union[datetime, None] = None
    request_date: Union[datetime, None] = None
    status: Union[str, None] = None
    transactions: Union[List[PayoutTransaction], None] = None
    account_id: Union[str, None] = None
    date_executed: Union[datetime, None] = None
    group_id: Union[str, None] = None

    @field_serializer("effective_date", "request_date")
    def serialize_datetime(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
