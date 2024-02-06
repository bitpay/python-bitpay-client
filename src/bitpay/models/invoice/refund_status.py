"""
RefundStatus
"""

from enum import Enum


class RefundStatus(Enum):
    """
    Refund Status
    """

    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"
    PREVIEW = "preview"
    CREATED = "created"
    CANCELLED = "cancelled"
