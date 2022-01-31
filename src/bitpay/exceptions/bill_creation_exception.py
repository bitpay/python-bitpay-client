"""
Bill Creation Exception gets raised when request for bill creation gets failed.
"""
from .bill_exception import BillException


class BillCreationException(BillException):
    """
    BillCreationException
    """

    __bitpay_message = "Failed to create bill"
    __bitpay_code = "BITPAY-BILL-CREATE"
    __api_code = ""

    def __init__(self, message, code=112, api_code="000000"):
        """
        Construct the BillCreationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
