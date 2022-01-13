from .invoice_exception import InvoiceException


class InvoiceCancellationException(InvoiceException):
    __bitpay_message = "Failed to cancel invoice object"
    __bitpay_code = "BITPAY-INVOICE-CANCEL"
    __api_code = ""

    def __init__(self, message, code=104, api_code="000000"):
        """
        Construct the InvoiceCancellationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(InvoiceCancellationException, self).__init__(message, code)

    # def get_api_code(self):
    #     """
    #     :return: Error code provided by the BitPay REST API
    #     """
    #     return self.__api_code
