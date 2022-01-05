from src.bitpay_sdk.exceptions.invoice_exception import InvoiceException


class InvoiceNotificationException(InvoiceException):
    __bitpay_message = "Failed to send invoice notification"
    __bitpay_code = "BITPAY-INVOICE-NOTIFICATION"
    __api_code = ""

    def __init__(self, message, code=102, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
