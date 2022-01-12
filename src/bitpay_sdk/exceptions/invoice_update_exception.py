from .invoice_exception import InvoiceException


class InvoiceUpdateException(InvoiceException):
    __bitpay_message = "Failed to update invoice"
    __bitpay_code = "BITPAY-INVOICE-UPDATE"
    __api_code = ""

    def __init__(self, message, code=104, api_code="000000"):
        """
        Construct the InvoiceUpdateException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super.__init__(message, code)

    def get_api_code(self):
        """
        :return: Error code provided by the BitPay REST API
        """
        return self.__api_code
