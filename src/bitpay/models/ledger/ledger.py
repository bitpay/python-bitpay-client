"""
Ledger
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class Ledger(BitPayModel):
    """
    Ledgers are records of money movement.
    """

    currency: Union[str, None] = None
    balance: Union[float, None] = None
