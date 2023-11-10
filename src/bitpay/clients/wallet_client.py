from typing import List

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.wallet.wallet import Wallet


class WalletClient:
    __bitpay_client = BitPayClient

    def __init__(self, bitpay_client: BitPayClient):
        self.__bitpay_client = bitpay_client

    def get_supported_wallets(self) -> List[Wallet]:
        """
        Retrieve all supported wallets.

        :return: A list of wallet objets.
        :rtype: [Wallet]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        response = self.__bitpay_client.get("supportedWallets/", None, False)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            wallets = []
            for wallet in response_json:
                wallets.append(Wallet(**wallet))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Wallet", str(exe)
            )

        return wallets
