import pytest
from bitpay.models.invoice.invoice_event_token import InvoiceEventToken


@pytest.mark.unit
def test_constructor():
    actions = ["someActions"]
    events = ["someEvents"]
    token = "someToken"
    invoice_event_token = InvoiceEventToken(
        **{"actions": actions, "events": events, "token": token}
    )

    assert actions == invoice_event_token.get_actions()
    assert events == invoice_event_token.get_events()
    assert token == invoice_event_token.get_token()


@pytest.mark.unit
def test_modify_actions():
    invoice_event_token = InvoiceEventToken()
    value = ["someValue"]
    invoice_event_token.set_actions(value)

    assert value == invoice_event_token.get_actions()


@pytest.mark.unit
def test_modify_events():
    invoice_event_token = InvoiceEventToken()
    value = ["someValue"]
    invoice_event_token.set_events(value)

    assert value == invoice_event_token.get_events()


@pytest.mark.unit
def test_modify_token():
    invoice_event_token = InvoiceEventToken()
    value = "someValue"
    invoice_event_token.set_token(value)

    assert value == invoice_event_token.get_token()
