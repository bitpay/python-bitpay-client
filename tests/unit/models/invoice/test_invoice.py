import pytest

from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.itemized_details import ItemizedDetails
from bitpay.models.invoice.shopper import Shopper


@pytest.mark.unit
def test_constructor():
    price = 10.25
    currency = "BCH"
    shopper = Shopper()
    guid = "someGuid"
    buyer_name = "someName"
    itemized_details = [ItemizedDetails(), ItemizedDetails()]

    invoice = Invoice(
        price=price,
        currency=currency,
        shopper=shopper,
        guid=guid,
        buyer=Buyer(name=buyer_name),
        itemizedDetails=itemized_details
    )

    assert price == invoice.price
    assert currency == invoice.currency
    assert shopper == invoice.shopper
    assert guid == invoice.guid
    assert buyer_name == invoice.buyer.name
    assert itemized_details == invoice.itemized_details
