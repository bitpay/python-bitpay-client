from bitpay.models.bill.bill import Bill
from bitpay.models.facade import Facade
from examples.client_provider import ClientProvider


class BillRequests:

    def create_bill(self) -> None:
        client = ClientProvider.create()

        bill = Bill()
        bill.name = 'someName'
        bill.email = 'someEmail@email.com'
        bill.address1 = 'SomeAddress'
        bill.city = 'MyCity'
        # ...

        client.create_bill(bill, Facade.MERCHANT)

    def get_bill(self) -> None:
        client = ClientProvider.create()

        bill = client.get_bill('someBillId', Facade.MERCHANT)

        bills = client.get_bills('draft')

    def update_bill(self) -> None:
        client = ClientProvider.create()

        bill = Bill()
        bill.email = 'myNew@email.com'

        result = client.update_bill(bill, 'someBillId')

    def deliver_bill_via_email(self) -> None:
        client = ClientProvider.create()

        result = client.deliver_bill('someBillId', 'someBillToken')
