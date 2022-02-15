"""
Rate Query Exception gets raised when request for rate retrieval gets failed .
"""
from .rates_exception import RateException


class RateQueryException(RateException):
    """
    RateQueryException
    """

    __bitpay_message = "Failed to retrieve rates"
    __bitpay_code = "BITPAY-RATES-GET"
    __api_code = ""

    def __init__(self, message, code=142, api_code="000000"):
        """
        Construct the RateQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
