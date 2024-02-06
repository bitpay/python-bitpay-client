"""
LedgerEntry
"""

from datetime import datetime
from typing import Union
from pydantic import field_validator, field_serializer
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.ledger.buyer import Buyer


class LedgerEntry(BitPayModel):
    """
    Ledger entry
    """

    type: Union[str, None] = None
    amount: Union[int, None] = None
    code: Union[int, None] = None
    description: Union[str, None] = None
    timestamp: Union[datetime, None] = None
    currency: Union[str, None] = None
    tx_type: Union[str, None] = None
    scale: Union[int, None] = None
    id: Union[str, None] = None
    support_request: Union[str, None] = None
    invoice_id: Union[str, None] = None

    # Buyer
    buyer_fields: Union[Buyer, None] = None

    invoice_amount: Union[float, None] = None
    invoice_currency: Union[str, None] = None
    transaction_currency: Union[str, None] = None

    @field_validator("amount")
    def convert_to_str(cls, value: Union[int, float, None]) -> Union[float, None]:
        if value is None:
            return None
        return float(value)

    @field_serializer("timestamp")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
