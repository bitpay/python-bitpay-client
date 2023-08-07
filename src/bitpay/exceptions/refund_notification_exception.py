"""
Refund Notification Exception gets raised when webhook fails to send notification
"""
from .refund_exception import RefundException


class RefundNotificationException(RefundException):
    """
    RefundNotificationException
    """

    __bitpay_message = "Failed to send refund notification"
    __bitpay_code = "BITPAY-REFUND-NOTIFICATION"
    __api_code = ""

    def __init__(self, message: str, code: int = 166, api_code: str = "000000"):
        """
        Construct the RefundNotificationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
