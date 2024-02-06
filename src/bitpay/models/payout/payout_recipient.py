"""
PayoutRecipient
"""

from typing import Union

from pydantic import Field

from bitpay.models.bitpay_model import BitPayModel


class PayoutRecipient(BitPayModel):
    """
    PayoutRecipient
    """

    email: Union[str, None] = None
    label: Union[str, None] = None
    notification_url: str = Field(alias="notificationURL", default=None)
    status: Union[str, None] = None
    id: Union[str, None] = None
    shopper_id: Union[str, None] = None
    token: Union[str, None] = None
    guid: Union[str, None] = None

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        data = super().to_json()
        if "notificationUrl" in data:
            data["notificationURL"] = data.pop("notificationUrl")

        return data
