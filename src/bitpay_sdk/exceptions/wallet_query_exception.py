from .wallet_exception import WalletException


class WalletQueryException(WalletException):
    __bitpay_message = "Failed to retrieve supported wallets"
    __bitpay_code = "BITPAY-WALLET-GET"
    __api_code = ""

    def __init__(self, message, code=183, api_code="000000"):
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super(WalletQueryException, self).__init__(message, code)

    # def get_api_code(self):
    #     return self.__api_code
