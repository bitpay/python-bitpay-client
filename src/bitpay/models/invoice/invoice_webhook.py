from typing import Union, Dict

from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.invoice.buyer_fields import BuyerFields


class InvoiceWebhook(BitPayModel):
    amount_paid: Union[float, None] = None
    buyer_fields: Union[BuyerFields, None] = None
    currency: Union[str, None] = None
    currency_time: Union[str, None] = None
    exception_status: Union[str, None] = None
    exchange_rates: Union[Dict[str, Dict[str, float]], None] = None
    id: Union[str, None] = None
    invoice_time: Union[str, None] = None
    order_id: Union[str, None] = None
    payment_subtotals: Union[Dict[str, int], None] = None
    payment_totals: Union[Dict[str, int], None] = None
    pos_data: Union[str, None] = None
    price: Union[float, None] = None
    status: Union[str, None] = None
    transaction_currency: Union[str, None] = None
    url: Union[str, None] = None
    in_invoice_id: Union[str, None] = None
    in_payment_request: Union[str, None] = None
