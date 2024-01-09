from examples.client_provider import ClientProvider


class LedgerRequests:
    def get_ledgers(self) -> None:
        client = ClientProvider.create()

        result = client.get_ledgers()

    def get_ledger_entries(self) -> None:
        client = ClientProvider.create()

        result = client.get_ledger_entries('USD', '2023-08-14', '2023-08-22')
