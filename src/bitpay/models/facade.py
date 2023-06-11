"""
Facade
"""
from enum import Enum

from bitpay.exceptions.bitpay_exception import BitPayException


class Facade(Enum):
    """
    Facade
    """

    MERCHANT = "merchant"
    PAYOUT = "payout"
    POS = "pos"
