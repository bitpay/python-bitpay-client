"""
InvoiceData: Object containing relevant information from the paid invoice
"""

from datetime import datetime
from pydantic import field_serializer
from typing import Union, Dict
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.settlement.refund_info import RefundInfo


class InvoiceData(BitPayModel):
    """
    invoice data
    """

    order_id: Union[str, None] = None
    date: Union[datetime, None] = None
    price: Union[float, None] = None
    currency: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    overpaid_amount: Union[float, None] = None
    payout_percentage: Union[Dict[str, int], None] = None
    refund_info: Union[RefundInfo, None] = None

    @field_serializer("date")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
