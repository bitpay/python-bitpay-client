import pytest

from bitpay.models.settlement.payout_info import PayoutInfo


@pytest.mark.unit
def test_constructor():
    routing = "someRouting"
    bank_name = "someBankName"
    account_holder_name = "someAccountHolderName"
    payout_info = PayoutInfo(
        routing=routing,
        bankName=bank_name,
        account_holder_name=account_holder_name
    )

    assert payout_info.routing == routing
    assert payout_info.bank_name == bank_name
    assert payout_info.account_holder_name == account_holder_name
