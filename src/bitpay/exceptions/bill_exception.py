"""
Bill Exception gets raised when some unexpected error occurs while processing a request
or trying to manage bills.
"""
from .bitpay_exception import BitPayException


class BillException(BitPayException):
    """
    BillException
    """

    __bitpay_message = "An unexpected error occurred while trying to manage the bill"
    __bitpay_code = "BITPAY-BILL-GENERIC"
    __api_code = ""

    def __init__(self, message="", code=111, api_code="000000"):
        """
        Construct the BillException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
