import pytest

from bitpay.models.rate.rate import Rate


@pytest.mark.unit
def test_constructor():
    name = "someName"
    code = "1234"
    rate = 12.45
    tested_class = Rate(name=name, code=code, rate=rate)

    assert name == tested_class.name
    assert code == tested_class.code
    assert rate == tested_class.rate
