from src.bitpay_sdk.exceptions.invoice_exception import InvoiceException


class InvoiceCancellationException(InvoiceException):
    __bitpay_message = "Failed to cancel invoice object"
    __bitpay_code = "BITPAY-INVOICE-CANCEL"
    __api_code = ""

    def __init__(self, message, code=104, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        return self.__api_code
