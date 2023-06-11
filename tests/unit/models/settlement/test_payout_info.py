import pytest

from bitpay.models.settlement.payout_info import PayoutInfo


@pytest.mark.unit
def test_constructor():
    routing = "someRouting"
    bank_name = "someBankName"
    account_holder_name = "someAccountHolderName"
    payout_info = PayoutInfo(
        **{
            "routing": routing,
            "bankName": bank_name,
            "accountHolderName": account_holder_name,
        }
    )

    assert payout_info.get_routing() == routing
    assert payout_info.get_bank_name() == bank_name
    assert payout_info.get_account_holder_name() == account_holder_name


@pytest.mark.unit
def test_modify_name():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_name(value)

    assert payout_info.get_name() == value


@pytest.mark.unit
def test_modify_account():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account(value)

    assert payout_info.get_account() == value


@pytest.mark.unit
def test_modify_routing():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_routing(value)

    assert payout_info.get_routing() == value


@pytest.mark.unit
def test_modify_merchant_ein():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_merchant_ein(value)

    assert payout_info.get_merchant_ein() == value


@pytest.mark.unit
def test_modify_label():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_label(value)

    assert payout_info.get_label() == value


@pytest.mark.unit
def test_modify_bank_country():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_bank_country(value)

    assert payout_info.get_bank_country() == value


@pytest.mark.unit
def test_modify_bank():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_bank(value)

    assert payout_info.get_bank() == value


@pytest.mark.unit
def test_modify_swift():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_swift(value)

    assert payout_info.get_swift() == value


@pytest.mark.unit
def test_modify_address():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_address(value)

    assert payout_info.get_address() == value


@pytest.mark.unit
def test_modify_city():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_city(value)

    assert payout_info.get_city() == value


@pytest.mark.unit
def test_modify_postal():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_postal(value)

    assert payout_info.get_postal() == value


@pytest.mark.unit
def test_modify_sort():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_sort(value)

    assert payout_info.get_sort() == value


@pytest.mark.unit
def test_modify_wire():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_wire(value)

    assert payout_info.get_wire() == value


@pytest.mark.unit
def test_modify_bank_name():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_bank_name(value)

    assert payout_info.get_bank_name() == value


@pytest.mark.unit
def test_modify_bank_address():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_bank_address(value)

    assert payout_info.get_bank_address() == value


@pytest.mark.unit
def test_modify_bank_address2():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_bank_address2(value)

    assert payout_info.get_bank_address2() == value


@pytest.mark.unit
def test_modify_iban():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_iban(value)

    assert payout_info.get_iban() == value


@pytest.mark.unit
def test_modify_additional_information():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_additional_information(value)

    assert payout_info.get_additional_information() == value


@pytest.mark.unit
def test_modify_account_holder_name():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_name(value)

    assert payout_info.get_account_holder_name() == value


@pytest.mark.unit
def test_modify_account_holder_address():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_address(value)

    assert payout_info.get_account_holder_address() == value


@pytest.mark.unit
def test_modify_account_holder_address2():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_address2(value)

    assert payout_info.get_account_holder_address2() == value


@pytest.mark.unit
def test_modify_account_holder_postal_code():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_postal_code(value)

    assert payout_info.get_account_holder_postal_code() == value


@pytest.mark.unit
def test_modify_account_holder_city():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_city(value)

    assert payout_info.get_account_holder_city() == value


@pytest.mark.unit
def test_modify_account_holder_country():
    payout_info = PayoutInfo()
    value = "someValue"
    payout_info.set_account_holder_country(value)

    assert payout_info.get_account_holder_country() == value
