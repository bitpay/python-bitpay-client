"""
Refund Creation Exception gets raised when request for refund creation gets failed for invoice.
"""
from .refund_exception import RefundException


class RefundCreationException(RefundException):
    """
    RefundCreationException
    """

    __bitpay_message = "Failed to create refund"
    __bitpay_code = "BITPAY-REFUND-CREATE"
    __api_code = ""

    def __init__(self, message: str, code: int = 162, api_code: str = "000000"):
        """
        Construct the RefundCreationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
