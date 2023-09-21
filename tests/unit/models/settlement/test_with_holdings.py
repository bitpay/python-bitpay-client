import pytest

from bitpay.models.settlement.with_holdings import WithHoldings


@pytest.mark.unit
def test_constructor():
    amount = 12.34
    notes = "someNotes"
    label = "someLabel"
    withholdings = WithHoldings(amount=amount, notes=notes, label=label)

    assert amount == withholdings.amount
    assert notes == withholdings.notes
    assert label == withholdings.label
