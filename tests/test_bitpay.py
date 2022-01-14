"""
BitPay Unit Tests
"""
import os
import unittest
from datetime import date, timedelta

from src.bitpay_sdk.client import Client
from src.bitpay_sdk.models.invoice.buyer import Buyer
from src.bitpay_sdk.models.invoice.invoice import Invoice
from src.bitpay_sdk.models.invoice.invoice_status import InvoiceStatus


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
        