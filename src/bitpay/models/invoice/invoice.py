"""
Invoice
"""
from typing import List, Union
from pydantic import Field
from .buyer import Buyer
from .buyer_provided_info import BuyerProvidedInfo
from .miner_fees import MinerFees
from .refund_info import RefundInfo
from .shopper import Shopper
from .supported_transaction_currencies import SupportedTransactionCurrencies
from .transaction import Transaction
from .itemized_details import ItemizedDetails
from .universal_codes import UniversalCodes
from ..bitpay_model import BitPayModel


class Invoice(BitPayModel):
    """
    Invoices are time-sensitive payment requests addressed to specific buyers.
    An invoice has a fixed price,typically denominated in fiat currency.
    It also has an equivalent price in the supported cryptocurrencies,
    calculated by BitPay, at a locked exchange rate with an expiration
    time of 15 minutes.
    """

    currency: Union[str, None] = None
    guid: Union[str, None] = None
    token: Union[str, None] = None
    price: Union[float, None] = None
    pos_data: Union[str, None] = None
    notification_url: Union[str, None] = Field(alias="notificationURL", default=None)
    transaction_speed: Union[str, None] = None
    full_notifications: bool = False
    notification_email: Union[str, None] = None
    redirect_url: Union[str, None] = Field(alias="redirectURL", default=None)
    order_id: Union[str, None] = None
    item_desc: Union[str, None] = None
    item_code: Union[str, None] = None
    physical: Union[bool, None] = False
    payment_currencies: Union[List[str], None] = None
    payment_subtotals: Union[dict, None] = None
    payment_totals: Union[dict, None] = None
    payment_display_totals: Union[dict, None] = None
    payment_display_subtotals: Union[dict, None] = None
    payment_codes: Union[dict, None] = None
    acceptance_window: Union[int, None] = None
    buyer: Union[Buyer, None] = None
    refund_addresses: Union[List[str], None] = None
    close_url: Union[str, None] = Field(alias="closeURL", default=None)
    auto_redirect: Union[bool, None] = False
    json_paypro_required: bool = False
    id: Union[str, None] = None
    url: Union[str, None] = None
    status: Union[str, None] = None
    low_fee_detected: Union[bool, None] = False
    invoice_time: Union[int, None] = None
    expiration_time: Union[int, None] = None
    current_time: Union[int, None] = None
    transactions: Union[List[Transaction], None] = None
    exception_status: Union[str, bool, None] = None
    target_confirmations: Union[int, None] = None
    refund_address_request_pending: bool = False
    buyer_provided_email: Union[str, None] = None
    buyer_provided_info: Union[BuyerProvidedInfo, None] = None
    buyer_sms: Union[str, None] = None
    supported_transaction_currencies: Union[SupportedTransactionCurrencies, None] = None
    miner_fees: Union[MinerFees, None] = None
    non_pay_pro_payment_received: Union[bool, None] = False
    shopper: Union[Shopper, None] = None
    bill_id: Union[str, None] = None
    refund_info: Union[List[RefundInfo], None] = None
    extended_notifications: Union[bool, None] = False
    invoice_buyer_provided_info: Union[BuyerProvidedInfo, None] = None
    transaction_currency: Union[str, None] = None
    underpaid_amount: Union[float, None] = None
    overpaid_amount: Union[float, None] = None
    amount_paid: Union[float, None] = None
    display_amount_paid: Union[str, None] = None
    exchange_rates: Union[dict, None] = None
    payment_string: Union[str, None] = None
    verification_link: Union[str, None] = None
    buyer_email: Union[str, None] = None
    merchant_name: Union[str, None] = None
    forced_buyer_selected_wallet: Union[str, None] = None
    forced_buyer_selected_transaction_currency: Union[str, None] = None
    itemized_details: Union[List[ItemizedDetails], None] = None
    universal_codes: Union[UniversalCodes, None] = None
    is_cancelled: Union[bool, None] = False
    bitpay_id_required: Union[bool, None] = False
