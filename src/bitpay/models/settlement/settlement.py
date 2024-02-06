"""
Settlement: Settlements are transfers of payment profits from BitPay to bank
accounts and cryptocurrency wallets owned by merchants, partners, etc. This
endpoint exposes reports detailing these settlements.
"""

from datetime import datetime
from pydantic import field_serializer
from typing import List, Union
from .payout_info import PayoutInfo
from .settlement_ledger_entry import SettlementLedgerEntry
from .with_holdings import WithHoldings
from ..bitpay_model import BitPayModel


class Settlement(BitPayModel):
    """
    Settlement
    """

    id: Union[str, None] = None
    account_id: Union[str, None] = None
    currency: Union[str, None] = None
    payout_info: Union[PayoutInfo, None] = None
    status: Union[str, None] = None
    date_created: Union[datetime, None] = None
    date_executed: Union[datetime, None] = None
    date_completed: Union[datetime, None] = None
    opening_date: Union[datetime, None] = None
    closing_date: Union[datetime, None] = None
    opening_balance: Union[float, None] = None
    ledger_entries_sum: Union[float, None] = None
    withholdings: Union[List[WithHoldings], None] = None
    withholdings_sum: Union[float, None] = None
    total_amount: Union[float, None] = None
    ledger_entries: Union[List[SettlementLedgerEntry], None] = None
    token: Union[str, None] = None

    @field_serializer("date_created", "date_executed", "date_completed", "closing_date")
    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return super().serialize_datetime_to_iso8601(dt)
