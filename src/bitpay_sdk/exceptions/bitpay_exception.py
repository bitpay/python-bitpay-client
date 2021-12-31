class BitPayException(Exception):
    __bitpay_message = "Unexpected Bitpay exception."
    __bitpay_code = "BITPAY-GENERIC";
    __apicode = ""

    """
        Construct the BitPayException.
        
        message (string) message [optional] The Exception message to throw.
        code (int)    $code    [optional] The Exception code to throw.
        @param string $apiCode [optional] The API Exception code to throw.
    """

    def __init__(self, message="", code=100, apicode="000000"):
        if not message:
            message = self.__bitpay_code + ": " + self.__bitpaymessage + ":" + message
        self.__apicode = apicode
        super().__init__(message)

    """
        @return string Error code provided by the BitPay REST API
    """
    def get_apicode(self):
        return self.__apicode
