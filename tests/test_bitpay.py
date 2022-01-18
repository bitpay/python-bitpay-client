"""
BitPay Unit Tests
"""
import os
import unittest
from datetime import date, timedelta
from src.bitpay_sdk.client import Client
from src.bitpay_sdk.models.bill.bill import Bill
from src.bitpay_sdk.models.bill.item import Item
from src.bitpay_sdk.models.currency import Currency
from src.bitpay_sdk.models.invoice.buyer import Buyer
from src.bitpay_sdk.models.invoice.invoice import Invoice
from src.bitpay_sdk.models.bill.bill_status import BillStatus
from src.bitpay_sdk.models.payout.payout_recipient import PayoutRecipient
from src.bitpay_sdk.models.payout.recipient_status import RecipientStatus
from src.bitpay_sdk.models.payout.payout_recipients import PayoutRecipients


class BitPayTest(unittest.TestCase):
    """
    Unit Test functions
    """

    def setUp(self):
        self.bitpay = Client(os.path.abspath("bitpay.config.json").encode())

    def test_should_get_invoice_id(self):
        invoice = Invoice(2.16, "eur")
        invoice.set_order_id("98e572ea-910e-415d-b6de-65f5090680f6")
        invoice.set_full_notifications(True)
        invoice.set_extended_notifications(True)
        invoice.set_transaction_speed("medium")
        invoice.set_notification_url("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
        invoice.set_redirect_url("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
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

        invoice.set_buyer(buyer)

        basic_invoice = self.bitpay.create_invoice(invoice)
        retrieve_invoice = self.bitpay.get_invoice(basic_invoice.get_id())

        self.assertIsNotNone(basic_invoice.get_id())
        self.assertIsNotNone(retrieve_invoice.get_id())

    def test_should_create_invoice_btc(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(2.16, "btc"))
        self.assertIsNotNone(basic_invoice.get_id())

    def test_should_create_invoice_bch(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(2.16, "bch"))
        self.assertIsNotNone(basic_invoice.get_id())

    def test_should_create_invoice_eth(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(2.16, "eth"))
        self.assertIsNotNone(basic_invoice.get_id())

    def test_should_get_invoice_URL(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(5.0, "usd"))
        self.assertIsNotNone(basic_invoice.get_url())

    def test_should_get_invoice_status(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(5.0, "usd"))
        self.assertEqual("new", basic_invoice.get_status())

    def test_should_create_invoice_one_tenth_btc(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(0.1, "btc"))
        self.assertEqual(0.1, basic_invoice.get_price())

    def test_should_create_invoice_100_usd(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(100.0, "usd"))
        self.assertEqual(100.0, basic_invoice.get_price())

    def test_should_create_invoice_100_eur(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(100.0, "eur"))
        self.assertEqual(100.0, basic_invoice.get_price())

    def test_should_get_invoice(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(5.0, "eur"))
        retrieved_invoice = self.bitpay.get_invoice(basic_invoice.get_id())

        self.assertEqual(basic_invoice.get_id(), retrieved_invoice.get_id())

    def test_should_get_invoices(self):
        today = date.today().strftime("%Y%m%d")
        date_start = (date.today() - timedelta(days=30)).strftime("%Y%m%d")
        invoices = self.bitpay.get_invoices(date_start, today, None, None, None, None)

        self.assertIsNotNone(invoices)
        self.assertGreater(len(invoices), 0)

    def test_should_create_update_and_delete_invoice(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(2, "btc"))
        retrieved_invoice = self.bitpay.get_invoice(basic_invoice.get_id())
        updated_invoice = self.bitpay.update_invoice(retrieved_invoice.get_id(),
                                                     "sandbox@bitpay.com")
        cancelled_invoice = self.bitpay.cancel_invoice(updated_invoice.get_id())
        retrieved_cancelled_invoice = self.bitpay.get_invoice(cancelled_invoice.get_id())

        self.assertIsNotNone(basic_invoice)
        self.assertIsNotNone(retrieved_invoice)
        self.assertIsNotNone(updated_invoice)
        self.assertIsNotNone(cancelled_invoice)
        self.assertIsNotNone(retrieved_cancelled_invoice)

    def test_should_request_invoice_webhook(self):
        basic_invoice = self.bitpay.create_invoice(Invoice(2, "btc"))
        result = self.bitpay.request_invoice_notifications(basic_invoice.get_id())
        self.assertTrue(result)

    def test_should_create_get_cancel_refund_request_new(self):
        today = date.today().strftime("%Y%m%d")
        date_start = (date.today() - timedelta(days=30)).strftime("%Y%m%d")
        invoices = self.bitpay.get_invoices(date_start, today, "complete", None, None, None)
        first_invoice = invoices[0]
        create_refund = self.bitpay.create_refund(first_invoice.get_id(),
                                                  1.0, "usd", True, False, False)
        retrieved_refunds = self.bitpay.get_refunds(first_invoice.get_id())
        last_refund = retrieved_refunds[-1]
        update_refund = self.bitpay.update_refund(last_refund.get_id(), "created")
        retrieved_refund = self.bitpay.get_refund(last_refund.get_id())
        notification_status = self.bitpay.request_refund_notification(last_refund.get_id())
        cancel_refund = self.bitpay.cancel_refund(last_refund.get_id())
        supported_wallets = self.bitpay.get_supported_wallets()

        self.assertIsNotNone(invoices)
        self.assertIsNotNone(retrieved_refunds)
        self.assertEqual("created", update_refund.get_status())
        self.assertEqual(last_refund.get_id(), retrieved_refund.get_id())
        self.assertTrue(notification_status)
        self.assertEqual("cancelled", cancel_refund.get_status())
        self.assertIsNotNone(supported_wallets)

    def test_should_create_bill_usd(self):
        items = []

        item = Item()
        item.set_price(30.0)
        item.set_quantity(9)
        item.set_description("product-a")
        items.append(item)

        item = Item()
        item.set_price(14.0)
        item.set_quantity(16)
        item.set_description("product-b")
        items.append(item)

        item = Item()
        item.set_price(17.0)
        item.set_quantity(24)
        item.set_description("product-c")
        items.append(item)

        item = Item()
        item.set_price(4.0)
        item.set_quantity(46)
        item.set_description("product-d")
        items.append(item)

        bill = Bill("1001", Currency.USD, "sandbox@bitpay.com", items)
        basic_bill = self.bitpay.create_bill(bill)

        self.assertIsNotNone(basic_bill.get_id())
        self.assertIsNotNone(basic_bill.get_items()[0].get_id())

    def test_should_create_bill_eur(self):
        items = []

        item = Item()
        item.set_price(30.0)
        item.set_quantity(9)
        item.set_description("product-a")
        items.append(item)

        item = Item()
        item.set_price(14.0)
        item.set_quantity(16)
        item.set_description("product-b")
        items.append(item)

        item = Item()
        item.set_price(17.0)
        item.set_quantity(24)
        item.set_description("product-c")
        items.append(item)

        item = Item()
        item.set_price(4.0)
        item.set_quantity(46)
        item.set_description("product-d")
        items.append(item)

        bill = Bill("1002", Currency.EUR, "sandbox@bitpay.com", items)
        basic_bill = self.bitpay.create_bill(bill)

        self.assertIsNotNone(basic_bill.get_id())
        self.assertIsNotNone(basic_bill.get_items()[0].get_id())
        self.assertEqual(BillStatus.Draft, basic_bill.get_status())
        self.assertIsNotNone(basic_bill.get_url())

    def test_should_get_bill(self):
        items = []

        item = Item()
        item.set_price(30.0)
        item.set_quantity(9)
        item.set_description("product-a")
        items.append(item)

        item = Item()
        item.set_price(14.0)
        item.set_quantity(16)
        item.set_description("product-b")
        items.append(item)

        item = Item()
        item.set_price(17.0)
        item.set_quantity(24)
        item.set_description("product-c")
        items.append(item)

        item = Item()
        item.set_price(4.0)
        item.set_quantity(46)
        item.set_description("product-d")
        items.append(item)

        bill = Bill("1003", Currency.USD, "sandbox@bitpay.com", items)
        basic_bill = self.bitpay.create_bill(bill)
        retrieve_bill = self.bitpay.get_bill(basic_bill.get_id())

        self.assertEqual(basic_bill.get_id(), retrieve_bill.get_id())
        self.assertEqual(basic_bill.get_items(), retrieve_bill.get_items())

    def test_should_update_bill(self):
        items = []

        item = Item()
        item.set_price(30.0)
        item.set_quantity(9)
        item.set_description("product-a")
        items.append(item)

        item = Item()
        item.set_price(14.0)
        item.set_quantity(16)
        item.set_description("product-b")
        items.append(item)

        item = Item()
        item.set_price(17.0)
        item.set_quantity(24)
        item.set_description("product-c")
        items.append(item)

        item = Item()
        item.set_price(4.0)
        item.set_quantity(46)
        item.set_description("product-d")
        items.append(item)

        bill = Bill("1004", Currency.EUR, "sandbox@bitpay.com", items)
        basic_bill = self.bitpay.create_bill(bill)
        retrieve_bill = self.bitpay.get_bill(basic_bill.get_id())

        self.assertEqual(basic_bill.get_id(), retrieve_bill.get_id())
        self.assertEqual(basic_bill.get_items(), retrieve_bill.get_items())
        self.assertCountEqual(4, retrieve_bill.get_items())

        items = retrieve_bill.get_items()
        item = Item()
        item.set_price(50.0)
        item.set_quantity(7)
        item.set_description("product-added")
        items.append(item)

        retrieve_bill.set_items(items)
        update_bill = self.bitpay.update_bill(retrieve_bill, retrieve_bill.get_id())
        items = update_bill.get_items()

        self.assertCountEqual(5, update_bill.get_items())
        self.assertEqual(items[-1].get_description(), "product-added")

    def test_should_get_bills(self):
        bills = self.bitpay.get_bills()

        self.assertGreater(0, len(bills))

    def test_should_get_bills_by_status(self):
        bills = self.bitpay.get_bills(BillStatus.Draft)

        self.assertGreater(0, len(bills))

    def test_should_deliver_bill(self):
        items = []

        item = Item()
        item.set_price(30.0)
        item.set_quantity(9)
        item.set_description("product-a")
        items.append(item)

        item = Item()
        item.set_price(14.0)
        item.set_quantity(16)
        item.set_description("product-b")
        items.append(item)

        item = Item()
        item.set_price(17.0)
        item.set_quantity(24)
        item.set_description("product-c")
        items.append(item)

        item = Item()
        item.set_price(4.0)
        item.set_quantity(46)
        item.set_description("product-d")
        items.append(item)

        bill = Bill("1005", Currency.EUR, "sandbox@bitpay.com", items)
        basic_bill = self.bitpay.create_bill(bill)
        result = self.bitpay.deliver_bill(basic_bill.get_id(),
                                          basic_bill.get_token())
        retrieve_bill = self.bitpay.get_bill(basic_bill.get_id())

        self.assertEqual(basic_bill.get_id(), retrieve_bill.get_id())
        self.assertEqual(basic_bill.get_items(), retrieve_bill.get_items())
        self.assertEqual("Success", result)
        self.assertNotEqual(basic_bill.get_status(), retrieve_bill.get_status())
        self.assertEqual(BillStatus.Sent, retrieve_bill.get_status())

    def test_should_get_ledger_usd(self):
        today = date.today().strftime("%Y%m%d")
        date_start = (date.today() - timedelta(days=7)).strftime("%Y%m%d")
        ledger = self.bitpay.get_ledger(Currency.USD, date_start, today)

        self.assertIsNotNone(ledger)
        self.assertGreater(0, len(ledger))

    def test_should_get_ledger_btc(self):
        today = date.today().strftime("%Y%m%d")
        date_start = (date.today() - timedelta(days=7)).strftime("%Y%m%d")
        ledger = self.bitpay.get_ledger(Currency.BTC, date_start, today)

        self.assertIsNotNone(ledger)
        self.assertGreater(0, len(ledger))

    def test_should_get_ledgers(self):
        ledgers = self.bitpay.get_ledgers()

        self.assertIsNotNone(ledgers)
        self.assertGreater(0, len(ledgers))

    def test_should_submit_payout_recipients(self):
        recipients_list = []

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient1")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient2")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient3")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        recipients_obj = PayoutRecipients(recipients_list)
        recipients = self.bitpay.submit_payout_recipients(recipients_obj)

        self.assertIsNotNone(recipients)
        self.assertCountEqual(3, recipients)

    def test_should_get_payout_recipient_id(self):
        recipients_list = []

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient1")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        recipients_obj = PayoutRecipients(recipients_list)
        recipients = self.bitpay.submit_payout_recipients(recipients_obj)
        first_recipient = recipients[0]
        retrieve_recipient = self.bitpay.get_payout_recipient(first_recipient.get_id())

        self.assertIsNotNone(first_recipient)
        self.assertIsNotNone(retrieve_recipient.get_id())
        self.assertEqual(first_recipient.get_id(), retrieve_recipient.get_id())

    def test_should_get_payout_recipients(self):
        recipients = self.bitpay.get_payout_recipients('active', 2)

        self.assertIsNotNone(recipients)
        self.assertCountEqual(2, recipients)

    def test_should_submit_get_and_delete_payout_recipient(self):
        recipients_list = []

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient1")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        recipients_obj = PayoutRecipients(recipients_list)
        recipients = self.bitpay.submit_payout_recipients(recipients_obj)
        first_recipient = recipients[0]
        retrieve_recipient = self.bitpay.get_payout_recipient(first_recipient.get_id())
        retrieve_recipient.set_label("updatedLabel")
        update_recipient = self.bitpay.update_payout_recipient(retrieve_recipient.get_id(),
                                                               retrieve_recipient)
        delete_recipient = self.bitpay.delete_payout_recipient(retrieve_recipient.get_id())

        self.assertIsNotNone(first_recipient)
        self.assertIsNotNone(retrieve_recipient.get_id())
        self.assertEqual(first_recipient.get_id(), retrieve_recipient.get_id())
        self.assertEqual(RecipientStatus.INVITED, retrieve_recipient.get_status())
        self.assertTrue(delete_recipient)
        self.assertEqual("updatedLabel", update_recipient.get_label())

    def test_should_request_payout_recipient_notification(self):
        recipients_list = []

        payout_recipient = PayoutRecipient()
        payout_recipient.set_email("sandbox@bitpay.com")
        payout_recipient.set_label("recipient1")
        payout_recipient.set_notification_url("https://hookb.in/QJOPBdMgRkukpp2WO60o")
        recipients_list.append(payout_recipient)

        recipients_obj = PayoutRecipients(recipients_list)
        recipients = self.bitpay.submit_payout_recipients(recipients_obj)
        first_recipient = recipients[0]
        result = self.bitpay.request_payout_recipient_notification(first_recipient.get_id())

        self.assertTrue(result)
