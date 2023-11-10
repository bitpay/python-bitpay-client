from bitpay.exceptions.bitpay_exception import BitPayException


class BitPayGenericException(BitPayException):
    def __init__(self, message: str):
        super().__init__(message)
