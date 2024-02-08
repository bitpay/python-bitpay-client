"""
InvoiceStatus
"""

from enum import Enum


class InvoiceStatus(Enum):
    """
    Invoice Status
    """

    NEW = "new"
    PAID = "paid"
    CONFIRMED = "confirmed"
    COMPLETE = "complete"
    EXPIRED = "expired"
    INVALID = "invalid"
    DECLINED = "declined"
