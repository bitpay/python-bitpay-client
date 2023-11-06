from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.facade import Facade
from bitpay.models.invoice.invoice import Invoice
from bitpay.models.invoice.invoice_event_token import InvoiceEventToken
from bitpay.utils.guid_generator import GuidGenerator
from bitpay.utils.token_container import TokenContainer


class InvoiceClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer
    __guid_generator = GuidGenerator

    def __init__(
        self,
        bitpay_client: BitPayClient,
        token_container: TokenContainer,
        guid_generator: GuidGenerator,
    ):
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container
        self.__guid_generator = guid_generator

    def create(
        self,
        invoice: Invoice,
        facade: Facade = Facade.MERCHANT,
        sign_request: bool = True,
    ) -> Invoice:
        """
        Create a BitPay invoice

        :param Invoice invoice: An Invoice object with request parameters defined
        :param str facade: The facade used to create it
        :param str sign_request: Signed request
        :return: A BitPay generated Invoice object
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """

        if invoice.guid is None:
            invoice.guid = self.__guid_generator.execute()

        invoice.token = self.__token_container.get_access_token(facade)
        invoice_json = invoice.to_json()
        response = self.__bitpay_client.post("invoices", invoice_json, sign_request)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )

        return invoice

    def get(
        self,
        invoice_id: str,
        facade: Facade = Facade.MERCHANT,
        sign_request: bool = True,
    ) -> Invoice:
        """
        Retrieve a BitPay invoice by invoice id using the specified facade.
        The clients must have been previously authorized for the specified
        facade (the public facade requires no authorization)

        :param str invoice_id: The id of the invoice to retrieve
        :param str facade: The facade used to create it
        :param bool sign_request: Signed request
        :return: A BitPay Invoice object
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(facade)}
        response = self.__bitpay_client.get(
            "invoices/%s" % invoice_id, params, sign_request
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def get_by_guid(
        self, guid: str, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Invoice:
        """
        Retrieve a BitPay invoice by invoice id using the specified facade.
        The clients must have been previously authorized for the specified
        facade (the public facade requires no authorization)

        :param str guid: The GUID of the invoice to retrieve
        :param str facade: The facade used to create it
        :param bool sign_request: Signed request
        :return: A BitPay Invoice object
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(facade)}
        response = self.__bitpay_client.get(
            "invoices/guid/%s" % guid, params, sign_request
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def get_invoices(
        self,
        date_start: str,
        date_end: str,
        status: Optional[int] = None,
        order_id: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[Invoice]:
        """
        Retrieve a collection of BitPay invoices.

        :param str date_start: The first date for the query filter.
        :param str date_end: The last date for the query filter.
        :param str status: The invoice status you want to query on.
        :param str order_id: The optional order id specified at time of invoice creation.
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Number of results to offset
        (ex. skip 10 will give you results starting with the 11th)
        :return: A list of BitPay Invoice objects.
        :rtype: [Invoice]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "dateStart": date_start,
            "dateEnd": date_end,
        }
        if status:
            params["status"] = status
        if order_id:
            params["orderId"] = order_id
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset

        response = self.__bitpay_client.get("invoices/", params, True)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoices = []
            for invoice_data in response_json:
                invoices.append(Invoice(**invoice_data))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoices

    def update(
        self,
        invoice_id: str,
        buyer_email: Optional[str] = None,
        buyer_sms: Optional[str] = None,
        sms_code: Optional[str] = None,
    ) -> Invoice:
        """
        Update a BitPay invoice with communication method.

        :param str invoice_id: The id of the invoice to updated.
        :param str buyer_email: The buyer's email address.
        :param str buyer_sms: The buyer's cell number.
        :param str sms_code: The buyer's received verification code.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}

        if buyer_email is not None:
            params["buyerEmail"] = buyer_email

        if buyer_sms is not None:
            params["buyerSms"] = buyer_sms

        if sms_code is not None:
            params["smsCode"] = sms_code

        response = self.__bitpay_client.update("invoices/%s" % invoice_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def cancel(self, invoice_id: str, force_cancel: bool = False) -> Invoice:
        """
        Delete a previously created BitPay invoice.

        :param str invoice_id: The Id of the BitPay invoice to be canceled.
        :param bool force_cancel: Query param that will cancel the invoice even if
        no contact information is present
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "forceCancel": force_cancel,
        }
        response = self.__bitpay_client.delete("invoices/%s" % invoice_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def cancel_by_guid(self, guid: str, force_cancel: bool = False) -> Invoice:
        """
        Delete a previously created BitPay invoice.

        :param str guid: The GUID of the BitPay invoice to be canceled.
        :param bool force_cancel: Query param that will cancel the invoice even if
        no contact information is present
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "forceCancel": force_cancel,
        }
        response = self.__bitpay_client.delete("invoices/guid/%s" % guid, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def get_event_token(self, invoice_id: str) -> InvoiceEventToken:
        """
        Retrieves a bus token which can be used to subscribe to invoice events.

        :param str invoice_id: The id of the invoice for which you want to fetch an event token.
        :return: Invoice Event Token.
        :rtype: InvoiceEventToken
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
        }
        response = self.__bitpay_client.get(
            "invoices/%s/events" % invoice_id, params, True
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return InvoiceEventToken(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

    def pay(self, invoice_id: str, status: str) -> Invoice:
        """
        Pay an invoice with a mock transaction - it works only for test environment.

        :param str invoice_id: The Id of the BitPay invoice.
        :param bool status: indicate if paid invoice should have status if complete true or a confirmed status.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "status": status,
        }
        response = self.__bitpay_client.update("invoices/pay/%s" % invoice_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Invoice", str(exe)
            )
            raise

        return invoice

    def request_invoice_notifications(self, invoice_id: str) -> bool:
        """
        Request a BitPay Invoice Webhook.

        :param str invoice_id: A BitPay invoice ID.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
        response = self.__bitpay_client.post(
            "invoices/%s" % invoice_id + "/notifications", params
        )
        response_json = ResponseParser.response_to_json_string(response)

        return response_json.lower() == "success"
