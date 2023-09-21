from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class PayoutGroupFailed(BitPayModel):
    err_message: Union[str, None] = None
    payout_id: Union[str, None] = None
    payee: Union[str, None] = None
