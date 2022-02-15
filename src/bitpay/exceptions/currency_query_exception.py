"""
Currency Query Exception gets raised when request for currency retrieval gets failed .
"""
from .invoice_exception import InvoiceException


class CurrencyQueryException(InvoiceException):
    """
    CurrencyQueryException
    """

    __bitpay_message = "Failed to retrieve currencies"
    __bitpay_code = "BITPAY-CURRENCY-GET"
    __api_code = ""

    def __init__(self, message, code=182, api_code="000000"):
        """
        Construct the CurrencyQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
