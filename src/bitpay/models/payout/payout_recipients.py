"""
PayoutRecipients
"""

from typing import List, Union

from .payout_recipient import PayoutRecipient
from ..bitpay_model import BitPayModel


class PayoutRecipients(BitPayModel):
    """
    PayoutRecipients
    """

    guid: Union[str, None] = None
    recipients: Union[List[PayoutRecipient], None] = None
    token: Union[str, None] = None
