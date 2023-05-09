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

    @staticmethod
    def from_str(facade: str):
        try:
            enum = Facade[facade.upper()]
        except Exception:
            raise BitPayException("Invalid facade")
        return enum
