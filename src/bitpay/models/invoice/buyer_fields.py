from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class BuyerFields(BitPayModel):
    buyer_address1: Union[str, None] = None
    buyer_address2: Union[str, None] = None
    buyer_city: Union[str, None] = None
    buyer_country: Union[str, None] = None
    buyer_email: Union[str, None] = None
    buyer_name: Union[str, None] = None
    buyer_notify: bool = False
    buyer_phone: Union[str, None] = None
    buyer_state: Union[str, None] = None
    buyer_zip: Union[str, None] = None
