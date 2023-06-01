"""
PayoutRecipient
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class PayoutRecipient:
    """
    PayoutRecipient
    """

    __email = None
    __label = None
    __notification_url = None
    __data = None

    __status = None
    __id = None
    __shopper_id = None
    __token = None
    __guid = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                if key == "notificationURL":
                    self.set_notification_url(str(value))
                else:
                    getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(
                        value
                    )
            except AttributeError:
                pass

    def get_email(self) -> Optional[str]:
        """
        Get method for email
        :return: email
        """
        return self.__email

    def set_email(self, email: Optional[str]) -> None:
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_data(self) -> Optional[str]:
        """
        Get method for data
        :return: data
        """
        return self.__data

    def set_data(self, data: Optional[str]) -> None:
        """
        Set method for to data
        :param data: data
        """
        self.__data = data

    def get_label(self) -> Optional[str]:
        """
        Get method for to label
        :return: label
        """
        return self.__label

    def set_label(self, label: Optional[str]) -> None:
        """
        Set method for to label
        :param label: label
        """
        self.__label = label

    def get_notification_url(self) -> Optional[str]:
        """
        Get method for to notification_url
        :return: notification_url
        """
        return self.__notification_url

    def set_notification_url(self, notification_url: Optional[str]) -> None:
        """
        Set method for to notification_url
        :param notification_url: notification_url
        """
        self.__notification_url = notification_url

    def get_status(self) -> Optional[str]:
        """
        Get method for status
        :return: status
        """
        return self.__status

    def set_status(self, status: Optional[str]) -> None:
        """
        Set method for status
        :param status: status
        """
        self.__status = status

    def get_id(self) -> Optional[str]:
        """
        Get method for id
        :return: id
        """
        return self.__id

    def set_id(self, id: Optional[str]) -> None:
        """
        Set method for id
        :param id: id
        """
        self.__id = id

    def get_shopper_id(self) -> Optional[str]:
        """
        Get method for to shopper_id
        :return: shopper_id
        """
        return self.__shopper_id

    def set_shopper_id(self, shopper_id: Optional[str]) -> None:
        """
        Set method for to shopper_id
        :param shopper_id: shopper_id
        """
        self.__shopper_id = shopper_id

    def get_token(self) -> Optional[str]:
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def get_guid(self) -> Optional[str]:
        """
        Gets guid.
        :return: guid
        """
        return self.__guid

    def set_guid(self, value: Optional[str]) -> None:
        """
        Sets guid.
        :param value: guid
        """
        self.__guid = value

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        data = ModelUtil.to_json(self)
        if "notificationUrl" in data:
            data["notificationURL"] = data.pop("notificationUrl")

        return data
