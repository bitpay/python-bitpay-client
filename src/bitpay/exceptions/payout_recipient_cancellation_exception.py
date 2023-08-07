"""
PayoutRecipient Cancellation exception gets raised when it fails to cancel payout recipient.
"""
from .payout_recipient_exception import PayoutRecipientException


class PayoutRecipientCancellationException(PayoutRecipientException):
    """
    PayoutRecipientCancellationException
    """

    __bitpay_message = "Failed to cancel payout recipient"
    __bitpay_code = "BITPAY-PAYOUT-RECIPIENT-CANCEL"
    __api_code = ""

    def __init__(self, message: str, code: int = 194, api_code: str = "000000"):
        """
        Construct the PayoutRecipientCancellationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
