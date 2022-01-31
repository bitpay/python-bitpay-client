"""
Currency Exception gets raised when some unexpected error occurs while processing a request
or trying to manage currencies.
"""
from .bitpay_exception import BitPayException


class CurrencyException(BitPayException):
    """
    CurrencyException
    """

    __bitpay_message = (
        "An unexpected error occurred while trying to manage the currency"
    )
    __bitpay_code = "BITPAY-CURRENCY-GENERIC"
    __api_code = ""

    def __init__(self, message="", code=181, api_code="000000"):
        """
        Construct the CurrencyException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
