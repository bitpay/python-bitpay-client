from typing import Union
from bitpay.models.bitpay_model import BitPayModel


class WithHoldings(BitPayModel):
    """
    Holdings
    """

    amount: Union[float, None] = None
    code: Union[str, None] = None
    description: Union[str, None] = None
    notes: Union[str, None] = None
    label: Union[str, None] = None
    bank_country: Union[str, None] = None
