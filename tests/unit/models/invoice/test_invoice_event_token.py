import pytest
from bitpay.models.invoice.invoice_event_token import InvoiceEventToken


@pytest.mark.unit
def test_constructor():
    actions = ["someActions"]
    events = ["someEvents"]
    token = "someToken"
    invoice_event_token = InvoiceEventToken(actions=actions, events=events, token=token)

    assert actions == invoice_event_token.actions
    assert events == invoice_event_token.events
    assert token == invoice_event_token.token
