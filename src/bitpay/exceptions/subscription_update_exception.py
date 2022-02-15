"""
Subscription Update Exception gets raised when it fails to update subscription
"""
from .subscription_exception import SubscriptionException


class SubscriptionUpdateException(SubscriptionException):
    """
    SubscriptionUpdateException
    """

    __bitpay_message = "Failed to update subscription"
    __bitpay_code = "BITPAY-SUBSCRIPTION-UPDATE"
    __api_code = ""

    def __init__(self, message, code=174, api_code="000000"):
        """
        Construct the SubscriptionUpdateException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
