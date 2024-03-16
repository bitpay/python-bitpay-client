from bitpay.client import Client
from bitpay.environment import Environment
from bitpay.models.facade import Facade
from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice


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

        client = Client.create_pos_client('somePosToken', Environment.TEST)

        result = client.create_invoice(invoice, Facade.POS, False)

    def get_invoice(self) -> None:
        client = Client.create_pos_client('somePosToken', Environment.TEST)

        invoice_by_id = client.get_invoice('someInvoiceId', Facade.POS, False)
