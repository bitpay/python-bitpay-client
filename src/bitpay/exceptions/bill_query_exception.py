"""
Bill Query Exception gets raised when request for bill retrieval gets failed .
"""
from .bill_exception import BillException


class BillQueryException(BillException):
    """
    BillQueryException
    """

    __bitpay_message = "Failed to retrieve bill"
    __bitpay_code = "BITPAY-BILL-GET"
    __api_code = ""

    def __init__(self, message, code=113, api_code="000000"):
        """
        Construct the BillQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
