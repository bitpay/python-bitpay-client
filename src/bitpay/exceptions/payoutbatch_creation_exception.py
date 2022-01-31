"""
Payout Creation Exception gets raised when request for payout batch creation gets failed.
"""
from .payout_exception import PayoutException


class PayoutBatchCreationException(PayoutException):
    """
    PayoutBatchCreationException
    """

    __bitpay_message = "Failed to create payout batch"
    __bitpay_code = "BITPAY-PAYOUT-BATCH-CREATE"
    __api_code = ""

    def __init__(self, message, code=202, api_code="000000"):
        """
        Construct the PayoutBatchCreationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
