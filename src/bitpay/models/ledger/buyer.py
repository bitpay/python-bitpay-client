"""
Buyer
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class Buyer(BitPayModel):
    """
    Allows merchant to pass buyer related information in the invoice object
    """

    name: Union[str, None] = None
    address1: Union[str, None] = None
    address2: Union[str, None] = None
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[str, None] = None
    country: Union[str, None] = None
    email: Union[str, None] = None
    phone: Union[str, None] = None
    notify: bool = False
