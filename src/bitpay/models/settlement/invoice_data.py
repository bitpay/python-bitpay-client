"""
InvoiceData: Object containing relevant information from the paid invoice
"""
from typing import Union
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.settlement.refund_info import RefundInfo


class InvoiceData(BitPayModel):
    """
    invoice data
    """

    order_id: Union[str, None] = None
    date: Union[str, None] = None
    price: Union[float, None] = None
    currency: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    over_paid_amount: Union[float, None] = None
    payout_percentage: Union[dict, None] = None
    buyer_email_address: Union[str, None] = None
    refund_info: Union[RefundInfo, None] = None
