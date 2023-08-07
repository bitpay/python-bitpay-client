from typing import List, Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class InvoiceEventToken:
    __token = None
    __events: List[str] = []
    __actions: List[str] = []

    def __init__(self, **kwargs: dict):
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key, value, {}, {"events": "str", "actions": "str"}
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_token(self) -> Optional[str]:
        return self.__token

    def set_token(self, token: str) -> None:
        self.__token = token

    def get_events(self) -> List[str]:
        return self.__events

    def set_events(self, events: List[str]) -> None:
        self.__events = events

    def get_actions(self) -> List[str]:
        return self.__actions

    def set_actions(self, actions: List[str]) -> None:
        self.__actions = actions

    def to_json(self) -> dict:
        return ModelUtil.to_json(self)
