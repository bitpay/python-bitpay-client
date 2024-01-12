from datetime import datetime
from typing import Union, Dict
from bitpay.models.bitpay_model import BitPayModel


class Transaction(BitPayModel):
    amount: Union[float, None] = None
    confirmations: Union[int, None] = None
    time: Union[datetime, None] = None
    received_time: Union[datetime, None] = None
    txid: Union[str, None] = None
    ex_rates: Union[Dict[str, float], None] = None
    output_index: Union[int, None] = None
