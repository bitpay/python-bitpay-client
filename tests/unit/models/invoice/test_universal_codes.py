import pytest

from bitpay.models.invoice.universal_codes import UniversalCodes


@pytest.mark.unit
def test_constructor():
    payment_string = "someString"
    verification_link = "https://url.com"

    universal_codes = UniversalCodes(payment_string=payment_string, verificationLink=verification_link)

    assert payment_string == universal_codes.payment_string
    assert verification_link == universal_codes.verification_link
