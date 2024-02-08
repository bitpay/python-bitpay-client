"""
RecipientStatus
"""

from enum import Enum


class RecipientStatus(Enum):
    """
    Recipient Status
    """

    INVITED = "invited"
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    ACTIVE = "active"
    PAUSED = "paused"
    REMOVED = "removed"
