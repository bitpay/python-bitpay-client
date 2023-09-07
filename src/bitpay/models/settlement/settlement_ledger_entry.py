"""
SettlementLedgerEntry: ledger entries in the settlement,
"""
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
    timestamp: Union[str, None] = None
    description: Union[str, None] = None
    reference: Union[str, None] = None
    invoice_data: Union[InvoiceData, None] = None
