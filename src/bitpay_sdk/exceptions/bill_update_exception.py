from .bill_exception import BillException


class BillUpdateException(BillException):
    __bitpay_message = "Failed to update bill"
    __bitpay_code = "BITPAY-BILL-UPDATE"
    __api_code = ""

    def __init__(self, message, code=114, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(BillUpdateException, self).__init__(message, code)

    # def get_api_code(self):
    #     return self.__api_code
