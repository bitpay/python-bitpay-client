"""
Ledger Query Exception gets raised when request for ledger retrieval gets failed .
"""
from .ledger_exception import LedgerException


class LedgerQueryException(LedgerException):
    """
    LedgerQueryException
    """

    __bitpay_message = "Failed to retrieve ledger"
    __bitpay_code = "BITPAY-LEDGER-GET"
    __api_code = ""

    def __init__(self, message: str, code: int = 132, api_code: str = "000000"):
        """
        Construct the LedgerQueryException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
