from examples.client_provider import ClientProvider


class RateRequests:
    def get_rate(self) -> None:
        client = ClientProvider.create()

        rates = client.get_rates()

        currency_rates = client.get_currency_rates('BTC')

        currency_pair_rate = client.get_currency_pair_rate('BTC', 'USD')
