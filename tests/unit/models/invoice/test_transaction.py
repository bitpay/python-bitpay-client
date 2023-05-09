import pytest

from bitpay.models.invoice.transaction import Transaction


@pytest.mark.unit
def test_constructor():
    amount = 12.45
    confirmations = 4
    transaction = Transaction(**{"amount": amount, "confirmations": confirmations})

    assert transaction.get_amount() == amount
    assert transaction.get_confirmations() == confirmations


@pytest.mark.unit
def test_modify_amount():
    transaction = Transaction()
    value = 12.23
    transaction.set_amount(value)

    assert transaction.get_amount() == value


@pytest.mark.unit
def test_modify_confirmations():
    transaction = Transaction()
    value = 3
    transaction.set_confirmations(value)

    assert transaction.get_confirmations() == value


@pytest.mark.unit
def test_modify_time():
    transaction = Transaction()
    value = "someValue"
    transaction.set_time(value)

    assert transaction.get_time() == value


@pytest.mark.unit
def test_modify_received_time():
    transaction = Transaction()
    value = "someValue"
    transaction.set_received_time(value)

    assert transaction.get_received_time() == value


@pytest.mark.unit
def test_modify_txid():
    transaction = Transaction()
    value = "someValue"
    transaction.set_txid(value)

    assert transaction.get_txid() == value


@pytest.mark.unit
def test_modify_ex_rates():
    transaction = Transaction()
    value = []
    transaction.set_ex_rates(value)

    assert transaction.get_ex_rates() == value


@pytest.mark.unit
def test_modify_output_index():
    transaction = Transaction()
    value = 2
    transaction.set_output_index(2)

    assert transaction.get_output_index() == value
