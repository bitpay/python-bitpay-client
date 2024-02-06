"""
BillStatus
"""

from enum import Enum


class BillStatus(Enum):
    """
    Bill Status
    """

    DRAFT = "draft"
    SENT = "sent"
    NEW = "new"
    PAID = "paid"
    COMPLETE = "complete"
