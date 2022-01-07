from src.bitpay_sdk.exceptions.refund_exception import RefundException


class RefundUpdateException(RefundException):
    __bitpay_message = "Failed to update refund"
    __bitpay_code = "BITPAY-REFUND-UPDATE"
    __api_code = ""

    def __init__(self, message, code=164, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
