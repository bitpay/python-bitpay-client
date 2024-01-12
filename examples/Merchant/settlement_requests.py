from examples.client_provider import ClientProvider


class SettlementRequests:
    def get_settlement(self) -> None:
        client = ClientProvider.create()

        settlement = client.get_settlement('someSettlementId')

        settlements = client.get_settlements('USD', '2023-08-14', '2023-08-22')

    def fetch_reconciliation_report(self) -> None:
        client = ClientProvider.create()

        client.get_settlement_reconciliation_report('settlementId', 'settlementToken')
