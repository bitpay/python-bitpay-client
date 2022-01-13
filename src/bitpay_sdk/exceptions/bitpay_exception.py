class BitPayException(Exception):
    __bitpay_message = "Unexpected Bitpay exception."
    __bitpay_code = "BITPAY-GENERIC";
    __api_code = ""

    def __init__(self, message, code=100, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(BitPayException, self).__init__(message, code)

    def get_api_code(self):
        return self.__api_code
