import pytest

from bitpay.models.settlement.refund_info import RefundInfo


@pytest.mark.unit
def test_constructor():
    support_request = "someValue"
    currency = "USD"
    amounts = {"USD": 12.34}
    refund_info = RefundInfo(
        support_request=support_request, currency=currency, amounts=amounts
    )

    assert support_request == refund_info.support_request
    assert currency == refund_info.currency
    assert amounts == refund_info.amounts
