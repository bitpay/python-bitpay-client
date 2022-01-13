from .bitpay_exception import BitPayException


class LedgerException(BitPayException):
    __bitpay_message = "An unexpected error occurred while trying to manage the ledger"
    __bitpay_code = "BITPAY-LEDGER-GENERIC"
    __api_code = ""

    def __init__(self, message="", code=131, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(LedgerException, self).__init__(message, code)

    # def get_api_code(self):
    #     return self.__api_code
