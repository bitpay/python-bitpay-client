import pytest

from bitpay.models.invoice.universal_codes import UniversalCodes


@pytest.mark.unit
def test_constructor():
    payment_string = "someString"
    verification_link = "https://url.com"

    universal_codes = UniversalCodes(**{"paymentString": payment_string, "verificationLink": verification_link})

    assert payment_string == universal_codes.get_payment_string()
    assert verification_link == universal_codes.get_verification_link()


@pytest.mark.unit
def test_modify_payment_string():
    universal_codes = UniversalCodes()
    value = "someValue"
    universal_codes.set_payment_string(value)

    assert value == universal_codes.get_payment_string()


@pytest.mark.unit
def test_modify_verification_link():
    universal_codes = UniversalCodes()
    value = "someValue"
    universal_codes.set_verification_link(value)

    assert value == universal_codes.get_verification_link()
