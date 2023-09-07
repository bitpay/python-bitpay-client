"""
Bill
"""
from typing import List, Union
from .item import Item
from ..bitpay_model import BitPayModel


class Bill(BitPayModel):
    """
    Bills are payment requests addressed to specific buyers.
    Bill line items have fixed prices, typically denominated
    in fiat currency.
    """

    currency: Union[str, None] = None
    token: Union[str, None] = None
    email: Union[str, None] = None
    items: Union[List[Item], None] = None
    number: Union[str, None] = None
    name: Union[str, None] = None
    address1: Union[str, None] = None
    address2: Union[str, None] = None
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[str, None] = None
    country: Union[str, None] = None
    cc: Union[List[str], None] = None
    phone: Union[str, None] = None
    due_date: Union[str, None] = None
    pass_processing_fee: bool = False
    status: Union[str, None] = None
    url: Union[str, None] = None
    created_date: Union[str, None] = None
    id: Union[str, None] = None
    merchant: Union[str, None] = None
