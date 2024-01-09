from examples.client_provider import ClientProvider


class WalletRequests:
    def get_supported_wallets(self) -> None:
        client = ClientProvider.create()

        rates = client.get_supported_wallets()
