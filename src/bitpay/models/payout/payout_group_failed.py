from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class PayoutGroupFailed:
    __err_message: Optional[str]
    __payout_id: Optional[str]
    __payee: Optional[str]

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(key, value, {}, {})
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_err_message(self) -> Optional[str]:
        return self.__err_message

    def set_err_message(self, value: str) -> None:
        self.__err_message = value

    def get_payee(self) -> Optional[str]:
        return self.__payee

    def set_payee(self, value: str) -> None:
        self.__payee = value

    def get_payout_id(self) -> Optional[str]:
        return self.__payout_id

    def set_payout_id(self, value: str) -> None:
        self.__payout_id = value
