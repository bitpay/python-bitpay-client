"""
Invoice Payment exception gets raised when it fails to pay invoice.
"""
from .invoice_exception import InvoiceException


class InvoicePaymentException(InvoiceException):
    """
    InvoicePaymentException
    """

    __bitpay_message = "Failed to pay invoice"
    __bitpay_code = "BITPAY-INVOICE-PAY-UPDATE"
    __api_code = ""

    def __init__(self, message: str, code: int = 107, api_code: str = "000000"):
        """
        Construct the InvoicePaymentException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
