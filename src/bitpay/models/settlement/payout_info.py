"""
PayoutInfo: Object containing the settlement info provided by the Merchant
in his BitPay account settings
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class PayoutInfo(BitPayModel):
    """
    PayoutInfo
    """

    name: Union[str, None] = None
    account: Union[str, None] = None
    routing: Union[str, None] = None
    merchant_ein: Union[str, None] = None
    label: Union[str, None] = None
    bank_country: Union[str, None] = None
    bank: Union[str, None] = None
    swift: Union[str, None] = None
    address: Union[str, None] = None
    city: Union[str, None] = None
    postal: Union[str, None] = None
    sort: Union[str, None] = None
    wire: bool = False
    bank_name: Union[str, None] = None
    bank_address: Union[str, None] = None
    bank_address2: Union[str, None] = None
    iban: Union[str, None] = None
    additional_information: Union[str, None] = None
    account_holder_name: Union[str, None] = None
    account_holder_address: Union[str, None] = None
    account_holder_address2: Union[str, None] = None
    account_holder_postal_code: Union[str, None] = None
    account_holder_city: Union[str, None] = None
    account_holder_country: Union[str, None] = None
