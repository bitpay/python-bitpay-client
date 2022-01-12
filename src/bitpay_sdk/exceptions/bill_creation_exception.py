from .bill_exception import BillException


class BillCreationException(BillException):
    __bitpay_message = "Failed to create bill"
    __bitpay_code = "BITPAY-BILL-CREATE"
    __api_code = ""

    def __init__(self, message, code=112, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
