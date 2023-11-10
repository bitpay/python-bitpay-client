from bitpay.exceptions.bitpay_generic_exception import BitPayGenericException


class BitPayValidationException(BitPayGenericException):
    def __init__(self, message: str):
        super().__init__(message)
