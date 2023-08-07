"""
Bill Update Exception gets raised when it fails to update bill
"""
from .bill_exception import BillException


class BillUpdateException(BillException):
    """
    BillUpdateException
    """

    __bitpay_message = "Failed to update bill"
    __bitpay_code = "BITPAY-BILL-UPDATE"
    __api_code = ""

    def __init__(self, message: str, code: int = 114, api_code: str = "000000"):
        """
        Construct the BillUpdateException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
