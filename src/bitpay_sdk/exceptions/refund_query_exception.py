from .refund_exception import RefundException


class RefundQueryException(RefundException):
    __bitpay_message = "Failed to retrieve refund"
    __bitpay_code = "BITPAY-REFUND-GET"
    __api_code = ""

    def __init__(self, message, code=163, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(RefundQueryException, self).__init__(message, code)

    # def get_api_code(self):
    #     return self.__api_code
