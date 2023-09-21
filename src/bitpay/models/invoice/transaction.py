from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class Transaction(BitPayModel):
    amount: Union[float, None] = None
    confirmations: Union[int, None] = None
    time: Union[str, None] = None
    received_time: Union[str, None] = None
    txid: Union[str, None] = None
    ex_rates: Union[dict, None] = None
    output_index: Union[int, None] = None
