"""
Payout Notification Exception gets raised when webhook fails to send notification
"""

from .payout_exception import PayoutException


class PayoutNotificationException(PayoutException):
    """
    PayoutNotificationException
    """

    __bitpay_message = "Failed to send payout notification"
    __bitpay_code = "BITPAY-PAYOUT-NOTIFICATION"
    __api_code = ""

    def __init__(self, message: str, code: int = 126, api_code: str = "000000"):
        """
        Construct the PayoutNotificationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
