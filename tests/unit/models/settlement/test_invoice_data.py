import pytest

from bitpay.models.invoice.refund_info import RefundInfo
from bitpay.models.settlement.invoice_data import InvoiceData


@pytest.mark.unit
def test_constructor():
    price = 12.23
    transaction_currency = "BCH"
    refund_info = RefundInfo()

    invoice_data = InvoiceData(
        **{
            "price": price,
            "transactionCurrency": transaction_currency,
            "refundInfo": refund_info,
        }
    )

    assert price == invoice_data.get_price()
    assert transaction_currency == invoice_data.get_transaction_currency()
    assert refund_info == invoice_data.get_refund_info()


@pytest.mark.unit
def test_modify_order_id():
    invoice_data = InvoiceData()
    value = "someValue"
    invoice_data.set_order_id(value)

    assert value == invoice_data.get_order_id()


@pytest.mark.unit
def test_modify_date():
    invoice_data = InvoiceData()
    value = "someValue"
    invoice_data.set_date(value)

    assert value == invoice_data.get_date()


@pytest.mark.unit
def test_modify_price():
    invoice_data = InvoiceData()
    value = 12
    invoice_data.set_price(value)

    assert value == invoice_data.get_price()


@pytest.mark.unit
def test_modify_currency():
    invoice_data = InvoiceData()
    value = "someValue"
    invoice_data.set_currency(value)

    assert value == invoice_data.get_currency()


@pytest.mark.unit
def test_modify_transaction_currency():
    invoice_data = InvoiceData()
    value = "someValue"
    invoice_data.set_transaction_currency(value)

    assert value == invoice_data.get_transaction_currency()


@pytest.mark.unit
def test_modify_over_paid_amount():
    invoice_data = InvoiceData()
    value = 35
    invoice_data.set_over_paid_amount(value)

    assert value == invoice_data.get_over_paid_amount()


@pytest.mark.unit
def test_modify_payout_percentage():
    invoice_data = InvoiceData()
    value = []
    invoice_data.set_payout_percentage(value)

    assert value == invoice_data.get_payout_percentage()


@pytest.mark.unit
def test_modify_buyer_email_address():
    invoice_data = InvoiceData()
    value = "someValue"
    invoice_data.set_buyer_email_address(value)

    assert value == invoice_data.get_buyer_email_address()


@pytest.mark.unit
def test_modify_refund_info():
    invoice_data = InvoiceData()
    value = RefundInfo()
    invoice_data.set_refund_info(value)

    assert value == invoice_data.get_refund_info()
