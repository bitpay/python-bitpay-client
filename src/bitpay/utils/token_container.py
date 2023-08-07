from typing import Dict

from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.models.facade import Facade


class TokenContainer:
    __data: Dict[Facade, str] = {}

    def get_access_token(self, facade: Facade) -> str:
        try:
            return self.__data[facade]
        except Exception as exe:
            raise BitPayException(
                "There is no token for the specified key: " + facade.value
            )

    def put(self, key: Facade, value: str) -> None:
        self.__data[key] = value

    def add_pos(self, token: str) -> None:
        self.__data[Facade.POS] = token

    def add_merchant(self, token: str) -> None:
        self.__data[Facade.MERCHANT] = token

    def add_payout(self, token: str) -> None:
        self.__data[Facade.PAYOUT] = token
