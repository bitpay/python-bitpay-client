import pytest

from bitpay.models.settlement.invoice_data import InvoiceData
from bitpay.models.settlement.refund_info import RefundInfo


@pytest.mark.unit
def test_constructor():
    price = 12.23
    transaction_currency = "BCH"
    refund_info = RefundInfo()

    invoice_data = InvoiceData(
        price=price,
        transaction_currency=transaction_currency,
        refund_info=refund_info
    )

    assert price == invoice_data.price
    assert transaction_currency == invoice_data.transaction_currency
    assert refund_info == invoice_data.refund_info
