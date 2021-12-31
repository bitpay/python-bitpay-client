from bitpay_exception import BitPayException


class InvoiceException(BitPayException):
    __bitpay_message = "An unexpected error occurred while trying to manage the invoice"
    __bitpay_code = "BITPAY-INVOICE-GENERIC"
    __apicode = ""

    '''
    Construct the InvoiceException.
    @param string $message [optional] The Exception message to throw.
    @param int    $code    [optional] The Exception code to throw.
    @param string $apicode [optional] The API Exception code to throw.
    '''

    def __init__(self, message="", code=100, apicode="000000"):
        if not message:
            message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__apicode = apicode
        super().__init__(message)

    """
        @return string Error code provided by the BitPay REST API
    """

    def get_apicode(self):
        return self.__apicode
