import pytest

from bitpay.models.settlement.with_holdings import WithHoldings


@pytest.mark.unit
def test_constructor():
    amount = 12.34
    notes = "someNotes"
    label = "someLabel"
    withholdings = WithHoldings(**{"amount": amount, "notes": notes, "label": label})

    assert amount == withholdings.get_amount()
    assert notes == withholdings.get_notes()
    assert label == withholdings.get_label()


@pytest.mark.unit
def test_modify_amount():
    withholdings = WithHoldings()
    value = 6
    withholdings.set_amount(value)

    assert withholdings.get_amount() == value


@pytest.mark.unit
def test_modify_code():
    withholdings = WithHoldings()
    value = "someValue"
    withholdings.set_code(value)

    assert withholdings.get_code() == value


@pytest.mark.unit
def test_modify_description():
    withholdings = WithHoldings()
    value = "someValue"
    withholdings.set_description(value)

    assert withholdings.get_description() == value


@pytest.mark.unit
def test_modify_notes():
    withholdings = WithHoldings()
    value = "someValue"
    withholdings.set_notes(value)

    assert withholdings.get_notes() == value


@pytest.mark.unit
def test_modify_label():
    withholdings = WithHoldings()
    value = "someValue"
    withholdings.set_label(value)

    assert withholdings.get_label() == value


@pytest.mark.unit
def test_modify_bank_country():
    withholdings = WithHoldings()
    value = "someValue"
    withholdings.set_bank_country(value)

    assert withholdings.get_bank_country() == value


