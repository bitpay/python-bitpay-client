import json
import os
from typing import List

import pytest
from pytest_mock import mocker

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bill_update_exception import BillUpdateException
from bitpay.models.bill.bill import Bill
from bitpay.models.bill.item import Item
from bitpay.models.facade import Facade
from bitpay.models.invoice.buyer import Buyer
from bitpay.models.invoice.invoice import Invoice
from bitpay.client import Client
from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients
from bitpay.utils.guid_generator import GuidGenerator
from bitpay.utils.token_container import TokenContainer

guid_token = "chc9kj52-04g0-4b6f-941d-3a844e352758"
merchant_token_value = "someMerchantToken"
payout_token_value = "somePayoutToken"
pos_token_value = "somePosToken"
invoice_id = "UZjwcYkWAKfTMn9J1yyfs4"


def get_bitpay_client(mocker):
    return mocker.Mock(spec=BitPayClient)


def get_token_container(mocker):
    token_container = mocker.Mock(spec=TokenContainer)
    token_container.get_access_token.side_effect = lambda value: {
        Facade.MERCHANT: merchant_token_value,
        Facade.PAYOUT: payout_token_value,
    }.get(value)

    return token_container


def get_guid_generator(mocker):
    generator = mocker.Mock(spec=GuidGenerator)
    generator.execute.return_value = guid_token

    return generator


def init_client(mocker, bitpay_client) -> Client:
    return Client(
        bitpay_client, get_token_container(mocker), get_guid_generator(mocker)
    )


def mock_response(
    mocked_response, mocked_endpoint, mocked_data, mocked_sign_request=None
):
    return (
        lambda endpoint, json_response, sign_request=None: mocked_response
        if (endpoint, json_response, sign_request)
        == (mocked_endpoint, mocked_data, mocked_sign_request)
        else (
            mocked_response
            if sign_request is None
            and (endpoint, json_response) == (mocked_endpoint, mocked_data)
            else Exception("Invalid request")
        )
    )


def get_example_invoice():
    invoice = Invoice(2.16, "eur")
    invoice.set_order_id("98e572ea-910e-415d-b6de-65f5090680f6")
    invoice.set_full_notifications(True)
    invoice.set_extended_notifications(True)
    invoice.set_transaction_speed("medium")
    invoice.set_notification_url("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
    invoice.set_redirect_u_r_l("https://hookbin.com/lJnJg9WW7MtG9GZlPVdj")
    invoice.set_pos_data("98e572ea35hj356xft8y8cgh56h5090680f6")
    invoice.set_item_desc("Ab tempora sed ut.")
    buyer = Buyer()
    buyer.set_name("Bily Matthews")
    buyer.set_email("sandbox@bitpay.com")
    buyer.set_address1("168 General Grove")
    buyer.set_address2("sandbox@bitpay.com")
    buyer.set_country("AD")
    buyer.set_locality("Port Horizon")
    buyer.set_notify(True)
    buyer.set_phone("+99477512690")
    buyer.set_postal_code("KY7 1TH")
    buyer.set_region("New Port")
    buyer.set_buyer_email("sandbox1@bitpay.com")
    invoice.set_buyer(buyer)
    return invoice


def get_example_bill():
    cc: List[str] = ["jane@doe.com"]
    item1 = Item()
    item2 = Item()
    item1.set_description("Test Item 1")
    item1.set_price(6.00)
    item1.set_quantity(1)
    item2.set_description("Test Item 2")
    item2.set_price(4.00)
    item2.set_quantity(1)
    bill = Bill("bill1234-ABCD", "USD", "some@email.com")
    bill.set_name("John Doe")
    bill.set_address1("2630 Hegal Place")
    bill.set_address2("Apt 42")
    bill.set_city("Alexandria")
    bill.set_state("VA")
    bill.set_zip("23242")
    bill.set_country("US")
    bill.set_cc(cc)
    bill.set_phone("555-123-456")
    bill.set_due_date("2021-5-31")
    bill.set_pass_processing_fee(True)
    bill.set_items([item1, item2])
    return bill


def get_example_payout_recipients():
    recipient1 = PayoutRecipient()
    recipient2 = PayoutRecipient()
    recipient1.set_email("alice@email.com")
    recipient2.set_email("bob@email.com")
    recipient1.set_label("Alice")
    recipient2.set_label("Bob")
    recipients_list = [recipient1, recipient2]
    recipient = PayoutRecipients()
    recipient.set_recipients(recipients_list)
    return recipient


def get_example_payout():
    payout = Payout(10.00, "USD", "GBP")
    payout.set_reference("payout_20210527")
    payout.set_notification_url(
        "https://yournotiticationURL.com/wed3sa0wx1rz5bg0bv97851eqx"
    )
    payout.set_notification_email("merchant@email.com")
    payout.set_email("john@doe.com")
    payout.set_label("John Doe")
    return payout


@pytest.mark.unit
def test_get_currencies(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_currencies_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.get.side_effect = mock_response(response, "currencies", None, False)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_currencies()

    # assert
    assert len(result) == 183
    assert result.get("BTC").get_code() == "BTC"
    assert result.get("BTC").get_name() == "Bitcoin"


@pytest.mark.unit
def test_create_invoice_by_merchant(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_invoice_request.json",
        "r",
    ) as file:
        invoice_dict = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.post.side_effect = mock_response(
        response, "invoices", invoice_dict, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.create_invoice(get_example_invoice(), Facade.MERCHANT, True)

    # assert
    assert result.get_order_id() == "026184kc-d001-41j9-9732d-bb249u7b0c24"
    assert result.get_guid() == "chc9kj52-04g0-4b6f-941d-3a844e352758"
    assert result.get_buyer_provided_info().get_name() == "Marcin"
    assert result.get_payment_totals()["ETH"] == 9589000000000000
    assert result.get_merchant_name() == "SUMO Heavy Industries LLC"
    assert result.get_buyer().get_name() == "Marcin"
    assert result.get_payment_totals().get("BTC") == 72100
    assert result.get_payment_display_totals().get("ETH") == "0.009589"
    assert result.get_exchange_rates().get("BTC").get("USD") == 16676.624268104035
    assert result.get_miner_fees().get_btc().get_fiat_amount() == 0.02
    assert result.get_supported_transaction_currencies().get_pax().get_enabled() is True
    assert (
        result.get_payment_codes().get("BTC").get("BIP73")
        == "https://test.bitpay.com/i/UZjwcYkWAKfTMn9J1yyfs4"
    )
    assert (
        result.get_universal_codes().get_payment_string()
        == "https://link.test.bitpay.com/i/UZjwcYkWAKfTMn9J1yyfs4"
    )


@pytest.mark.unit
def test_create_invoice_by_pos(mocker):
    # arrange
    token_container = mocker.Mock(spec=TokenContainer)
    token_container.get_access_token.side_effect = lambda value: {
        Facade.POS: pos_token_value,
    }.get(value)

    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_invoice_by_pos_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.post.side_effect = mock_response(response, "invoices", request, False)
    client = Client(bitpay_client, token_container, get_guid_generator(mocker))

    # act
    result = client.create_invoice(get_example_invoice(), Facade.POS, False)

    # assert
    assert result.get_order_id() == "026184kc-d001-41j9-9732d-bb249u7b0c24"
    assert result.get_guid() == "chc9kj52-04g0-4b6f-941d-3a844e352758"
    assert result.get_buyer_provided_info().get_name() == "Marcin"
    assert result.get_payment_totals()["ETH"] == 9589000000000000
    assert result.get_merchant_name() == "SUMO Heavy Industries LLC"


@pytest.mark.unit
def test_get_invoice_by_merchant(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.get.side_effect = mock_response(
        response, "invoices/" + invoice_id, {"token": merchant_token_value}, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_invoice(invoice_id, Facade.MERCHANT)

    # assert
    assert result.get_guid() == guid_token
    assert result.get_order_id() == "084a86b6-68aa-47bc-b435-e64d122391d1"
    assert result.get_buyer_provided_info().get_name() == "Marcin"
    assert result.get_merchant_name() == "SUMO Heavy Industries LLC"


@pytest.mark.unit
def test_get_invoice_by_pos(mocker):
    # arrange
    token_container = mocker.Mock(spec=TokenContainer)
    token_container.get_access_token.side_effect = lambda value: {
        Facade.POS: pos_token_value,
    }.get(value)
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.get.side_effect = mock_response(
        response, "invoices/" + invoice_id, {"token": pos_token_value}, False
    )
    client = Client(bitpay_client, token_container, get_guid_generator(mocker))

    # act
    result = client.get_invoice(invoice_id, Facade.POS, False)

    # assert
    assert result.get_guid() == guid_token
    assert result.get_order_id() == "084a86b6-68aa-47bc-b435-e64d122391d1"
    assert result.get_buyer_provided_info().get_name() == "Marcin"
    assert result.get_merchant_name() == "SUMO Heavy Industries LLC"


@pytest.mark.unit
def test_get_invoice_by_guid(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.get.side_effect = mock_response(
        response, "invoices/guid/" + guid_token, {"token": merchant_token_value}, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_invoice_by_guid(guid_token, Facade.MERCHANT)

    # assert
    assert result.get_guid() == guid_token
    assert result.get_order_id() == "084a86b6-68aa-47bc-b435-e64d122391d1"
    assert result.get_buyer_provided_info().get_name() == "Marcin"
    assert result.get_merchant_name() == "SUMO Heavy Industries LLC"


@pytest.mark.unit
def test_get_invoices(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_invoices_response.json",
        "r",
    ) as file:
        response = json.load(file)
    date_start = "2022-5-10"
    date_end = "2022-5-11"
    status = "complete"
    limit = 1

    bitpay_client.get.side_effect = mock_response(
        response,
        "invoices/",
        {
            "token": merchant_token_value,
            "dateStart": date_start,
            "dateEnd": date_end,
            "status": status,
            "limit": limit,
        },
        True,
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_invoices(date_start, date_end, status, None, limit, None)

    # assert
    assert len(result) == 1
    assert result[0].get_order_id() == "084a86b6-68aa-47bc-b435-e64d122391d1"
    assert result[0].get_buyer_provided_info().get_name() == "Marcin"
    assert result[0].get_merchant_name() == "SUMO Heavy Industries LLC"


@pytest.mark.unit
def test_get_invoice_event_token(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_invoice_event_token.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.get.side_effect = mock_response(
        response,
        "invoices/%s/events" % invoice_id,
        {"token": merchant_token_value},
        True,
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_invoice_event_token(invoice_id)

    # assert
    assert (
        result.get_token()
        == "4MuqDPt93i9Xbf8SnAPniwbGeNLW8A3ScgAmukFMgFUFRqTLuuhVdAFfePPysVqL2P"
    )
    assert result.get_events()[1] == "confirmation"
    assert result.get_actions()[1] == "unsubscribe"


@pytest.mark.unit
def test_update_invoice(mocker):
    # arrange
    invoice_id = "12345"
    buyer_email = "some@email.com"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)

    bitpay_client.update.side_effect = mock_response(
        response,
        "invoices/" + invoice_id,
        {"token": merchant_token_value, "buyerEmail": buyer_email},
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.update_invoice(invoice_id, buyer_email)

    # assert
    assert result.get_guid() == "chc9kj52-04g0-4b6f-941d-3a844e352758"


@pytest.mark.unit
def test_pay_invoice(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/pay_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "status": "complete"}

    bitpay_client.update.side_effect = mock_response(
        response, "invoices/pay/" + invoice_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.pay_invoice(invoice_id, "complete")

    # assert
    assert result.get_status() == "complete"


@pytest.mark.unit
def test_forced_cancel_invoice(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/cancel_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "forceCancel": True}
    bitpay_client.delete.side_effect = mock_response(
        response, "invoices/" + invoice_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_invoice(invoice_id, True)

    # assert
    assert result.get_guid() == "payment#1234"
    assert result.get_is_cancelled() is True


@pytest.mark.unit
def test_cancel_invoice(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/cancel_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "forceCancel": False}
    bitpay_client.delete.side_effect = mock_response(
        response, "invoices/" + invoice_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_invoice(invoice_id, False)

    # assert
    assert result.get_guid() == "payment#1234"
    assert result.get_is_cancelled() is True


@pytest.mark.unit
def test_cancel_invoice_by_guid(mocker):
    # arrange
    guid = "12345"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/cancel_invoice_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "forceCancel": False}
    bitpay_client.delete.side_effect = mock_response(
        response, "invoices/guid/" + guid, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_invoice_by_guid(guid, False)

    # assert
    assert result.get_guid() == "payment#1234"
    assert result.get_is_cancelled()


@pytest.mark.unit
def test_request_invoice_notifications(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    response = "success"
    params = {"token": merchant_token_value}
    bitpay_client.post.side_effect = mock_response(
        response, "invoices/" + invoice_id + "/notifications", params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.request_invoice_notifications(invoice_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_create_refund(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    guid = "37bd36bd-6fcb-409c-a907-47f9244302aa"
    params = {
        "token": merchant_token_value,
        "preview": True,
        "reference": "someReference",
        "amount": 10.0,
        "immediate": False,
        "guid": guid,
        "invoiceId": "UZjwcYkWAKfTMn9J1yyfs4",
        "buyerPaysRefundFee": False,
    }
    bitpay_client.post.side_effect = mock_response(response, "refunds", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.create_refund(
        invoice_id, 10.0, True, False, False, "someReference", guid
    )

    # assert
    assert result.get_guid() == guid
    assert result.get_currency() == "USD"
    assert result.get_transaction_currency() == "BTC"
    assert result.get_refund_fee() == 0.03
    assert result.get_buyer_pays_refund_fee() is False


@pytest.mark.unit
def test_get_refund_by_id(mocker):
    # arrange
    refund_id = "WoE46gSLkJQS48RJEiNw3L"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "refunds/" + refund_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_refund(refund_id)

    # assert
    assert result.get_invoice() == "Hpqc63wvE1ZjzeeH4kEycF"
    assert result.get_transaction_currency() == "BTC"
    assert result.get_refund_fee() == 0.04
    assert result.get_buyer_pays_refund_fee() is False


@pytest.mark.unit
def test_get_refund_by_guid(mocker):
    # arrange
    guid = "37bd36bd-6fcb-409c-a907-47f9244302aa"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "refunds/guid/" + guid, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_refund_by_guid(guid)

    # assert
    assert result.get_invoice() == "Hpqc63wvE1ZjzeeH4kEycF"
    assert result.get_transaction_currency() == "BTC"
    assert result.get_refund_fee() == 0.04
    assert result.get_buyer_pays_refund_fee() is False


@pytest.mark.unit
def test_get_refunds(mocker):
    # arrange
    invoice_id = "Hpqc63wvE1ZjzeeH4kEycF"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_refunds_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "invoiceId": invoice_id}
    bitpay_client.get.side_effect = mock_response(response, "refunds", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_refunds(invoice_id)

    # assert
    assert len(result) == 1
    assert result[0].get_id() == "WoE46gSLkJQS48RJEiNw3L"
    assert result[0].get_reference() == "Test refund"


@pytest.mark.unit
def update_refund_by_id(mocker):
    # arrange
    refund_id = "WoE46gSLkJQS48RJEiNw3L"
    status = "complete"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "status": status}
    bitpay_client.update.side_effect = mock_response(
        response, "refunds" + refund_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.update_refund(refund_id, status)

    # assert
    assert result.get_invoice() == "Hpqc63wvE1ZjzeeH4kEycF"
    assert result.get_transaction_currency() == "BTC"
    assert result.get_refund_fee() == 0.04
    assert result.get_buyer_pays_refund_fee() is False


@pytest.mark.unit
def update_refund_by_guid(mocker):
    # arrange
    guid_id = "37bd36bd-6fcb-409c-a907-47f9244302aa"
    status = "complete"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "status": status}
    bitpay_client.update.side_effect = mock_response(
        response, "refunds" + guid_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.update_refund_by_guid(guid_id, status)

    # assert
    assert result.get_invoice() == "Hpqc63wvE1ZjzeeH4kEycF"
    assert result.get_transaction_currency() == "BTC"
    assert result.get_refund_fee() == 0.04
    assert result.get_buyer_pays_refund_fee() is False


@pytest.mark.unit
def test_send_refund_notification(mocker):
    # arrange
    refund_id = "1234"
    bitpay_client = get_bitpay_client(mocker)
    response = {"status": "success"}
    params = {"token": merchant_token_value}
    bitpay_client.post.side_effect = mock_response(
        response, "refunds/" + refund_id + "/notifications", params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.request_refund_notification(refund_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_cancel_refund_by_id(mocker):
    # arrange
    refund_id = "WoE46gSLkJQS48RJEiNw3L"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/cancel_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.delete.side_effect = mock_response(
        response, "refunds/" + refund_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_refund(refund_id)

    # assert
    assert result.get_status() == "cancelled"


@pytest.mark.unit
def test_cancel_refund_by_guid(mocker):
    # arrange
    guid = "12345"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/cancel_refund_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.delete.side_effect = mock_response(
        response, "refunds/guid/" + guid, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_refund_by_guid(guid)

    # assert
    assert result.get_status() == "cancelled"


@pytest.mark.unit
def test_create_bill_by_merchant_facade(mocker):
    # arrange
    bill = get_example_bill()

    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/create_bill_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/create_bill_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.post.side_effect = mock_response(response, "bills", request, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.create_bill(bill)

    # assert
    assert result.get_status() == "draft"
    assert result.get_number() == "bill1234-ABCD"
    assert result.get_cc()[0] == "jane@doe.com"
    assert result.get_id() == "X6KJbe9RxAGWNReCwd1xRw"
    assert result.get_items()[1].get_description() == "Test Item 2"
    assert (
        result.get_token()
        == "qVVgRARN6fKtNZ7Tcq6qpoPBBE3NxdrmdMD883RyMK4Pf8EHENKVxCXhRwyynWveo"
    )


@pytest.mark.unit
def test_create_bill_by_pos_facade(mocker):
    # arrange
    token_container = mocker.Mock(spec=TokenContainer)
    token_container.get_access_token.side_effect = lambda value: {
        Facade.POS: pos_token_value,
    }.get(value)
    bill = get_example_bill()

    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/create_bill_by_pos_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/create_bill_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.post.side_effect = mock_response(response, "bills", request, False)
    client = Client(bitpay_client, token_container, get_guid_generator(mocker))

    # act
    result = client.create_bill(bill, Facade.POS, False)

    # assert
    assert result.get_status() == "draft"
    assert result.get_number() == "bill1234-ABCD"
    assert result.get_cc()[0] == "jane@doe.com"
    assert result.get_id() == "X6KJbe9RxAGWNReCwd1xRw"
    assert result.get_items()[1].get_description() == "Test Item 2"
    assert (
        result.get_token()
        == "qVVgRARN6fKtNZ7Tcq6qpoPBBE3NxdrmdMD883RyMK4Pf8EHENKVxCXhRwyynWveo"
    )


@pytest.mark.unit
def test_get_bill_by_merchant_facade(mocker):
    # arrange
    bill_id = "X6KJbe9RxAGWNReCwd1xRw"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_bill_response.json", "r"
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "bills/" + bill_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_bill(bill_id)

    # assert
    assert result.get_status() == "draft"
    assert result.get_merchant() == "7HyKWn3d4xdhAMQYAEVxVq"
    assert result.get_items()[1].get_id() == "Apy3i2TpzHRYP8tJCkrZMT"
    assert (
        result.get_token()
        == "6EBQR37MgDJPfEiLY3jtRq7eTP2aodR5V5wmXyyZhru5FM5yF4RCGKYQtnT7nhwHjA"
    )


@pytest.mark.unit
def test_get_bill_by_pos_facade(mocker):
    # arrange
    token_container = mocker.Mock(spec=TokenContainer)
    token_container.get_access_token.side_effect = lambda value: {
        Facade.POS: pos_token_value,
    }.get(value)
    bill_id = "X6KJbe9RxAGWNReCwd1xRw"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_bill_response.json", "r"
    ) as file:
        response = json.load(file)
    params = {"token": pos_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "bills/" + bill_id, params, False
    )
    client = Client(bitpay_client, token_container, get_guid_generator(mocker))

    # act
    result = client.get_bill(bill_id, Facade.POS, False)

    # assert
    assert result.get_status() == "draft"
    assert result.get_merchant() == "7HyKWn3d4xdhAMQYAEVxVq"
    assert result.get_items()[1].get_id() == "Apy3i2TpzHRYP8tJCkrZMT"
    assert (
        result.get_token()
        == "6EBQR37MgDJPfEiLY3jtRq7eTP2aodR5V5wmXyyZhru5FM5yF4RCGKYQtnT7nhwHjA"
    )


@pytest.mark.unit
def test_get_bills(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_bills_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(response, "bills", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_bills()

    # assert
    assert len(result) == 2
    assert (
        result[0].get_token()
        == "6EBQR37MgDJPfEiLY3jtRqBMYLg8XSDqhp2kp7VSDqCMHGHnsw4bqnnwQmtehzCvSo"
    )
    assert (
        result[1].get_token()
        == "6EBQR37MgDJPfEiLY3jtRq7eTP2aodR5V5wmXyyZhru5FM5yF4RCGKYQtnT7nhwHjA"
    )
    assert result[0].get_id() == "X6KJbe9RxAGWNReCwd1xRw"
    assert result[1].get_id() == "3Zpmji8bRKxWJo2NJbWX5H"
    assert result[1].get_state() == "VA"


@pytest.mark.unit
def test_get_bills_by_status(mocker):
    # arrange
    status = "draft"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_bills_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "status": status}
    bitpay_client.get.side_effect = mock_response(response, "bills", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_bills(status)

    # assert
    assert len(result) == 2
    assert (
        result[0].get_token()
        == "6EBQR37MgDJPfEiLY3jtRqBMYLg8XSDqhp2kp7VSDqCMHGHnsw4bqnnwQmtehzCvSo"
    )
    assert (
        result[1].get_token()
        == "6EBQR37MgDJPfEiLY3jtRq7eTP2aodR5V5wmXyyZhru5FM5yF4RCGKYQtnT7nhwHjA"
    )
    assert result[0].get_id() == "X6KJbe9RxAGWNReCwd1xRw"
    assert result[1].get_id() == "3Zpmji8bRKxWJo2NJbWX5H"
    assert result[1].get_state() == "VA"


@pytest.mark.unit
def test_update_bill_with_missing_token_should_throws_exception(mocker):
    with pytest.raises(BillUpdateException):
        # arrange
        bill_id = "1234"
        bitpay_client = get_bitpay_client(mocker)
        client = init_client(mocker, bitpay_client)

        # act
        client.update_bill(get_example_bill(), bill_id)


@pytest.mark.unit
def test_update_bill(mocker):
    # arrange
    bill_id = "1234"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/update_bill_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_bill_response.json", "r"
    ) as file:
        response = json.load(file)
    bitpay_client.update.side_effect = mock_response(
        response, "bills/" + bill_id, request, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    bill = get_example_bill()
    bill.set_token("billToken")
    result = client.update_bill(bill, bill_id)

    # assert
    assert result.get_status() == "draft"
    assert result.get_number() == "bill1234-EFGH"
    assert result.get_cc()[0] == "jane@doe.com"
    assert result.get_id() == "X6KJbe9RxAGWNReCwd1xRw"
    assert result.get_items()[1].get_description() == "Test Item 2"
    assert (
        result.get_token()
        == "6EBQR37MgDJPfEiLY3jtRq7eTP2aodR5V5wmXyyZhru5FM5yF4RCGKYQtnT7nhwHjA"
    )


@pytest.mark.unit
def test_deliver_bill_by_merchant_facade(mocker):
    # arrange
    bill_id = "12345"
    bill_token = "someBillToken"
    bitpay_client = get_bitpay_client(mocker)
    params = {"token": bill_token}
    bitpay_client.post.side_effect = mock_response(
        "Success", "bills/" + bill_id + "/deliveries", params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.deliver_bill(bill_id, bill_token)

    # assert
    assert result is True


#
# def test_deliverBill_by_pos_facade(mocker):
#     # arrange
#     bitpay_client = get_bitpay_client(mocker)
#     with open(os.path.abspath(os.path.dirname(__file__)) + '/json/create_invoice_response.json', 'r') as file:
#         response = json.load(file)
#     params = {"token": merchant_token_value}
#     bitpay_client.post.side_effect = mock_response(response, "invoices", params, True)
#     client = init_client(mocker, bitpay_client)
#
#     # act
#     result = client.
#
#     # assert
#     assert
#
#


@pytest.mark.unit
def test_get_rates(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_rates_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.get.side_effect = mock_response(response, "rates", None, False)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_rates()

    # assert
    assert len(result.get_rates()) == 9


@pytest.mark.unit
def test_get_currency_rates_usd(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    response = {"code": "USD", "name": "US Dollar", "rate": 27430}
    bitpay_client.get.side_effect = mock_response(response, "rates/USD", None, False)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_currency_rates("USD")

    # assert
    assert len(result.get_rates()) == 1


@pytest.mark.unit
def test_get_currency_rates_btc(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_rates_bch_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.get.side_effect = mock_response(response, "rates/BCH", None, False)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_currency_rates("BCH")

    # assert
    assert len(result.get_rates()) == 183


@pytest.mark.unit
def test_get_currency_pair_rate(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    response = {"code": "USD", "name": "US Dollar", "rate": 119.11}
    bitpay_client.get.side_effect = mock_response(
        response, "rates/BCH/USD", None, False
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_currency_pair_rate("BCH", "USD")

    # assert
    assert result.get_rate() == 119.11
    assert result.get_name() == "US Dollar"
    assert result.get_code() == "USD"


@pytest.mark.unit
def get_ledger_entries(mocker):
    # arrange
    currency = "USD"
    dateStart = "2021-5-10"
    dateEnd = "2021-5-31"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_ledger_entries_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value, "starDate": dateStart, "endDate": dateEnd}
    bitpay_client.post.side_effect = mock_response(
        response, "ledgers/" + currency, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_ledger_entries(currency, dateStart, dateEnd)

    # assert
    assert len(result) == 3
    assert result[0].get_description() == "20210510_fghij"
    assert result[2].get_type() == "Invoice Refund"
    assert result[2].get_buyer_fields().get_address1() == "2630 Hegal Place"


@pytest.mark.unit
def test_get_ledgers(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_ledgers.json", "r"
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(response, "ledgers", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_ledgers()

    # assert
    assert len(result) == 3
    assert result[1].get_currency() == "USD"
    assert result[1].get_balance() == 2389.82


@pytest.mark.unit
def test_submit_payout_recipients(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/submit_payout_recipients_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/submit_payout_recipients_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.post.side_effect = mock_response(
        response, "recipients", request, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.submit_payout_recipients(get_example_payout_recipients())

    # assert
    assert len(result) == 2
    assert (
        result[0].get_token()
        == "2LVBntm7z92rnuVjVX5ZVaDoUEaoY4LxhZMMzPAMGyXcejgPXVmZ4Ae3oGaCGBFKQf"
    )
    assert result[1].get_status() == "invited"
    assert result[1].get_id() == "X3icwc4tE8KJ5hEPNPpDXW"


@pytest.mark.unit
def test_get_payout_recipients(mocker):
    # arrange
    status = "invited"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_payout_recipients_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {
        "token": payout_token_value,
        "status": status,
        "limit": "100",
        "offset": "0",
    }
    bitpay_client.get.side_effect = mock_response(response, "recipients", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_payout_recipients(status)

    # assert
    assert len(result) == 2
    assert (
        result[0].get_token()
        == "2LVBntm7z92rnuVjVX5ZVaDoUEaoY4LxhZMMzPAMGyXcejgPXVmZ4Ae3oGaCGBFKQf"
    )
    assert (
        result[1].get_token()
        == "2LVBntm7z92rnuVjVX5ZVaDoUEaoY4LxhZMMzPAMGyXrrBAB9vRY3BVxGLbAa6uEx7"
    )


@pytest.mark.unit
def test_get_payout_recipient(mocker):
    # arrange
    recipient_id = "JA4cEtmBxCp5cybtnh1rds"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_payout_recipient_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": payout_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "recipients/" + recipient_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_payout_recipient(recipient_id)

    # assert
    assert result.get_email() == "john.smith@email.com"
    assert result.get_label() == "Bob123"
    assert result.get_status() == "invited"
    assert (
        result.get_token()
        == "2LVBntm7z92rnuVjVX5ZVaDoUEaoY4LxhZMMzPAMGyXcejgPXVmZ4Ae3oGaCGBFKQf"
    )


@pytest.mark.unit
def test_update_payout_recipient(mocker):
    # arrange
    recipient_id = "JA4cEtmBxCp5cybtnh1rds"
    label = "Bob123"
    update_payout_recipient_data = PayoutRecipient()
    update_payout_recipient_data.set_label(label)
    update_payout_recipient_data.set_token(label)
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/update_payout_recipient_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/update_payout_recipient_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.update.side_effect = mock_response(
        response, "recipients/" + recipient_id, request, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.update_payout_recipient(recipient_id, update_payout_recipient_data)

    # assert
    assert result.get_id() == "X3icwc4tE8KJ5hEPNPpDXW"
    assert result.get_email() == "bob@email.com"


@pytest.mark.unit
def test_delete_payout_recipient(mocker):
    # arrange
    recipient_id = "JA4cEtmBxCp5cybtnh1rds"
    bitpay_client = get_bitpay_client(mocker)
    response = {"status": "Success"}
    params = {"token": payout_token_value}
    bitpay_client.delete.side_effect = mock_response(
        response, "recipients/" + recipient_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.delete_payout_recipient(recipient_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_request_payout_recipient_notification(mocker):
    # arrange
    recipient_id = "JA4cEtmBxCp5cybtnh1rds"
    bitpay_client = get_bitpay_client(mocker)
    response = {"status": "Success"}
    params = {"token": payout_token_value}
    url = "recipients/" + recipient_id + "/notifications"
    bitpay_client.post.side_effect = mock_response(response, url, params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.request_payout_recipient_notification(recipient_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_submit_payout(mocker):
    # arrange
    payout = get_example_payout()
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/submit_payout_request.json",
        "r",
    ) as file:
        request = json.load(file)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/submit_payout_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.post.side_effect = mock_response(response, "payouts", request, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.submit_payout(payout)

    # assert
    assert (
        result.get_token()
        == "6RZSTPtnzEaroAe2X4YijenRiqteRDNvzbT8NjtcHjUVd9FUFwa7dsX8RFgRDDC5SL"
    )
    assert result.get_notification_email() == "merchant@email.com"
    assert (
        result.get_notification_url()
        == "https://yournotiticationURL.com/wed3sa0wx1rz5bg0bv97851eqx"
    )
    assert result.get_account_id() == "SJcWZCFq344DL8QnXpdBNM"
    assert result.get_id() == "JMwv8wQCXANoU2ZZQ9a9GH"


@pytest.mark.unit
def test_get_payout(mocker):
    # arrange
    payout_id = "JMwv8wQCXANoU2ZZQ9a9GH"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_payout_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": payout_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "payouts/" + payout_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_payout(payout_id)

    # assert
    assert result.get_recipient_id() == "LDxRZCGq174SF8AnQpdBPB"
    assert result.get_shopper_id() == "7qohDf2zZnQK5Qanj8oyC2"
    assert (
        result.get_notification_url()
        == "https://yournotiticationURL.com/wed3sa0wx1rz5bg0bv97851eqx"
    )
    assert (
        result.get_token()
        == "6RZSTPtnzEaroAe2X4YijenRiqteRDNvzbT8NjtcHjUVd9FUFwa7dsX8RFgRDDC5SL"
    )


@pytest.mark.unit
def test_cancel_payout(mocker):
    # arrange
    payout_id = "1234"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/success_response.json", "r"
    ) as file:
        response = json.load(file)
    params = {"token": payout_token_value}
    bitpay_client.delete.side_effect = mock_response(
        response, "payouts/" + payout_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.cancel_payout(payout_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_get_payouts(mocker):
    # arrange
    startDate = "2021-05-27"
    endDate = "2021-05-31"
    limit = 10
    offset = 1
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/get_payouts.json", "r"
    ) as file:
        response = json.load(file)
    params = {
        "token": payout_token_value,
        "startDate": startDate,
        "endDate": endDate,
        "limit": limit,
        "offset": offset,
    }
    bitpay_client.get.side_effect = mock_response(response, "payouts", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_payouts(startDate, endDate, None, None, limit, offset)

    # assert
    assert len(result) == 2
    assert (
        result[0].get_notification_url()
        == "https://yournotiticationURL.com/wed3sa0wx1rz5bg0bv97851eqx"
    )
    assert result[0].get_status() == "complete"
    assert result[0].get_transactions()[0].get_amount() == 0.000254
    assert (
        result[1].get_token()
        == "9pVLfvdjt59q1JiY2JEsf2hr5FsjimfY4qRLFi85tMiXSCkJ9mQ2oSQqYKVangKaro"
    )


@pytest.mark.unit
def test_request_payout_notification(mocker):
    # arrange
    payout_id = "1234"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/json/success_response.json", "r"
    ) as file:
        response = json.load(file)
    params = {"token": payout_token_value}
    bitpay_client.post.side_effect = mock_response(
        response, "payouts/" + payout_id + "/notifications", params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.request_payout_notification(payout_id)

    # assert
    assert result is True


@pytest.mark.unit
def test_get_settlements(mocker):
    # arrange
    currency = "USD"
    dateStart = "2021-05-10"
    dateEnd = "2021-05-12"
    status = "processing"
    limit = 10
    offset = 0
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_settlements_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {
        "token": merchant_token_value,
        "limit": limit,
        "offset": offset,
        "currency": currency,
        "startDate": dateStart,
        "endDate": dateEnd,
        "status": status,
    }
    bitpay_client.get.side_effect = mock_response(response, "settlements", params, True)
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_settlements(currency, dateStart, dateEnd, status, limit, offset)

    # assert
    assert len(result) == 2
    assert result[0].get_id() == "KBkdURgmE3Lsy9VTnavZHX"
    assert result[0].get_payout_info().get_label() == "Corporate account"
    assert result[0].get_withholdings_sum() == 0
    assert result[0].get_total_amount() == 22.09


@pytest.mark.unit
def test_get_settlement(mocker):
    # arrange
    settlement_id = "DNFnN3fFjjzLn6if5bdGJC"
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_settlement_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": merchant_token_value}
    bitpay_client.get.side_effect = mock_response(
        response, "settlements/" + settlement_id, params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_settlement(settlement_id)

    # assert
    assert result.get_id() == "RPWTabW8urd3xWv2To989v"
    assert result.get_payout_info().get_bank_country() == "Netherlands"
    assert result.get_ledger_entries_sum() == 20.82
    assert result.get_withholdings()[0].get_description() == "Pending Refunds"


@pytest.mark.unit
def test_get_settlement_reconciliation_report(mocker):
    # arrange
    settlement_id = "DNFnN3fFjjzLn6if5bdGJC"
    settlement_token = (
        "5T1T5yGDEtFDYe8jEVBSYLHKewPYXZrDLvZxtXBzn69fBbZYitYQYH4BFYFvvaVU7D"
    )
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_settlement_reconciliation_report_response.json",
        "r",
    ) as file:
        response = json.load(file)
    params = {"token": settlement_token}
    bitpay_client.get.side_effect = mock_response(
        response, "settlements/" + settlement_id + "/reconciliationReport", params, True
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_settlement_reconciliation_report(
        settlement_id, settlement_token
    )

    # assert
    assert result.get_id() == "RvNuCTMAkURKimwgvSVEMP"
    assert result.get_payout_info().get_bank_country() == "Netherlands"
    assert result.get_ledger_entries_sum() == 2956.77
    assert result.get_withholdings()[0].get_description() == "Pending Refunds"
    assert result.get_ledger_entries()[0].get_amount() == 5.83


@pytest.mark.unit
def test_get_supported_wallets(mocker):
    # arrange
    bitpay_client = get_bitpay_client(mocker)
    with open(
        os.path.abspath(os.path.dirname(__file__))
        + "/json/get_supported_wallets_response.json",
        "r",
    ) as file:
        response = json.load(file)
    bitpay_client.get.side_effect = mock_response(
        response, "supportedWallets/", None, False
    )
    client = init_client(mocker, bitpay_client)

    # act
    result = client.get_supported_wallets()

    # assert
    assert len(result) == 7
    assert result[0].get_avatar() == "bitpay-wallet.png"
    assert len(result[0].get_currencies()) == 15
    assert (
        result[0].get_currencies()[0].get_image()
        == "https://bitpay.com/img/icon/currencies/BTC.svg"
    )
