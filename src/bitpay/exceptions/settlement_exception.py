"""
Settlement Exception gets raised when some unexpected error occurs while processing a request
or trying to manage settlement.
"""
from .bitpay_exception import BitPayException


class SettlementException(BitPayException):
    """
    SettlementException
    """

    __bitpay_message = (
        "An unexpected error occurred while trying to manage the settlement"
    )
    __bitpay_code = "BITPAY-SETTLEMENTS-GENERIC"
    __api_code = ""

    def __init__(self, message: str = "", code: int = 151, api_code: str = "000000"):
        """
        Construct the SettlementException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
