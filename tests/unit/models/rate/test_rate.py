import pytest

from bitpay.models.rate.rate import Rate


@pytest.mark.unit
def test_constructor():
    name = "someName"
    code = 1234
    rate = 12.45
    tested_class = Rate(**{"name": name, "code": code, "rate": rate})

    assert name == tested_class.get_name()
    assert code == tested_class.get_code()
    assert rate == tested_class.get_rate()


@pytest.mark.unit
def test_modify_name():
    rate = Rate()
    value = "someValue"
    rate.set_name(value)

    assert rate.get_name() == value


@pytest.mark.unit
def test_modify_code():
    rate = Rate()
    value = "someValue"
    rate.set_code(value)

    assert rate.get_code() == value


@pytest.mark.unit
def test_modify_rate():
    rate = Rate()
    value = 12.34
    rate.set_rate(value)

    assert rate.get_rate() == value
