"""
PayoutRecipientCreation Exception gets raised when request for recipient creation gets failed.
"""
from .payout_recipient_exception import PayoutRecipientException


class PayoutRecipientCreationException(PayoutRecipientException):
    """
    PayoutRecipientCreationException
    """

    __bitpay_message = "Failed to create payout recipient"
    __bitpay_code = "BITPAY-PAYOUT-RECIPIENT-SUBMIT"
    __api_code = ""

    def __init__(self, message: str, code: int = 112, api_code: str = "000000"):
        """
        Construct the PayoutRecipientCreationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
