from typing import Optional, List

from bitpay.utils import key_utils
from bitpay.utils.model_util import ModelUtil


class Transaction:
    __amount = None
    __confirmations = None
    __time = None
    __received_time = None
    __txid = None
    __ex_rates = None
    __output_index = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {"amount": "float", "confirmations": "int", "outputIndex": "int"},
                    {"exRates": "dict"},
                )
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_amount(self) -> Optional[float]:
        return self.__amount

    def get_confirmations(self) -> Optional[int]:
        return self.__confirmations

    def get_time(self) -> Optional[str]:
        return self.__time

    def get_received_time(self) -> Optional[str]:
        return self.__received_time

    def get_txid(self) -> Optional[str]:
        return self.__txid

    def get_ex_rates(self) -> Optional[List[dict]]:
        return self.__ex_rates

    def get_output_index(self) -> Optional[int]:
        return self.__output_index

    def set_amount(self, value: Optional[float]) -> None:
        self.__amount = value

    def set_confirmations(self, value: Optional[int]) -> None:
        self.__confirmations = value

    def set_time(self, value: Optional[str]) -> None:
        self.__time = value

    def set_received_time(self, value: Optional[str]) -> None:
        self.__received_time = value

    def set_txid(self, value: Optional[str]) -> None:
        self.__txid = value

    def set_ex_rates(self, value: Optional[List[dict]]) -> None:
        self.__ex_rates = value

    def set_output_index(self, value: Optional[int]) -> None:
        self.__output_index = value

    def to_json(self) -> dict:
        return ModelUtil.to_json(self)
