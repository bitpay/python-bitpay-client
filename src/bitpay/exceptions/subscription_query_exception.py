"""
Subscription Query Exception gets raised when request for payout batch retrieval gets failed .
"""
from .subscription_exception import SubscriptionException


class SubscriptionQueryException(SubscriptionException):
    """
    SubscriptionQueryException
    """

    __bitpay_message = "Failed to retrieve subscription"
    __bitpay_code = "BITPAY-SUBSCRIPTION-GET"
    __api_code = ""

    def __init__(self, message, code=173, api_code="000000"):
        """
        Construct the SubscriptionQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
