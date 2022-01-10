from src.bitpay_sdk.exceptions.bill_exception import BillException


class BillDeliveryException(BillException):
    __bitpay_message = "Failed to deliver bill"
    __bitpay_code = "BITPAY-BILL-DELIVERY"
    __api_code = ""

    def __init__(self, message, code=115, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
