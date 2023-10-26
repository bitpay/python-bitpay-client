from typing import Union

from bitpay.exceptions.bitpay_exception import BitPayException


class BitPayApiException(BitPayException):
    """
    BitPayApiException
    """

    __message: str
    __code: Union[str, None] = None

    def __init__(self, message: str, code: Union[str, None]):
        """
        Construct the BitPayApiException.

        :param message: The Exception message to throw.
        :param code: [optional] The API Exception.
        """
        self.__code = code
        super().__init__(message)

    def get_code(self) -> Union[str, None]:
        """
        :return: Error code provided by the BitPay REST API
        """
        return self.__code
