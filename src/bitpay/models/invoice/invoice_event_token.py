from typing import List, Union
from bitpay.models.bitpay_model import BitPayModel


class InvoiceEventToken(BitPayModel):
    token: Union[str, None] = None
    events: List[str] = []
    actions: List[str] = []
