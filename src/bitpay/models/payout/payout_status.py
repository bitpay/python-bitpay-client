"""
PayoutStatus
"""

from enum import Enum


class PayoutStatus(Enum):
    NEW = "new"
    FUNDED = "funded"
    PROCESSING = "processing"
    COMPLETE = "complete"
    FAILED = "failed"
    CANCELLED = "cancelled"
    PAID = "paid"
    UNPAID = "unpaid"
