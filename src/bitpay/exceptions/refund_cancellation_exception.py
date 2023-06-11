"""
Refund Cancellation exception gets raised when refund request gets failed.
"""
from .refund_exception import RefundException


class RefundCancellationException(RefundException):
    """
    RefundCancellationException
    """

    __bitpay_message = "Failed to cancel refund object"
    __bitpay_code = "BITPAY-REFUND-CANCEL"
    __api_code = ""

    def __init__(self, message: str, code: int = 165, api_code: str = "000000"):
        """
        Construct the RefundCancellationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
