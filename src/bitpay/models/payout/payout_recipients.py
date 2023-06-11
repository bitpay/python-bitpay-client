"""
PayoutRecipients
"""
from typing import Optional, List

from .payout_recipient import PayoutRecipient
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class PayoutRecipients:
    """
    PayoutRecipients
    """

    __guid = None
    __recipients: Optional[List[PayoutRecipient]] = None
    __token = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {}, {"recipients": PayoutRecipient}
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_guid(self) -> Optional[str]:
        """
        Get method for guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid: Optional[str]) -> None:
        """
        Set method for guid
        :param guid: guid
        """
        self.__guid = guid

    def get_token(self) -> Optional[str]:
        """
        Get method for token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for token
        :param token: token
        """
        self.__token = token

    def get_recipients(self) -> Optional[List[PayoutRecipient]]:
        """
        Get method for recipients
        :return: recipients
        """
        return self.__recipients

    def set_recipients(self, recipients: Optional[List[PayoutRecipient]]) -> None:
        """
        Set method for recipients
        :param recipients: recipients
        """
        self.__recipients = recipients

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
