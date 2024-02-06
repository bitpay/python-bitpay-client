"""
SupportedTransactionCurrency
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel


class SupportedTransactionCurrency(BitPayModel):
    """
    currency selected for payment is enabled
    """

    enabled: Union[bool, None] = None
    reason: Union[str, None] = None
