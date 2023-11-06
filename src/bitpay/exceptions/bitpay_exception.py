"""
BitPay Exception gets raised when some unexpected error occurs while processing a request
"""


class BitPayException(Exception):
    """
    BitPayException
    """

    __message: str

    def __init__(self, message: str):
        """
        Construct the BitPayException.

        :param message: The Exception message to throw.
        """
        self.__message = message
        super().__init__(message)

    def get_message(self) -> str:
        return self.__message
