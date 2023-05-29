"""
Payout Cancellation exception gets raised when it fails to cancel payout.
"""
from .payout_exception import PayoutException


class PayoutCancellationException(PayoutException):
    """
    PayoutCancellationException
    """

    __bitpay_message = "Failed to cancel payout object"
    __bitpay_code = "BITPAY-PAYOUT-CANCEL"
    __api_code = ""

    def __init__(self, message: str, code: int = 124, api_code: str = "000000"):
        """
        Construct the PayoutCancellationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
