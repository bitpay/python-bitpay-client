"""
BitPay Exception gets raised when some unexpected error occurs while processing a request
"""


class BitPayException(Exception):
    """
    BitPayException
    """

    __bitpay_message = "Unexpected Bitpay exception."
    __bitpay_code = "BITPAY-GENERIC"
    __api_code = ""

    def __init__(self, message, code=100, api_code="000000"):
        """
        Construct the BillUpdateException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)

    def get_api_code(self):
        """
        :return: Error code provided by the BitPay REST API
        """
        return self.__api_code
