from bitpay.models.facade import Facade
from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice
from examples.client_provider import ClientProvider


class InvoiceRequests:
    def create_invoice(self) -> None:
        invoice = Invoice()
        invoice.full_notifications = True
        invoice.extended_notifications = True
        invoice.notification_url = "https://test/lJnJg9WW7MtG9GZlPVdj"
        invoice.redirect_url = "https://test/lJnJg9WW7MtG9GZlPVdj"
        invoice.notification_email = "my@email.com"

        buyer = Buyer()
        buyer.name = "Test"
        buyer.email = "test@email.com"
        buyer.address1 = "168 General Grove"
        buyer.country = "AD"
        buyer.locality = "Port Horizon"
        buyer.notify = True
        buyer.phone = "+990123456789"
        buyer.postal_code = "KY7 1TH"
        buyer.region = "New Port"

        invoice.buyer = buyer

        client = ClientProvider.create()

        result = client.create_invoice(invoice, Facade.MERCHANT)

    def get_invoice(self) -> None:
        client = ClientProvider.create()

        invoice_by_id = client.get_invoice('someInvoiceId')

        invoice_by_guid = client.get_invoice_by_guid('someGuid')

        invoices = client.get_invoices('2023-04-14', '2023-04-17')

    def update_invoice(self) -> None:
        client = ClientProvider.create()

        result = client.update_invoice('someInvoiceId', None, '123123213')

    def cancel_invoice(self) -> None:
        client = ClientProvider.create()

        client.cancel_invoice('someInvoiceId')

        client.cancel_invoice_by_guid('someGuid')

    def request_invoice_webhook_to_be_resent(self) -> None:
        client = ClientProvider.create()

        client.request_invoice_notifications('someInvoiceId')
