"""
PayoutBatch Cancellation exception gets raised when it fails to cancel payout batch.
"""
from .payout_exception import PayoutException


class PayoutBatchCancellationException(PayoutException):
    """
    PayoutBatchCancellationException
    """
    __bitpay_message = "Failed to cancel payout batch"
    __bitpay_code = "BITPAY-PAYOUT-BATCH-CANCEL"
    __api_code = ""

    def __init__(self, message, code=204, api_code="000000"):
        """
        Construct the PayoutBatchCancellationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)

    # def get_api_code(self):
    #     """
    #     :return: Error code provided by the BitPay REST API
    #     """
    #     return self.__api_code
