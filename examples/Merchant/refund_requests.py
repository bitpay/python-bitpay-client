from examples.client_provider import ClientProvider


class RefundRequests:
    def create_refund(self) -> None:
        client = ClientProvider.create()

        result = client.create_refund('invoiceId', 12.34)

    def update_refund(self) -> None:
        client = ClientProvider.create()

        client.update_refund('refundId', 'created')

        client.update_refund_by_guid('someGuid', 'created')

    def get_refund(self) -> None:
        client = ClientProvider.create()

        client.get_refund('refundId')

        client.get_refund_by_guid('someGuid')

    def cancel_refund(self) -> None:
        client = ClientProvider.create()

        result = client.cancel_refund('someRefundId')

    def request_refund_notification_to_be_resent(self) -> None:
        client = ClientProvider.create()

        result = client.request_refund_notification('someRefundId')
