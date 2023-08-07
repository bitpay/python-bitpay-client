"""
Refund Update Exception gets raised when it fails to update refund
"""
from .refund_exception import RefundException


class RefundUpdateException(RefundException):
    """
    RefundUpdateException
    """

    __bitpay_message = "Failed to update refund"
    __bitpay_code = "BITPAY-REFUND-UPDATE"
    __api_code = ""

    def __init__(self, message: str, code: int = 164, api_code: str = "000000"):
        """
        Construct the RefundUpdateException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
