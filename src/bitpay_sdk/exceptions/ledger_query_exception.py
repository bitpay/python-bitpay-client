from src.bitpay_sdk.exceptions.ledger_exception import LedgerException


class LedgerQueryException(LedgerException):
    __bitpay_message = "Failed to retrieve ledger"
    __bitpay_code = "BITPAY-LEDGER-GET"
    __api_code = ""

    def __init__(self, message, code=132, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
