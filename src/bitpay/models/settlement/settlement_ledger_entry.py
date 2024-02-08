"""
SettlementLedgerEntry: ledger entries in the settlement,
"""

from datetime import datetime
from pydantic import field_serializer
from typing import Union
from .invoice_data import InvoiceData
from ..bitpay_model import BitPayModel


class SettlementLedgerEntry(BitPayModel):
    """
    SettlementLedgerEntry
    """

    code: Union[int, None] = None
    invoice_id: Union[str, None] = None
    amount: Union[float, None] = None
    timestamp: Union[datetime, None] = None
    description: Union[str, None] = None
    invoice_data: Union[InvoiceData, None] = None

    @field_serializer("timestamp")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
