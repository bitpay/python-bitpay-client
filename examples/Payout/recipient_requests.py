from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients
from examples.client_provider import ClientProvider


class RecipientRequests:
    def invite_recipients(self) -> None:
        client = ClientProvider.create()

        recipient = PayoutRecipient()
        recipient.email = 'some@email.com'

        result = client.submit_payout_recipients(
            PayoutRecipients(**{"recipients": [recipient]})
        )

    def get_recipient(self) -> None:
        client = ClientProvider.create()

        result = client.get_payout_recipient('recipientId')

    def update_recipient(self) -> None:
        client = ClientProvider.create()

        recipient = PayoutRecipient()
        recipient.email = 'some@email.com'

        result = client.update_payout_recipient('recipientId', recipient)

    def remove_recipient(self) -> None:
        client = ClientProvider.create()

        result = client.delete_payout_recipient('recipientId')
