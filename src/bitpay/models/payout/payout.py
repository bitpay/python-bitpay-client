"""
Payout
"""
from typing import List, Union
from pydantic import Field
from .payout_transaction import PayoutTransaction
from ..bitpay_model import BitPayModel


class Payout(BitPayModel):
    """
    Payout
    """

    amount: float = 0.0
    id: Union[str, None] = None
    token: Union[str, None] = None
    currency: Union[str, None] = None
    effective_date: Union[str, None] = None
    reference: Union[str, None] = None
    notification_email: Union[str, None] = None
    notification_url: Union[str, None] = Field(alias="notificationURL", default=None)
    redirect_url: Union[str, None] = None
    ledger_currency: Union[str, None] = None
    shopper_id: Union[str, None] = None
    recipient_id: Union[str, None] = None
    exchange_rates: Union[dict, None] = None
    account: Union[str, None] = None
    email: Union[str, None] = None
    label: Union[str, None] = None
    support_phone: Union[str, None] = None
    status: Union[str, None] = None
    message: Union[str, None] = None
    request_date: Union[str, None] = None
    date_executed: Union[str, None] = None
    transactions: Union[List[PayoutTransaction], None] = None
    account_id: Union[str, None] = None
    group_id: Union[str, None] = None

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        data = super().to_json()
        if "notificationUrl" in data:
            data["notificationURL"] = data.pop("notificationUrl")

        return data
