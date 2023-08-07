import os
import datetime

import pytest

from bitpay.client import Client
from bitpay.models.bill.bill import Bill
from bitpay.models.bill.item import Item
from bitpay.models.facade import Facade
from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.refund import Refund
from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients
from bitpay.models.payout.payout_status import PayoutStatus


class TestClient:
    """
    Before use these tests you have to generate BitPay.config.json by BitPaySetup and put this file
    into this directory.
    You should create recipient in test.bitpay.com/dashboard/payouts/recipients and put this email
    to "email.txt" file in this directory. It's required for submit requests.
    It's impossible to test settlements in test environment.
    """

    __client = None
    __email = None

    @classmethod
    def setup_class(cls):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "email.txt")
        try:
            with open(file_path, "r") as file:
                cls.__email = file.read()
        except Exception as exe:
            raise Exception(
                "Please create in this directory email.txt according with class description"
            )
        if cls.__email == "":
            raise Exception("Please fill correct email")

        config_path = os.path.join(current_directory, "bitpay.config.json")
        if not os.path.exists(config_path):
            raise Exception(
                "Please create in this directory bitpay.config.json for functional tests"
            )
        cls.__client = Client.create_client_by_config_file_path(config_path)

    def example_invoice(self) -> Invoice:
        invoice = Invoice(10, "eur")
        invoice.set_order_id("98e572ea-910e-415d-b6de-65f5090680f6")
        invoice.set_full_notifications(True)
        invoice.set_extended_notifications(True)
        invoice.set_transaction_speed("medium")
        invoice.set_notification_url("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
        invoice.set_redirect_u_r_l("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
        invoice.set_pos_data("98e572ea35hj356xft8y8cgh56h5090680f6")
        invoice.set_item_desc("Ab tempora sed ut.")
        buyer = Buyer()
        buyer.set_name("Bily Matthews")
        buyer.set_email("sandbox@bitpay.com")
        buyer.set_address1("168 General Grove")
        buyer.set_address2("sandbox@bitpay.com")
        buyer.set_country("AD")
        buyer.set_locality("Port Horizon")
        buyer.set_notify(True)
        buyer.set_phone("+99477512690")
        buyer.set_postal_code("KY7 1TH")
        buyer.set_region("New Port")
        buyer.set_buyer_email("sandbox1@bitpay.com")
        invoice.set_buyer(buyer)
        return invoice

    @pytest.mark.functional
    def test_wallet_requests(self):
        supported_wallets = self.__client.get_supported_wallets()
        assert len(supported_wallets) > 0

    @pytest.mark.functional
    def test_rate_requests(self):
        rate = self.__client.get_currency_pair_rate("BCH", "USD")
        assert rate.get_rate() > 0

        rates = self.__client.get_rates()
        assert rates.get_rate("USD") > 0

        rate_usd = self.__client.get_currency_rates("BTC")
        assert rate_usd.get_rate("BCH") > 0

    @pytest.mark.functional
    def test_currency_requests(self):
        currencies = self.__client.get_currencies()
        btc = currencies.get("BTC")
        assert "Bitcoin", btc.get_name()

    @pytest.mark.functional
    def test_invoice_requests(self):
        invoice = self.__client.create_invoice(self.example_invoice())
        invoice_token = invoice.get_token()
        invoice_id = invoice.get_id()

        invoice_get = self.__client.get_invoice(invoice_id)
        assert invoice_token == invoice_get.get_token()

        invoice_get_by_guid = self.__client.get_invoice_by_guid(invoice.get_guid())
        assert invoice_token == invoice_get_by_guid.get_token()

        invoices = self.__client.get_invoices(
            TestClient.yesterday_date(), TestClient.tomorrow_date()
        )
        assert len(invoices) > 0
        assert any(i.get_token() == invoice_token for i in invoices) is True

        invoice_event_token = self.__client.get_invoice_event_token(invoice_id)
        assert invoice_event_token.get_token() is not None

        updated_email = "updated@email.com"
        update_invoice = self.__client.update_invoice(invoice_id, updated_email)
        assert updated_email == update_invoice.get_buyer_provided_email()

        invoice_get_after_update = self.__client.get_invoice(invoice_id)
        assert invoice_get_after_update.get_buyer_provided_email() == updated_email

        cancel_invoice = self.__client.cancel_invoice(invoice_id)
        assert cancel_invoice.get_is_cancelled() is True

        invoice_to_cancel_by_guid = self.__client.create_invoice(self.example_invoice())
        cancel_invoice_by_guid = self.__client.cancel_invoice_by_guid(
            invoice_to_cancel_by_guid.get_guid()
        )
        assert cancel_invoice_by_guid.get_is_cancelled() is True

    @pytest.mark.functional
    def test_refunds_requests(self):
        invoice = self.__client.create_invoice(self.example_invoice())
        invoice_id = invoice.get_id()
        self.__client.pay_invoice(invoice_id)

        refund = self.__client.create_refund(invoice_id, 10.0)
        refund_id = refund.get_id()

        retrieve_refund = self.__client.get_refund(refund_id)
        assert retrieve_refund.get_id() == refund_id

        retrieve_refund_by_guid = self.__client.get_refund_by_guid(refund.get_guid())
        assert retrieve_refund_by_guid.get_id() == refund_id

        refunds = self.__client.get_refunds(invoice_id)
        assert len(refunds) > 0
        assert any(i.get_invoice() == invoice_id for i in refunds) is True

        refund_notification = self.__client.request_refund_notification(refund_id)
        assert refund_notification is True

        cancel_refund = self.__client.cancel_refund(refund_id)
        assert "canceled" == cancel_refund.get_status()
        retrieve_refund_after_canceled = self.__client.get_refund(refund_id)
        assert "canceled" == retrieve_refund_after_canceled.get_status()

        refund_to_cancel_by_guid = self.__client.create_refund(invoice_id, 10.0)
        cancel_by_guid = self.__client.cancel_refund_by_guid(
            refund_to_cancel_by_guid.get_guid()
        )
        retrieve_refund_after_canceled_by_guid = self.__client.get_refund(
            cancel_by_guid.get_id()
        )
        assert "canceled" == retrieve_refund_after_canceled_by_guid.get_status()

    @pytest.mark.functional
    def test_recipients_request(self):
        email = "bob@email.com"
        payout_recipient = PayoutRecipient(**{"email": email, "label": "Bob"})
        requested_recipients = [payout_recipient]

        recipients = self.__client.submit_payout_recipients(
            PayoutRecipients(**{"recipients": requested_recipients})
        )
        recipient_id = recipients[0].get_id()

        retrieve_recipient = self.__client.get_payout_recipient(recipient_id)
        assert email == retrieve_recipient.get_email()

        retrieve_recipients_by_status = self.__client.get_payout_recipients(
            "invited", 1, 0
        )
        assert len(retrieve_recipients_by_status) > 0

        updated_label = "updatedLabel"
        update_recipient_request = PayoutRecipient(**{"label": updated_label})
        update_recipient = self.__client.update_payout_recipient(
            recipient_id, update_recipient_request
        )
        assert updated_label == update_recipient.get_label()

        request_payout_recipient_notification = (
            self.__client.request_payout_recipient_notification(recipient_id)
        )
        assert request_payout_recipient_notification is True

        remove_recipient = self.__client.delete_payout_recipient(recipient_id)
        assert remove_recipient is True

    @pytest.mark.functional
    def test_payout_requests(self):
        payout_recipient = PayoutRecipient(**{"email": self.__email, "label": "Bob"})
        requested_recipients = [payout_recipient]

        recipients = self.__client.submit_payout_recipients(
            PayoutRecipients(**{"recipients": requested_recipients})
        )
        recipient_id = recipients[0].get_id()

        notification_url = "https://somenotificationURL.com"
        payout = Payout(
            10.00,
            "USD",
            "USD",
            **{
                "recipientId": recipient_id,
                "notificationEmail": self.__email,
                "reference": "Python Functional Test",
                "notificationURL": notification_url,
            }
        )
        submit_payout = self.__client.submit_payout(payout)
        payout_id = submit_payout.get_id()
        assert self.__email == submit_payout.get_notification_email()
        assert payout_id is not None

        get_payout_by_id = self.__client.get_payout(payout_id)
        assert self.__email == get_payout_by_id.get_notification_email()

        payouts = self.__client.get_payouts(
            TestClient.yesterday_date(), TestClient.tomorrow_date()
        )
        assert len(payouts) > 0
        assert any(p.get_notification_email() == self.__email for p in payouts) is True

        request_payout_notification = self.__client.request_payout_notification(
            payout_id
        )
        assert request_payout_notification is True

        cancel_payout = self.__client.cancel_payout(payout_id)
        assert cancel_payout is True

        payout_group = self.__client.create_payout_group([payout])
        payout_group_id = payout_group.get_payouts()[0].get_group_id()
        assert payout_group.get_payouts()[0].get_notification_url() == notification_url
        assert len(payout_group.get_payouts()) == 1

        cancel_payout_group = self.__client.cancel_payout_group(payout_group_id)
        assert cancel_payout_group.get_payouts()[0].get_status() == PayoutStatus.Cancelled

    @pytest.mark.functional
    def test_ledgers_requests(self):
        ledgers = self.__client.get_ledgers()
        assert len(ledgers) > 0

        ledger_entries = self.__client.get_ledger_entries(
            "USD", TestClient.yesterday_date(), TestClient.tomorrow_date()
        )
        assert len(ledger_entries) > 0

    @pytest.mark.functional
    def test_bills_requests(self):
        item1 = Item(**{"quantity": 1, "description": "Test Item 1", "price": 10.00})

        requested_bill = Bill(
            "bill1234-ABCD",
            "USD",
            "john@doe.com",
            **{
                "name": "John Doe",
                "address1": "2630 Hegal Place",
                "address2": "Apt 42",
                "city": "Alexandria",
                "state": "VA",
                "zip": "23242",
                "country": "US",
                "phone": "555-123-456",
                "dueDate": "2021-5-31",
                "passProcessingFee": True,
                "items": [item1],
            }
        )
        create_bill = self.__client.create_bill(requested_bill, Facade.MERCHANT)
        bill_id = create_bill.get_id()

        get_bill = self.__client.get_bill(bill_id)
        assert bill_id == get_bill.get_id()

        bills = self.__client.get_bills()
        assert len(bills) > 0

        item_updated = Item(
            **{"quantity": 1, "description": "Test Item Updated", "price": 9.00}
        )
        updated_bill_request = Bill(
            "bill1234-EFGH",
            "USD",
            "john@doe.com",
            **{"items": [item_updated], "token": create_bill.get_token()}
        )
        updated_bill = self.__client.update_bill(updated_bill_request, bill_id)
        assert updated_bill.get_items()[0].get_price() == 9.00

        deliver_bill = self.__client.deliver_bill(bill_id, create_bill.get_token())
        assert deliver_bill is True

    @staticmethod
    def yesterday_date():
        return (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    @staticmethod
    def tomorrow_date():
        return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
