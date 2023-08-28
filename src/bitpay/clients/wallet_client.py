from typing import List

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.wallet_query_exception import WalletQueryException
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
        :raises BitPayException
        :raises WalletQueryException
        """
        try:
            response_json = self.__bitpay_client.get("supportedWallets/", None, False)
        except BitPayException as exe:
            raise WalletQueryException(
                "failed to serialize wallet object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise WalletQueryException(
                "failed to serialize wallet object : %s" % str(exe)
            )

        try:
            wallets = []
            for wallet in response_json:
                wallets.append(Wallet(**wallet))
        except Exception as exe:
            raise WalletQueryException(
                "failed to deserialize BitPay server response (Wallet) : %s" % str(exe)
            )

        return wallets
