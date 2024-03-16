from bitpay.client import Client
from bitpay.environment import Environment
from bitpay.models.bill.bill import Bill
from bitpay.models.facade import Facade


class BillRequests:
    def create_bill(self) -> None:
        client = Client.create_pos_client('somePosToken', Environment.TEST)

        bill = Bill()
        bill.name = 'someName'
        bill.email = 'someEmail@email.com'
        bill.address1 = 'SomeAddress'
        bill.city = 'MyCity'
        # ...

        result = client.create_bill(bill, Facade.POS, False)

    def get_bill(self) -> None:
        client = Client.create_pos_client('somePosToken', Environment.TEST)

        result = client.get_bill('someBillId', Facade.POS, False)

    def deliver_bill_via_email(self) -> None:
        client = Client.create_pos_client('somePosToken', Environment.TEST)

        result = client.deliver_bill('someBillId', 'token')
