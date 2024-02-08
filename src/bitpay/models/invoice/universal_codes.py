"""
UniversalCodes
"""

from typing import Union

from bitpay.models.bitpay_model import BitPayModel
from bitpay.utils.model_util import ModelUtil


class UniversalCodes(BitPayModel):
    """
    object containing wallet-specific URLs for payment protocol
    """

    payment_string: Union[str, None] = None
    verification_link: Union[str, None] = None
