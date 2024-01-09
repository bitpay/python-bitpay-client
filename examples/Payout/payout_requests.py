from bitpay.models.payout.payout import Payout
from examples.client_provider import ClientProvider


class PayoutRequests:
    def createPayout(self) -> None:
        client = ClientProvider.create()

        payout = Payout()
        payout.notification_email = 'myEmail@email.com'
        payout.notification_url = 'https://my-url.com'

        result = client.submit_payout(payout)

        payouts = client.create_payout_group([payout])

    def get_payout(self) -> None:
        client = ClientProvider.create()

        payout = client.get_payout('myPayoutId')

        payouts = client.get_payouts('2023-08-14', '2023-08-22')

    def cancel_payout(self) -> None:
        client = ClientProvider.create()

        client.cancel_payout('payoutId')

        # payout_group = payout.group_id
        client.cancel_payout_group('payoutGroupId')

    def request_payout_webhook_to_be_resent(self) -> None:
        client = ClientProvider.create()

        client.request_payout_notification('somePayoutId')
