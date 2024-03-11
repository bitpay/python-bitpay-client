import os
import json
from typing import List, Optional

from bitpay.clients.bill_client import BillClient
from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.currency_client import CurrencyClient
from bitpay.clients.invoice_client import InvoiceClient
from bitpay.clients.ledger_client import LedgerClient
from bitpay.clients.payout_client import PayoutClient
from bitpay.clients.payout_recipient_client import PayoutRecipientClient
from bitpay.clients.rate_client import RateClient
from bitpay.clients.refund_client import RefundClient
from bitpay.clients.settlement_client import SettlementClient
from bitpay.clients.wallet_client import WalletClient
from .config import Config
from .environment import Environment
from .exceptions.bitpay_exception_provider import BitPayExceptionProvider
from .exceptions.bitpay_generic_exception import BitPayGenericException
from .models.facade import Facade
from .models.bill.bill import Bill
from .models.invoice.invoice_event_token import InvoiceEventToken
from .models.payout.payout_group import PayoutGroup
from .models.rate.rate import Rate
from .utils.guid_generator import GuidGenerator
from .models.rate.rates import Rates
from .models.currency import Currency
from .models.ledger.ledger import Ledger
from .models.wallet.wallet import Wallet
from .models.payout.payout import Payout
from .models.invoice.refund import Refund
from .models.invoice.invoice import Invoice
from .models.ledger.ledger_entry import LedgerEntry
from .models.settlement.settlement import Settlement
from .exceptions.bitpay_exception import BitPayException
from .models.payout.payout_recipient import PayoutRecipient
from .models.payout.payout_recipients import PayoutRecipients
from .utils.token_container import TokenContainer


class Client:
    __bitpay_client: BitPayClient
    __token_container: TokenContainer
    __guid_generator: GuidGenerator

    def __init__(
        self,
        bitpay_client: BitPayClient,
        token_container: TokenContainer,
        guid_generator: Optional[GuidGenerator] = None,
    ) -> None:
        try:
            self.__bitpay_client = bitpay_client
            self.__token_container = token_container
            if guid_generator is None:
                guid_generator = GuidGenerator()
            self.__guid_generator = guid_generator
        except Exception as exe:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "failed to initiate clients: " + str(exe)
            )

    @staticmethod
    def create_pos_client(pos_token: str, environment: Environment = Environment.PROD):  # type: ignore
        token_container = TokenContainer()
        token_container.add_pos(pos_token)

        bitpay_client = BitPayClient(Client.get_base_url(environment))

        return Client(bitpay_client, token_container, GuidGenerator())

    @staticmethod
    def create_client(  # type: ignore
        private_key_or_private_key_path: str,
        token_container: TokenContainer,
        environment: Environment = Environment.PROD,
        proxy: Optional[str] = None,
    ):
        """
        :raises BitPayGenericException
        """
        try:
            base_url = Client.get_base_url(environment)
            ec_key = Client.get_ec_key(private_key_or_private_key_path)
            bitpay_client = BitPayClient(base_url, ec_key, proxy)
            guid_generator = GuidGenerator()

            return Client(bitpay_client, token_container, guid_generator)
        except Exception as exe:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "failed to process configuration: " + str(exe)
            )

    @staticmethod
    def create_client_by_config_file_path(config_file_path: str):  # type: ignore
        """
        :raises BitPayGenericException
        """
        if not os.path.exists(config_file_path):
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "Configuration file not found"
            )

        try:
            with open(config_file_path, "r") as read_file:
                json_data = json.loads(read_file.read())

            environment = json_data["BitPayConfiguration"]["Environment"]
            config = json_data["BitPayConfiguration"]["EnvConfig"][environment]
            proxy = config["proxy"]
            private_key_path = config["PrivateKeyPath"]
            if private_key_path is None:
                private_key_or_private_key_path = config["PrivateKey"]
            else:
                private_key_or_private_key_path = private_key_path

            token_container = TokenContainer()
            token_container.add_pos(config["ApiTokens"].get("pos", None))
            token_container.add_merchant(config["ApiTokens"].get("merchant", None))
            token_container.add_payout(config["ApiTokens"].get("payout", None))

            if "test" == environment.lower():
                environment = Environment.TEST
            else:
                environment = Environment.PROD

            return Client.create_client(
                private_key_or_private_key_path, token_container, environment, proxy
            )
        except Exception as exe:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "Error when reading configuration file. " + str(exe)
            )

    @staticmethod
    def get_ec_key(private_key_or_private_key_path: Optional[str]) -> str:
        """
        :raises BitPayGenericException
        """
        if private_key_or_private_key_path is None:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "Private Key file not found"
            )
            raise BitPayGenericException("Private Key file not found")

        if os.path.exists(private_key_or_private_key_path):
            with open(private_key_or_private_key_path, "r") as read_file:
                return read_file.read()

        return private_key_or_private_key_path

    @staticmethod
    def get_base_url(environment: Environment) -> str:
        return (
            Config.TEST_URL.value
            if environment == environment.TEST
            else Config.PROD_URL.value
        )

    def get_access_token(self, facade: Facade) -> str:
        """
        :raises BitPayGenericException
        """
        try:
            return self.__token_container.get_access_token(facade)
        except Exception as exe:
            message = "There is no token for the specified key: " + facade.value
            BitPayExceptionProvider.throw_generic_exception_with_message(message)
            raise BitPayGenericException(message)

    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////

    def create_invoice(
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
        :raises BitPayException
        :raises InvoiceCreationException
        """
        client = self.create_invoice_client()

        return client.create(invoice, facade, sign_request)

    def get_invoice(
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
        :raises BitPayException
        :raises InvoiceQueryException
        """
        client = self.create_invoice_client()
        return client.get(invoice_id, facade, sign_request)

    def get_invoice_by_guid(
        self, guid: str, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Invoice:
        """
        Retrieve a BitPay invoice by invoice id using the specified facade.
        The clients must have been previously authorized for the specified
        facade (the public facade requires no authorization)

        :param str guid: The id of the invoice to retrieve
        :param str facade: The facade used to create it
        :param bool sign_request: Signed request
        :return: A BitPay Invoice object
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceQueryException
        """
        client = self.create_invoice_client()
        return client.get_by_guid(guid, facade, sign_request)

    def get_invoices(
        self,
        date_start: str,
        date_end: str,
        status: Optional[str] = None,
        order_id: Optional[str] = None,
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
        :raises BitPayException
        :raises InvoiceQueryException
        """
        client = self.create_invoice_client()
        return client.get_invoices(
            date_start, date_end, status, order_id, limit, offset
        )

    def get_invoice_event_token(self, invoice_id: str) -> InvoiceEventToken:
        """
        Retrieves a bus token which can be used to subscribe to invoice events.

        :param str invoice_id: The id of the invoice for which you want to fetch an event token.
        :return: Invoice Event Token.
        :rtype: InvoiceEventToken
        :raises BitPayException
        :raises InvoiceQueryException
        """
        client = self.create_invoice_client()
        return client.get_event_token(invoice_id)

    def update_invoice(
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
        :raises BitPayException
        :raises InvoiceUpdateException
        """
        client = self.create_invoice_client()
        return client.update(invoice_id, buyer_email, buyer_sms, sms_code)

    def cancel_invoice(self, invoice_id: str, force_cancel: bool = False) -> Invoice:
        """
        Delete a previously created BitPay invoice.

        :param str invoice_id: The Id of the BitPay invoice to be canceled.
        :param bool force_cancel: Query param that will cancel the invoice even if
        no contact information is present
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceCancellationException
        """
        client = self.create_invoice_client()
        return client.cancel(invoice_id, force_cancel)

    def cancel_invoice_by_guid(self, guid: str, force_cancel: bool = False) -> Invoice:
        """
        Delete a previously created BitPay invoice.

        :param str guid: The GUID of the BitPay invoice to be canceled.
        :param bool force_cancel: Query param that will cancel the invoice even if
        no contact information is present
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceCancellationException
        """
        client = self.create_invoice_client()
        return client.cancel_by_guid(guid, force_cancel)

    def pay_invoice(self, invoice_id: str, status: str = "complete") -> Invoice:
        """
        Pay an invoice with a mock transaction - it works only for test environment.

        :param str invoice_id: The Id of the BitPay invoice.
        :param bool status: indicate if paid invoice should have status if complete true or a confirmed status.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoicePaymentException
        """
        client = self.create_invoice_client()
        return client.pay(invoice_id, status)

    def request_invoice_notifications(self, invoice_id: str) -> bool:
        """
        Request a BitPay Invoice Webhook.

        :param str invoice_id: A BitPay invoice ID.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises InvoiceNotificationException
        """
        client = self.create_invoice_client()
        return client.request_invoice_notifications(invoice_id)

    def create_refund(
        self,
        invoice_id: str,
        amount: float,
        preview: bool = False,
        immediate: bool = False,
        buyer_pays_refund_fee: bool = False,
        reference: Optional[str] = None,
        guid: Optional[str] = None,
    ) -> Refund:
        """
        Create a refund for a BitPay invoice.

        :param str invoice_id: The BitPay invoice Id having the associated refund to be created.
        :param float amount: Amount to be refunded in the currency indicated.
        :param bool preview: Whether to create the refund request as a preview (which will not be
         acted on until status is updated)
        :param bool immediate: Whether funds should be removed from merchant ledger immediately on
        submission or at time of processing
        :param bool buyer_pays_refund_fee: Whether the buyer should pay the refund fee (default is
        merchant)
        :param str reference: Present only if specified in the request to create the refund.
        This is your reference label for this refund. It will be passed-through on each response for you to identify
        the refund in your system. Maximum string length is 100 characters.
        :param str guid: Variable provided by the merchant and designed to be used by the merchant
        to correlate the refund with a refund ID in their system.
        :return: An updated Refund Object
        :rtype: Refund
        :raises BitPayException
        :raises RefundCreationException
        """
        client = self.create_refund_client()
        return client.create(
            invoice_id,
            amount,
            preview,
            immediate,
            buyer_pays_refund_fee,
            reference,
            guid,
        )

    def get_refund(self, refund_id: str) -> Refund:
        """
        Retrieve a previously made refund request on a BitPay invoice.

        :param str refund_id: The BitPay refund ID.
        :return: BitPay Refund object with the associated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundQueryException
        """
        client = self.create_refund_client()
        return client.get(refund_id)

    def get_refund_by_guid(self, guid: str) -> Refund:
        """
        Retrieve a previously made refund request on a BitPay invoice.

        :param str guid: The BitPay refund GUID.
        :return: BitPay Refund object with the associated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundQueryException
        """
        client = self.create_refund_client()
        return client.get_by_guid(guid)

    def get_refunds(self, invoice_id: str) -> List[Refund]:
        """
        Retrieve all refund requests on a BitPay invoice.

        :param str invoice_id: The BitPay invoice object having the associated refunds.
        :return: list of BitPay Refund objects with the associated Refund objects.
        :rtype: [Refund]
        :raises BitPayException
        :raises RefundQueryException
        """
        client = self.create_refund_client()
        return client.get_refunds(invoice_id)

    def update_refund(self, refund_id: str, status: str) -> Refund:
        """
        Update the status of a BitPay invoice refund.

        :param str refund_id: BitPay refund ID.
        :param str status: The new status for the refund to be updated
        :return: A BitPay generated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundUpdateException
        """
        client = self.create_refund_client()
        return client.update(refund_id, status)

    def update_refund_by_guid(self, refund_guid: str, status: str) -> Refund:
        """
        Update the status of a BitPay invoice refund.

        :param str refund_guid: BitPay refund GUID.
        :param str status: The new status for the refund to be updated
        :return: A BitPay generated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundUpdateException
        """
        client = self.create_refund_client()
        return client.update_by_guid(refund_guid, status)

    def cancel_refund(self, refund_id: str) -> Refund:
        """
        Cancel a previously submitted refund request on a BitPay invoice.

        :param str refund_id: The refund Id for the refund to be canceled.
        :return: Cancelled refund Object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundCancellationException
        """
        client = self.create_refund_client()
        return client.cancel(refund_id)

    def cancel_refund_by_guid(self, guid: str) -> Refund:
        """
        Cancel a previously submitted refund request on a BitPay invoice.

        :param str guid: The refund GUID for the refund to be canceled.
        :return: Cancelled refund Object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundCancellationException
        """
        client = self.create_refund_client()
        return client.cancel_by_guid(guid)

    def request_refund_notification(self, refund_id: str) -> bool:
        """
        Send a refund notification.

        :param str refund_id: BitPay refund ID to notify.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises RefundNotificationException
        """
        client = self.create_refund_client()
        return client.request_notification(refund_id)

    def get_supported_wallets(self) -> List[Wallet]:
        """
        Retrieve all supported wallets.

        :return: A list of wallet objets.
        :rtype: [Wallet]
        :raises BitPayException
        :raises WalletQueryException
        """
        client = self.create_wallet_client()
        return client.get_supported_wallets()

    def create_bill(
        self, bill: Bill, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Bill:
        """
        Create a BitPay Bill.

        :param Bill bill: A Bill object with request parameters defined.
        :param str facade: The facade used to create it.
        :param bool sign_request: Signed request.
        :return: A BitPay generated Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillCreationException
        """
        client = self.create_bill_client()
        return client.create(bill, facade, sign_request)

    def get_bills(self, status: Optional[str] = None) -> List[Bill]:
        """
        Retrieve a collection of BitPay bills.

        :param str status: The status to filter the bills.
        :return: A list of BitPay Bill objects.
        :rtype: [Bill]
        :raises BitPayException
        :raises BillQueryException
        """
        client = self.create_bill_client()
        return client.get_bills(status)

    def get_bill(
        self, bill_id: str, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Bill:
        """
        Retrieve a BitPay bill by bill id using the specified facade.

        :param str bill_id: The id of the bill to retrieve.
        :param str facade: The facade used to create it.
        :param bool sign_request: Signed request.
        :return: A BitPay Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillQueryException
        """
        client = self.create_bill_client()
        return client.get(bill_id, facade, sign_request)

    def update_bill(self, bill: Bill, bill_id: str) -> Bill:
        """
        Update a BitPay Bill.

        :param Bill bill: A Bill object with the parameters to update defined.
        :param str bill_id: The Id of the Bill to update.
        :return: An updated Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillUpdateException
        """
        client = self.create_bill_client()
        return client.update(bill, bill_id)

    def deliver_bill(self, bill_id: str, bill_token: str) -> bool:
        """
        Deliver a BitPay Bill.

        :param str bill_id: The id of the requested bill.
        :param str bill_token: The token of the requested bill.
        :return: A response status returned from the API.
        :rtype: bool
        :raises BitPayException
        :raises BillDeliveryException
        """
        client = self.create_bill_client()
        return client.deliver(bill_id, bill_token)

    def get_ledger_entries(
        self, currency: str, start_date: str, end_date: str
    ) -> List[LedgerEntry]:
        """
        Retrieve a list of ledgers by date range using the merchant facade.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str start_date: The first date for the query filter.
        :param str end_date: The last date for the query filter.
        :return: A LedgerEntry object populated with the BitPay ledger entries list.
        :rtype: [LedgerEntry]
        """
        client = self.create_ledger_client()
        return client.get_entries(currency, start_date, end_date)

    def get_ledgers(self) -> List[Ledger]:
        """
        Retrieve a list of ledgers using the merchant facade.

        :return: A list of Ledger objects populated with the currency and
        current balance of each one.
        :rtype [Ledger]
        :raises BitPayException
        :raises LedgerQueryException
        """
        client = self.create_ledger_client()
        return client.get_ledgers()

    def submit_payout_recipients(
        self, recipients: PayoutRecipients
    ) -> List[PayoutRecipient]:
        """
        Submit BitPay Payout Recipients.

        :param PayoutRecipient recipients:
        :return: A PayoutRecipients object with request parameters defined.
        :rtype: [PayoutRecipient]
        :raises BitPayException
        :raises PayoutRecipientCreationException
        """
        client = self.create_payout_recipient_client()
        return client.submit(recipients)

    def get_payout_recipient(self, recipient_id: str) -> PayoutRecipient:
        """
        Retrieve a BitPay payout recipient by batch id using.The clients must have been
        previously authorized for the payout facade.

        :param str recipient_id: The id of the recipient to retrieve.
        :return: A BitPay PayoutRecipient object.
        :rtype: PayoutRecipient
        :raises BitPayException
        :raises PayoutRecipientQueryException
        """
        client = self.create_payout_recipient_client()
        return client.get(recipient_id)

    def get_payout_recipients(
        self, status: Optional[str] = None, limit: int = 100, offset: int = 0
    ) -> List[PayoutRecipient]:
        """
        Retrieve a collection of BitPay Payout Recipients.

        :param str status: The recipient status you want to query on.
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Offset for paging
        :return: A list of BitPayRecipient objects.
        :rtype: [PayoutRecipient]
        :raises BitPayException
        :raises PayoutRecipientQueryException
        """
        client = self.create_payout_recipient_client()
        return client.get_recipients(status, limit, offset)

    def update_payout_recipient(
        self, recipient_id: str, recipient: PayoutRecipient
    ) -> PayoutRecipient:
        """
        Update a Payout Recipient.

        :param str recipient_id: The recipient id for the recipient to be updated.
        :param str recipient: A PayoutRecipient object with updated parameters defined.
        :return: The updated recipient object.
        :rtype: PayoutRecipient
        :raises BitPayException
        :raises PayoutRecipientUpdateException
        """
        client = self.create_payout_recipient_client()
        return client.update(recipient_id, recipient)

    def delete_payout_recipient(self, recipient_id: str) -> bool:
        """
        Cancel a BitPay Payout recipient.

        :param str recipient_id: The id of the recipient to cancel.
        :return: True if the delete operation was successful, false otherwise.
        """
        client = self.create_payout_recipient_client()
        return client.delete(recipient_id)

    def request_payout_recipient_notification(self, recipient_id: str) -> bool:
        """
        Send a payout recipient notification

        :param str recipient_id: The id of the recipient to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype bool
        :raises BitPayException
        :raises PayoutRecipientNotificationException
        """
        client = self.create_payout_recipient_client()
        return client.request_notification(recipient_id)

    def submit_payout(self, payout: Payout) -> Payout:
        """
        Submit a BitPay Payout.

        :param Payout payout: A Payout object with request parameters defined.
        :return: A BitPay generated Payout object.
        :rtype: Payout
        :raises BitPayException
        :raises PayoutCreationException
        """
        client = self.create_payout_client()
        return client.submit(payout)

    def get_payout(self, payout_id: str) -> Payout:
        """
        Retrieve a BitPay payout by payout id using.The clients must have been
        previously authorized for the payout facade.

        :param str payout_id: The id of the payout to retrieve.
        :return: A BitPay generated Payout object.
        :rtype Payout
        :raises BitPayException
        :raises PayoutQueryException
        """
        client = self.create_payout_client()
        return client.get(payout_id)

    def get_payouts(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[str] = None,
        reference: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[Payout]:
        """
        Retrieve a collection of BitPay payouts.

        :param str start_date: The start date for the query.
        :param str end_date: The end date for the query.
        :param str status: The status to filter (optional).
        :param str reference: The optional reference specified at payout request creation.
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Offset for paging
        :return: A list of BitPay Payout objects.
        :rtype [Payout]
        :raises BitPayException
        :raises PayoutQueryException
        """
        client = self.create_payout_client()
        return client.get_payouts(
            start_date,
            end_date,
            status,
            reference,
            limit,
            offset,
        )

    def cancel_payout(self, payout_id: str) -> bool:
        """
        Cancel a BitPay Payout.

        :param str payout_id: The id of the payout to cancel.
        :return: True if payout was successfully canceled, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutCancellationException
        """
        client = self.create_payout_client()
        return client.cancel(payout_id)

    def request_payout_notification(self, payout_id: str) -> bool:
        """
        Send a payout notification

        :param str payout_id: The id of the payout to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutNotificationException
        """
        client = self.create_payout_client()
        return client.request_notification(payout_id)

    def create_payout_group(self, payouts: List[Payout]) -> PayoutGroup:
        """
        Submit a BitPay Payouts. See https://developer.bitpay.com/reference/create-payout-group

        :param List[Payout] payouts: Payouts to create
        :return: PayoutGroup
        :raises BitPayException
        """
        client = self.create_payout_client()
        return client.create_group(payouts)

    def cancel_payout_group(self, group_id: str) -> PayoutGroup:
        """
        Cancel a BitPay Payouts. See https://developer.bitpay.com/reference/cancel-a-payout-group

        :param group_id The the groupId of the collection of payouts you want to cancel.
        :return: PayoutGroup
        :raises BitPayException
        """
        client = self.create_payout_client()
        return client.cancel_group(group_id)

    def get_settlements(
        self,
        currency: Optional[str] = None,
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> List[Settlement]:
        """
        Retrieves settlement reports for the calling merchant filtered by query. The `limit`
        and `offset` parameters specify pages for large query sets.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str date_start: The start date for the query.
        :param str date_end: The end date for the query.
        :param str status: Can be `processing`, `completed`, or `failed`.
        :param int limit: Maximum number of settlements to retrieve.
        :param int offset: Offset for paging
        :return: A list of BitPay Settlement objects
        :rtype: [Settlement]
        :raises BitPayException
        :raises SettlementQueryException
        """
        client = self.create_settlement_client()
        return client.get_settlements(
            currency,
            date_start,
            date_end,
            status,
            limit,
            offset,
        )

    def get_settlement(self, settlement_id: str) -> Settlement:
        """
        Retrieves a summary of the specified settlement.

        :param str settlement_id: Settlement Id
        :return: A BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        client = self.create_settlement_client()
        return client.get(settlement_id)

    def get_settlement_reconciliation_report(
        self, settlement_id: str, settlement_token: str
    ) -> Settlement:
        """
        Gets a detailed reconciliation report of the activity within the settlement period

        :param str settlement_id: Settlement id to generate report for.
        :param str settlement_token: Settlement token to generate report for.
        :return: A detailed BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        client = self.create_settlement_client()
        return client.get_reconciliation_report(settlement_id, settlement_token)

    def get_currencies(self) -> dict:
        """
        Fetch the supported currencies.

        :return: A list of BitPay Invoice objects.
        :rtype: [Currency]
        :raises BitPayException
        :raises CurrencyQueryException
        """
        client = self.create_currency_client()
        return client.get_currencies()

    def get_rates(self) -> Rates:
        """
        Retrieve the exchange rate table maintained by BitPay.  See https://bitpay.com/bitcoin-exchange-rates.

        :return: A Rates object populated with the BitPay exchange rate table.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        client = self.create_rate_client()
        return client.get_rates()

    def get_currency_rates(self, base_currency: str) -> Rates:
        """
        Retrieve all the rates for a given cryptocurrency

        :param str base_currency: The cryptocurrency for which you want to fetch the rates.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :return: A Rates object populated with the currency rates for the requested baseCurrency.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        client = self.create_rate_client()
        return client.get_currency_rates(base_currency)

    def get_currency_pair_rate(self, base_currency: str, currency: str) -> Rate:
        """
        Retrieve the rate for a cryptocurrency / fiat pair

        :param str base_currency: The cryptocurrency for which you want to fetch the fiat-equivalent rate.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :param str currency: The fiat currency for which you want to fetch the baseCurrency rate
        :return: A rate object populated with the currency rate for the requested baseCurrency.
        :rtype: Rate
        :raises BitPayException
        :raises RateQueryException
        """
        client = self.create_rate_client()
        return client.get_currency_pair_rate(base_currency, currency)

    def create_bill_client(self) -> BillClient:
        return BillClient(self.__bitpay_client, self.__token_container)

    def create_currency_client(self) -> CurrencyClient:
        return CurrencyClient(self.__bitpay_client)

    def create_invoice_client(self) -> InvoiceClient:
        return InvoiceClient(
            self.__bitpay_client, self.__token_container, self.__guid_generator
        )

    def create_ledger_client(self) -> LedgerClient:
        return LedgerClient(self.__bitpay_client, self.__token_container)

    def create_payout_client(self) -> PayoutClient:
        return PayoutClient(self.__bitpay_client, self.__token_container)

    def create_payout_recipient_client(self) -> PayoutRecipientClient:
        return PayoutRecipientClient(
            self.__bitpay_client, self.__token_container, self.__guid_generator
        )

    def create_rate_client(self) -> RateClient:
        return RateClient(self.__bitpay_client)

    def create_refund_client(self) -> RefundClient:
        """
        :return: RateClient
        """
        return RefundClient(
            self.__bitpay_client, self.__token_container, self.__guid_generator
        )

    def create_settlement_client(self) -> SettlementClient:
        return SettlementClient(self.__bitpay_client, self.__token_container)

    def create_wallet_client(self) -> WalletClient:
        return WalletClient(self.__bitpay_client)
