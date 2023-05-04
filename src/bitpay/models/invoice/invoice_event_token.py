from typing import List, Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case


class InvoiceEventToken:
    __token = None
    __events = List[str]
    __actions = List[str]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
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

    def set_actions(self, actions: List[str]):
        self.__actions = actions
