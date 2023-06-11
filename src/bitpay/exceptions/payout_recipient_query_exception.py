"""
PayoutRecipientQuery Exception gets raised when request for recipient retrieval gets failed .
"""
from .invoice_exception import InvoiceException


class PayoutRecipientQueryException(InvoiceException):
    """
    PayoutRecipientQueryException
    """

    __bitpay_message = "Failed to retrieve payout recipient"
    __bitpay_code = "BITPAY-PAYOUT-RECIPIENT-GET"
    __api_code = ""

    def __init__(self, message: str, code: int = 193, api_code: str = "000000"):
        """
        Construct the PayoutRecipientQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
