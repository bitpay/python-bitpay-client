from .bitpay_exception import BitPayException


class RefundException(BitPayException):
    __bitpay_message = "An unexpected error occurred while trying to manage the refund"
    __bitpay_code = "BITPAY-REFUND-GENERIC"
    __api_code = ""

    def __init__(self, message="", code=161, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)

    def get_api_code(self):
        return self.__api_code
