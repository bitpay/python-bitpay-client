"""
BuyerProvidedInfo: Information collected from the buyer during the process of paying
an invoice. Initially this object is empty.
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class BuyerProvidedInfo(BitPayModel):
    """
    Information collected from the buyer during the process of paying an invoice.
     Initially this object is empty.
    """

    name: Union[str, None] = None
    phone_number: Union[str, None] = None
    selected_wallet: Union[str, None] = None
    email_address: Union[str, None] = None
    selected_transaction_currency: Union[str, None] = None
    sms: Union[str, None] = None
    sms_verified: bool = False
