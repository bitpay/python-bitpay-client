import pytest

from bitpay.models.invoice.buyer_provided_info import BuyerProvidedInfo


@pytest.mark.unit
def test_constructor():
    name = "someName"
    phone_number = "1234"
    buyer_provided_info = BuyerProvidedInfo(**{"name": name, "phoneNumber": phone_number})

    assert name == buyer_provided_info.get_name()
    assert phone_number == buyer_provided_info.get_phone_number()


@pytest.mark.unit
def test_modify_email_address():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_email_address(value)
    
    assert value == buyer_provided_info.get_email_address()

    
@pytest.mark.unit
def test_modify_name():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_name(value)
    
    assert value == buyer_provided_info.get_name()
    
    
@pytest.mark.unit
def test_modify_phone_number():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_phone_number(value)
    
    assert value == buyer_provided_info.get_phone_number()
    
    
@pytest.mark.unit
def test_modify_selected_transaction_currency():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_selected_transaction_currency(value)
    
    assert value == buyer_provided_info.get_selected_transaction_currency()
    
    
@pytest.mark.unit
def test_modify_selected_wallet():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_selected_wallet(value)
    
    assert value == buyer_provided_info.get_selected_wallet()
    
    
@pytest.mark.unit
def test_modify_sms():
    buyer_provided_info = BuyerProvidedInfo()
    value = "someValue"
    buyer_provided_info.set_sms(value)
    
    assert value == buyer_provided_info.get_sms()
    
    
@pytest.mark.unit
def test_modify_sms_verified():
    buyer_provided_info = BuyerProvidedInfo()
    value = True
    buyer_provided_info.set_sms_verified(value)
    
    assert value == buyer_provided_info.get_sms_verified()
