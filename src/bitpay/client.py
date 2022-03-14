"""
Class Client
package Bitpay
author  Antonio Buedo
version 14.3.2203
See bitpay.com/api for more information.
"""
import os
import json

from .config import Config
from .tokens import Tokens
from .models.facade import Facade
from .models.bill.bill import Bill
from .models.Rate.rate import Rate
from .utils.rest_cli import RESTcli
from .models.Rate.rates import Rates
from .models.currency import Currency
from .models.ledger.ledger import Ledger
from .models.wallet.wallet import Wallet
from .models.payout.payout import Payout
from .models.invoice.refund import Refund
from .models.invoice.invoice import Invoice
from .models.payout.payout_batch import PayoutBatch
from .models.ledger.ledger_entry import LedgerEntry
from .models.settlement.settlement import Settlement
from .exceptions.bitpay_exception import BitPayException
from .models.subscription.subscription import Subscription
from .models.payout.payout_recipient import PayoutRecipient
from .models.payout.payout_recipients import PayoutRecipients
from .exceptions.bill_query_exception import BillQueryException
from .exceptions.rate_query_exception import RateQueryException
from .exceptions.bill_update_exception import BillUpdateException
from .exceptions.ledger_query_exception import LedgerQueryException
from .exceptions.wallet_query_exception import WalletQueryException
from .exceptions.refund_query_exception import RefundQueryException
from .exceptions.payout_query_exception import PayoutQueryException
from .exceptions.bill_creation_exception import BillCreationException
from .exceptions.bill_delivery_exception import BillDeliveryException
from .exceptions.refund_update_exception import RefundUpdateException
from .exceptions.invoice_query_exception import InvoiceQueryException
from .exceptions.invoice_update_exception import InvoiceUpdateException
from .exceptions.currency_query_exception import CurrencyQueryException
from .exceptions.refund_creation_exception import RefundCreationException
from .exceptions.payout_creation_exception import PayoutCreationException
from .exceptions.invoice_payment_exception import InvoicePaymentException
from .exceptions.settlement_query_exception import SettlementQueryException
from .exceptions.invoice_creation_exception import InvoiceCreationException
from .exceptions.payoutbatch_query_exception import PayoutBatchQueryException
from .exceptions.subscription_query_exception import SubscriptionQueryException
from .exceptions.subscription_update_exception import SubscriptionUpdateException
from .exceptions.refund_notification_exception import RefundNotificationException
from .exceptions.refund_cancellation_exception import RefundCancellationException
from .exceptions.payout_cancellation_exception import PayoutCancellationException
from .exceptions.payout_notification_exception import PayoutNotificationException
from .exceptions.invoice_cancellation_exception import InvoiceCancellationException
from .exceptions.invoice_notification_exception import InvoiceNotificationException
from .exceptions.payoutbatch_creation_exception import PayoutBatchCreationException
from .exceptions.subscription_creation_exception import SubscriptionCreationException
from .exceptions.payout_recipient_query_exception import PayoutRecipientQueryException
from .exceptions.payout_recipient_update_exception import PayoutRecipientUpdateException
from .exceptions.payoutbatch_cancellation_exception import (
    PayoutBatchCancellationException,
)
from .exceptions.payoutbatch_notification_exception import (
    PayoutBatchNotificationException,
)
from .exceptions.payout_recipient_creation_exception import (
    PayoutRecipientCreationException,
)
from .exceptions.payout_recipient_cancellation_exception import (
    PayoutRecipientCancellationException,
)
from .exceptions.payout_recipient_notification_exception import (
    PayoutRecipientNotificationException,
)


class Client:
    """
    * Class Client
    * @package Bitpay
    * @author  Antonio Buedo
    * @version 3.4.2203
    * See bitpay.com/api for more information.
    """

    __configuration = None
    __env = None
    __ec_key = None
    __token_cache = None
    __currencies_info = []
    __restcli = None

    def __init__(
        self, config_file_path, environment=None, private_key=None, tokens=None
    ):
        try:
            if config_file_path:
                self.build_config_from_file(config_file_path)
                self.init_keys()
                self.init()
            else:
                self.__env = environment
                self.build_config(private_key, tokens)
                self.init_keys()
                self.init()
        except Exception as exe:
            raise BitPayException("failed to initiate client: " + str(exe))

    def build_config_from_file(self, config_file_path: str):
        try:
            self.__configuration = Config()

            if os.path.exists(config_file_path):
                try:
                    read_file = open(config_file_path, "r")
                    json_data = json.loads(read_file.read())
                    self.__env = json_data["BitPayConfiguration"]["Environment"]
                    env_config = json_data["BitPayConfiguration"]["EnvConfig"][
                        self.__env
                    ]
                    read_file.close()
                except Exception as exe:
                    raise BitPayException(
                        "Error when reading configuration file", str(exe)
                    )

                self.__configuration.set_environment(self.__env)
                self.__configuration.set_envconfig({self.__env: env_config})
            else:
                raise BitPayException("Configuration file not found")

        except Exception as exe:
            raise BitPayException("failed to process configuration: " + str(exe))

    def build_config(self, private_key_path: str, tokens: Tokens):
        """
        :param private_key_path: path to private key
        :param tokens: New tokens are provided with each response from the API.
        """
        try:
            self.__configuration = Config()

            if os.path.exists(private_key_path):
                read_file = open(private_key_path, "r")
                plain_private_key = read_file.read()
                self.__ec_key = plain_private_key
                read_file.close()
            else:
                raise BitPayException("Private Key file not found")

            env_config = {
                "PrivateKeyPath": private_key_path,
                "PrivateKey": plain_private_key,
                "ApiTokens": tokens,
            }
            self.__configuration.set_environment(self.__env)
            self.__configuration.set_envconfig({self.__env: env_config})
        except Exception as exe:
            raise BitPayException("failed to process configuration: " + str(exe))

    def init_keys(self):
        if not self.__ec_key:
            try:
                private_key_path = self.__configuration.get_envconfig()[self.__env][
                    "PrivateKeyPath"
                ]
                if os.path.exists(private_key_path):
                    with open(private_key_path) as f:
                        self.__ec_key = f.read()
                else:
                    plain_private_key = self.__configuration.get_envconfig()[
                        self.__env
                    ]["PrivateKey"]
                    if plain_private_key:
                        self.__ec_key = plain_private_key

            except Exception as exe:
                raise BitPayException(
                    "When trying to load private key. Make sure the "
                    "configuration details are correct and the private key"
                    " and tokens are valid: ",
                    str(exe),
                )

    def init(self):
        try:
            proxy = None
            if "proxy" in self.__configuration.get_envconfig()[self.__env]:
                proxy = self.__configuration.get_envconfig()[self.__env]["proxy"]

            self.__restcli = RESTcli(self.__env, self.__ec_key, proxy)
            self.load_access_tokens()
            self.__currencies_info = self.load_currencies()
        except Exception as exe:
            raise BitPayException(
                "failed to deserialize BitPay server response" " (Token array): ",
                str(exe),
            )

    def load_currencies(self):
        try:
            return []
        except BitPayException as exe:
            print(exe)

    def load_access_tokens(self):
        try:
            self.clear_access_token_cache()
            self.__token_cache = self.__configuration.get_envconfig()[self.__env][
                "ApiTokens"
            ]
        except Exception as exe:
            raise BitPayException("When trying to load the tokens: ", str(exe))

    def clear_access_token_cache(self):
        self.__token_cache = Tokens()

    def get_access_token(self, key: str):
        try:
            return self.__token_cache[key]
        except Exception as exe:
            raise BitPayException("There is no token for the specified key: ", str(exe))

    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////

    def create_invoice(
        self, invoice: Invoice, facade: str = Facade.Merchant, sign_request: bool = True
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
        try:
            invoice.set_token(self.get_access_token(facade))
            invoice_json = invoice.to_json()
            response_json = self.__restcli.post("invoices", invoice_json, sign_request)
        except BitPayException as exe:
            raise InvoiceCreationException(
                "failed to serialize Invoice object : " "%s" % str(exe),
                exe.get_api_code(),
            )
        except Exception as exe:
            raise InvoiceCreationException(
                "failed to serialize Invoice object : %s" % str(exe)
            )

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceCreationException(
                "failed to deserialize BitPay server response "
                "(Invoice) : %s" % str(exe)
            )

        return invoice

    def get_invoice(
        self, invoice_id: str, facade: str = Facade.Merchant, sign_request: bool = True
    ) -> Invoice:
        """
        Retrieve a BitPay invoice by invoice id using the specified facade.
        The client must have been previously authorized for the specified
        facade (the public facade requires no authorization)

        :param str invoice_id: The id of the invoice to retrieve
        :param str facade: The facade used to create it
        :param bool sign_request: Signed request
        :return: A BitPay Invoice object
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceQueryException
        """
        try:
            params = {"token": self.get_access_token(facade)}
            response_json = self.__restcli.get(
                "invoices/%s" % invoice_id, params, sign_request
            )
        except BitPayException as exe:
            raise InvoiceQueryException(
                "failed to serialize Invoice object : " "%s" % str(exe),
                exe.get_api_code(),
            )
        except Exception as exe:
            raise InvoiceQueryException(
                "failed to serialize Invoice object :" " %s" % str(exe)
            )

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceQueryException(
                "failed to deserialize BitPay server response"
                " (Invoice) : %s" % str(exe)
            )

        return invoice

    def get_invoices(
        self,
        date_start: str,
        date_end: str,
        status: str = None,
        order_id: str = None,
        limit: int = None,
        offset: int = None,
    ) -> [Invoice]:
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
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "dateStart": date_start,
                "date_end": date_end,
            }
            if status:
                params["status"] = status
            if order_id:
                params["order_id"] = order_id
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset

            response_json = self.__restcli.get("invoices/", parameters=params)
        except BitPayException as exe:
            raise InvoiceQueryException(
                "failed to serialize Invoice object : %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise InvoiceQueryException(
                "failed to serialize Invoice object : %s" % str(exe)
            )

        try:
            invoices = []
            for invoice_data in response_json:
                invoices.append(Invoice(**invoice_data))
        except Exception as exe:
            raise InvoiceQueryException(
                "failed to deserialize BitPay server "
                "response (Invoice) : %s" % str(exe)
            )

        return invoices

    def update_invoice(self, invoice_id: str, buyer_email: str) -> Invoice:
        """
        Update a BitPay invoice with communication method.

        :param str invoice_id: The id of the invoice to updated.
        :param str buyer_email: The buyer's email address.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceUpdateException
        """
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "buyer_email": buyer_email,
            }
            response_json = self.__restcli.update("invoices/%s" % invoice_id, params)
        except BitPayException as exe:
            raise InvoiceUpdateException(
                "failed to serialize Invoice object :" " %s" % str(exe),
                exe.get_api_code(),
            )
        except Exception as exe:
            raise InvoiceUpdateException(
                "failed to serialize Invoice object : %s" % str(exe)
            )

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceUpdateException(
                "failed to deserialize BitPay server response"
                " (Invoice) : %s" % str(exe)
            )

        return invoice

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
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "force_cancel": force_cancel,
            }
            response_json = self.__restcli.delete("invoices/%s" % invoice_id, params)
        except BitPayException as exe:
            raise InvoiceCancellationException(
                "failed to serialize Invoice object : %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise InvoiceCancellationException(
                "failed to serialize Invoice object : %s" % str(exe)
            )

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceCancellationException(
                "failed to deserialize BitPay server"
                " response (Invoice) : %s" % str(exe)
            )
        return invoice

    def pay_invoice(self, invoice_id: str, complete: bool = True) -> Invoice:
        """
        Pay an invoice with a mock transaction.

        :param str invoice_id: The Id of the BitPay invoice.
        :param bool complete: indicate if paid invoice should have status if complete true or a confirmed status.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoicePaymentException
        """
        if self.__env.lower() != "test":
            raise InvoicePaymentException(
                "Pay Invoice method only available in test or demo environments"
            )
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "complete": complete,
            }
            response_json = self.__restcli.update("invoices/pay/%s" % invoice_id, params)
        except BitPayException as exe:
            raise InvoicePaymentException(
                "failed to serialize Invoice object : %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise InvoicePaymentException(
                "failed to serialize Invoice object : %s" % str(exe)
            )

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoicePaymentException(
                "failed to deserialize BitPay server"
                " response (Invoice) : %s" % str(exe)
            )
        return invoice

    def request_invoice_notifications(self, invoice_id: str) -> bool:
        """
        Request a BitPay Invoice Webhook.

        :param str invoice_id: A BitPay invoice ID.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises InvoiceNotificationException
        """
        try:
            invoice = self.get_invoice(invoice_id)
        except Exception as exe:
            raise InvoiceNotificationException(
                f"Invoice with ID: " + {invoice_id} + " Not Found : ", str(exe)
            )
        params = {"token": invoice.get_token()}

        try:
            response_json = self.__restcli.post(
                "invoices/%s" % invoice_id + "/notifications", params
            )
        except Exception as exe:
            raise InvoiceNotificationException(
                "failed to deserialize BitPay server"
                " response (Invoice) : %s" % str(exe)
            )

        return response_json.lower() == "success"

    def create_refund(
        self,
        invoice_id: str,
        amount: float,
        currency: str,
        preview: bool = False,
        immediate: bool = False,
        buyer_pays_refund_fee: bool = False,
    ) -> Refund:
        """
        Create a refund for a BitPay invoice.

        :param str invoice_id: The BitPay invoice Id having the associated refund to be created.
        :param float amount: Amount to be refunded in the currency indicated.
        :param str currency: Reference currency used for the refund, usually the same as the currency
         used to create the invoice.
        :param bool preview: Whether to create the refund request as a preview (which will not be
         acted on until status is updated)
        :param bool immediate: Whether funds should be removed from merchant ledger immediately on
        submission or at time of processing
        :param bool buyer_pays_refund_fee: Whether the buyer should pay the refund fee (default is
        merchant)
        :return: An updated Refund Object
        :rtype: Refund
        :raises BitPayException
        :raises RefundCreationException
        """
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "invoiceId": invoice_id,
                "amount": amount,
                "currency": currency,
                "preview": preview,
                "immediate": immediate,
                "buyerPaysRefundFee": buyer_pays_refund_fee,
            }

            response_json = self.__restcli.post("refunds", params, True)
        except BitPayException as exe:
            raise RefundCreationException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundCreationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundCreationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refund

    def get_refund(self, refund_id: str) -> Refund:
        """
        Retrieve a previously made refund request on a BitPay invoice.

        :param str refund_id: The BitPay refund ID.
        :return: BitPay Refund object with the associated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("refunds/%s" % refund_id, params)
        except BitPayException as exe:
            raise RefundQueryException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundQueryException("failed to serialize refund object : %s" % exe)
        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundQueryException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refund

    def get_refunds(self, invoice_id: str) -> [Refund]:
        """
        Retrieve all refund requests on a BitPay invoice.

        :param str invoice_id: The BitPay invoice object having the associated refunds.
        :return: list of BitPay Refund objects with the associated Refund objects.
        :rtype: [Refund]
        :raises BitPayException
        :raises RefundQueryException
        """
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "invoiceId": invoice_id,
            }
            response_json = self.__restcli.get("refunds", params)
        except BitPayException as exe:
            raise RefundQueryException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundQueryException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            refunds = []
            for refund_data in response_json:
                refunds.append(Refund(**refund_data))
        except Exception as exe:
            raise RefundQueryException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refunds

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
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "status": status}

            response_json = self.__restcli.update("refunds/%s" % refund_id, params)
        except BitPayException as exe:
            raise RefundUpdateException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundUpdateException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundUpdateException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refund

    def cancel_refund(self, refund_id: str) -> Refund:
        """
        Cancel a previously submitted refund request on a BitPay invoice.

        :param str refund_id: The refund Id for the refund to be canceled.
        :return: Cancelled refund Object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundCancellationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.delete("refunds/%s" % refund_id, params)
        except BitPayException as exe:
            raise RefundCancellationException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundCancellationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundCancellationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refund

    def request_refund_notification(self, refund_id: str) -> bool:
        """
        Send a refund notification.

        :param str refund_id: BitPay refund ID to notify.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises RefundNotificationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.post(
                "refunds/%s" % refund_id + "/notifications", params, True
            )
        except BitPayException as exe:
            raise RefundNotificationException(
                "failed to serialize refund object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise RefundNotificationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            result = response_json["status"].lower() == "success"
        except Exception as exe:
            raise RefundNotificationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return result

    def get_supported_wallets(self) -> [Wallet]:
        """
        Retrieve all supported wallets.

        :return: A list of wallet objets.
        :rtype: [Wallet]
        :raises BitPayException
        :raises WalletQueryException
        """
        try:
            response_json = self.__restcli.get("supportedWallets/", None, False)
        except BitPayException as exe:
            raise WalletQueryException(
                "failed to serialize wallet object :  %s" % str(exe), exe.get_api_code()
            )
        except Exception as exe:
            raise WalletQueryException(
                "failed to serialize wallet object : %s" % str(exe)
            )

        try:
            wallets = []
            for wallet in response_json:
                wallets.append(Wallet(**wallet))
        except Exception as exe:
            raise WalletQueryException(
                "failed to deserialize BitPay server response (Wallet) : %s" % str(exe)
            )

        return wallets

    def create_bill(
        self, bill: Bill, facade: str = Facade.Merchant, sign_request: bool = True
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
        try:
            bill.set_token(self.get_access_token(facade))
            response_json = self.__restcli.post("bills", bill.to_json(), sign_request)
        except BitPayException as exe:
            raise BillCreationException(
                "failed to serialize bill object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillCreationException(
                "failed to deserialize BitPay server response (Bill) : %s" % str(exe)
            )

        return bill

    def get_bills(self, status: str = None) -> [Bill]:
        """
        Retrieve a collection of BitPay bills.

        :param str status: The status to filter the bills.
        :return: A list of BitPay Bill objects.
        :rtype: [Bill]
        :raises BitPayException
        :raises BillQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            if status:
                params["status"] = status
            response_json = self.__restcli.get("bills", params, True)
        except BitPayException as exe:
            raise BillQueryException(
                "failed to serialize bill object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            bills = []
            for bill_data in response_json:
                bills.append(Bill(**bill_data))
        except Exception as exe:
            raise BillQueryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )

        return bills

    def get_bill(self, bill_id: str) -> Bill:
        """
        Retrieve a BitPay bill by bill id using the specified facade.

        :param str bill_id: The id of the bill to retrieve.
        :return: A BitPay Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("bills/%s" % bill_id, params)
        except BitPayException as exe:
            raise BillQueryException(
                "failed to serialize bill object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillQueryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )
        return bill

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
        try:
            response_json = self.__restcli.update("bills/%s" % bill_id, bill.to_json())
        except BitPayException as exe:
            raise BillUpdateException(
                "failed to serialize bill object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillUpdateException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )
        return bill

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
        try:
            params = {"token": bill_token}
            response_json = self.__restcli.post(
                "bills/%s" % bill_id + "/deliveries", params
            )
        except BitPayException as exe:
            raise BillDeliveryException(
                "failed to serialize bill object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            result = response_json
        except Exception as exe:
            raise BillDeliveryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )
        return result

    def get_ledger(
        self, currency: str, start_date: str, end_date: str
    ) -> [LedgerEntry]:
        """
        Retrieve a list of ledgers by date range using the merchant facade.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str start_date: The first date for the query filter.
        :param str end_date: The last date for the query filter.
        :return: A LedgerEntry object populated with the BitPay ledger entries list.
        :rtype: [LedgerEntry]
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}

            if currency:
                params["currency"] = currency

            if start_date:
                params["startDate"] = start_date

            if end_date:
                params["endDate"] = end_date

            response_json = self.__restcli.get("ledgers/%s" % currency, params)
        except BitPayException as exe:
            raise LedgerQueryException(
                "failed to serialize Ledger object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(LedgerEntry(**ledger))
        except Exception as exe:
            raise LedgerQueryException(
                "failed to deserialize BitPay server response "
                "(Ledger) : %s" % str(exe)
            )
        return ledgers

    def get_ledgers(self) -> [Ledger]:
        """
        Retrieve a list of ledgers using the merchant facade.

        :return: A list of Ledger objects populated with the currency and
        current balance of each one.
        :rtype [Ledger]
        :raises BitPayException
        :raises LedgerQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("ledgers", params)
        except BitPayException as exe:
            raise LedgerQueryException(
                "failed to serialize Ledger object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(Ledger(**ledger))
        except Exception as exe:
            raise LedgerQueryException(
                "failed to deserialize BitPay server response"
                " (Ledger) : %s" % str(exe)
            )
        return ledgers

    def submit_payout_recipients(
        self, recipients: PayoutRecipients
    ) -> [PayoutRecipient]:
        """
        Submit BitPay Payout Recipients.

        :param PayoutRecipient recipients:
        :return: A PayoutRecipients object with request parameters defined.
        :rtype: [PayoutRecipient]
        :raises BitPayException
        :raises PayoutRecipientCreationException
        """
        try:
            recipients.set_token(self.get_access_token(Facade.Payout))

            response_json = self.__restcli.post(
                "recipients", recipients.to_json(), True
            )
        except BitPayException as exe:
            raise PayoutRecipientCreationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            recipients = []
            for recipient in response_json:
                recipients.append(PayoutRecipient(**recipient))
        except Exception as exe:
            raise PayoutRecipientCreationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return recipients

    def get_payout_recipient(self, recipient_id: str) -> PayoutRecipient:
        """
        Retrieve a BitPay payout recipient by batch id using.The client must have been
        previously authorized for the payout facade.

        :param str recipient_id: The id of the recipient to retrieve.
        :return: A BitPay PayoutRecipient object.
        :rtype: PayoutRecipient
        :raises BitPayException
        :raises PayoutRecipientQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.get("recipients/%s" % recipient_id, params)
        except BitPayException as exe:
            raise PayoutRecipientQueryException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_recipient = PayoutRecipient(**response_json)
        except Exception as exe:
            raise PayoutRecipientQueryException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return payout_recipient

    def get_payout_recipients(
        self, status: str = None, limit: int = 100, offset: int = 0
    ) -> [PayoutRecipient]:
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
        try:
            params = {
                "token": self.get_access_token(Facade.Payout),
                "limit": str(limit),
                "offset": str(offset),
            }
            if status:
                params["status"] = status

            response_json = self.__restcli.get("recipients", params)
        except BitPayException as exe:
            raise PayoutRecipientQueryException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_recipients = []
            for payout_recipient in response_json:
                payout_recipients.append(PayoutRecipient(**payout_recipient))
        except Exception as exe:
            raise PayoutRecipientQueryException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return payout_recipients

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
        try:
            recipient.set_token(self.get_access_token(Facade.Payout))
            response_json = self.__restcli.update(
                "recipients/%s" % recipient_id, recipient.to_json()
            )
        except BitPayException as exe:
            raise PayoutRecipientUpdateException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_recipient = PayoutRecipient(**response_json)
        except Exception as exe:
            raise PayoutRecipientUpdateException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return payout_recipient

    def delete_payout_recipient(self, recipient_id: str) -> bool:
        """
        Cancel a BitPay Payout recipient.

        :param str recipient_id: The id of the recipient to cancel.
        :return: True if the delete operation was successfull, false otherwise.
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
        except BitPayException as exe:
            raise PayoutRecipientCancellationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )
        try:
            response_json = self.__restcli.delete(
                "recipients/%s" % recipient_id, params
            )
        except Exception as exe:
            raise PayoutRecipientCancellationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return response_json["status"].lower() == "success"

    def request_payout_recipient_notification(self, recipient_id: str) -> bool:
        """
        Send a payout recipient notification

        :param str recipient_id: The id of the recipient to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype bool
        :raises BitPayException
        :raises PayoutRecipientNotificationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
        except BitPayException as exe:
            raise PayoutRecipientNotificationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            response_json = self.__restcli.post(
                "recipients/%s" % recipient_id + "/notifications", params
            )
        except Exception as exe:
            raise PayoutRecipientNotificationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return response_json["status"].lower() == "success"

    def submit_payout(self, payout: Payout) -> Payout:
        """
        Submit a BitPay Payout.

        :param Payout payout: A Payout object with request parameters defined.
        :return: A BitPay generated Payout object.
        :rtype: Payout
        :raises BitPayException
        :raises PayoutCreationException
        """
        try:
            payout.set_token(self.get_access_token(Facade.Payout))
            response_json = self.__restcli.post("payouts", payout.to_json(), True)
        except BitPayException as exe:
            raise PayoutCreationException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutCreationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout

    def get_payout(self, payout_id: str) -> Payout:
        """
        Retrieve a BitPay payout by payout id using.The client must have been
        previously authorized for the payout facade.

        :param str payout_id: The id of the payout to retrieve.
        :return: A BitPay generated Payout object.
        :rtype Payout
        :raises BitPayException
        :raises PayoutQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.get("payouts/%s" % payout_id, params)
        except BitPayException as exe:
            raise PayoutQueryException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutQueryException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout

    def get_payouts(
        self,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        reference: str = None,
        limit: int = None,
        offset: int = None,
    ) -> [Payout]:
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
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            if start_date:
                params["startDate"] = start_date
            if end_date:
                params["endDate"] = end_date
            if status:
                params["status"] = status
            if reference:
                params["reference"] = reference
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset

            response_json = self.__restcli.get("payouts", params)
        except BitPayException as exe:
            raise PayoutQueryException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payouts = []
            for payout in response_json:
                payouts.append(Payout(**payout))
        except Exception as exe:
            raise PayoutQueryException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payouts

    def cancel_payout(self, payout_id: str) -> bool:
        """
        Cancel a BitPay Payout.

        :param str payout_id: The id of the payout to cancel.
        :return: True if payout was successfully canceled, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutCancellationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.delete("payouts/%s" % payout_id, params)
        except BitPayException as exe:
            raise PayoutCancellationException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutCancellationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout

    def request_payout_notification(self, payout_id: str) -> bool:
        """
        Send a payout notification

        :param str payout_id: The id of the payout to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutNotificationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.post(
                "payouts/%s" % payout_id + "/notifications", params
            )
        except BitPayException as exe:
            raise PayoutNotificationException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutNotificationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout

    def submit_payout_batch(self, batch: PayoutBatch) -> PayoutBatch:
        """
        Submit a BitPay Payout batch.

        :param PayoutBatch batch: A PayoutBatch object with request parameters defined.
        :return: A BitPay generated PayoutBatch object.
        :rtype PayoutBatch
        :raises BitPayException
        :raises PayoutBatchCreationException
        """
        try:
            batch.set_token(self.get_access_token(Facade.Payout))

            response_json = self.__restcli.post("payoutBatches", batch.to_json(), True)
        except BitPayException as exe:
            raise PayoutBatchCreationException(
                "failed to serialize PayoutBatch object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_batch = PayoutBatch(**response_json)
        except Exception as exe:
            raise PayoutBatchCreationException(
                "failed to deserialize BitPay server response "
                " (PayoutBatch) : %s" % str(exe)
            )
        return payout_batch

    def get_payout_batch(self, payout_batch_id: str) -> PayoutBatch:
        """
        Retrieve a BitPay payout batch by batch id using.
        The client must have been previously authorized for the payout facade.

        :param str payout_batch_id: The id of the payout batch to retrieve.
        :return: A BitPay PayoutBatch object.
        :rtype: PayoutBatch
        :raises BitPayException
        :raises PayoutBatchQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.get(
                "payoutBatches/%s" % payout_batch_id, params
            )
        except BitPayException as exe:
            raise PayoutBatchQueryException(
                "failed to serialize Payout object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            payout_batch = PayoutBatch(**response_json)
        except Exception as exe:
            raise PayoutBatchQueryException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout_batch

    def get_payout_batches(
        self,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        limit: int = None,
        offset: int = None,
    ) -> [PayoutBatch]:
        """
        Retrieve a collection of BitPay payout batches.

        :param str start_date: The start date for the query.
        :param str end_date: The end date for the query.
        :param str status: The status to filter (optional).
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Offset for paging
        :return: A list of BitPay PayoutBatch objects.
        :rtype: PayoutBatch
        :raises BitPayException
        :raises PayoutBatchQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            if start_date:
                params["startDate"] = start_date
            if end_date:
                params["endDate"] = end_date
            if status:
                params["status"] = status
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset

            response_json = self.__restcli.get("payoutBatches", params)
        except BitPayException as exe:
            raise PayoutBatchQueryException(
                "failed to serialize PayoutBatch object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_batches = []
            for payout_batch in response_json:
                payout_batches.append(PayoutBatch(**payout_batch))
        except Exception as exe:
            raise PayoutBatchQueryException(
                "failed to deserialize BitPay server response "
                " (PayoutBatch) : %s" % str(exe)
            )
        return payout_batches

    def cancel_payout_batch(self, payout_batch_id: str) -> bool:
        """
        Cancel a BitPay Payout batch.

        :param str payout_batch_id: The id of the payout batch to cancel.
        :return: True if the refund was successfully canceled, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutBatchCancellationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.delete(
                "payoutBatches/%s" % payout_batch_id, params
            )
        except BitPayException as exe:
            raise PayoutBatchCancellationException(
                "failed to serialize PayoutBatch object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_batch = PayoutBatch(**response_json)
        except Exception as exe:
            raise PayoutBatchCancellationException(
                "failed to deserialize BitPay server response "
                " (PayoutBatch) : %s" % str(exe)
            )
        return payout_batch

    def request_payout_batch_notification(self, payout_batch_id: str) -> bool:
        """
        Send a payout batch notification

        :param str payout_batch_id: The id of the payout batch to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutBatchNotificationException
        """
        try:
            params = {"token": self.get_access_token(Facade.Payout)}
            response_json = self.__restcli.post(
                "payoutBatches/%s" % payout_batch_id + "/notifications", params
            )
        except BitPayException as exe:
            raise PayoutBatchNotificationException(
                "failed to serialize PayoutBatch object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            payout_batch = PayoutBatch(**response_json)
        except Exception as exe:
            raise PayoutBatchNotificationException(
                "failed to deserialize BitPay server response "
                " (PayoutBatch) : %s" % str(exe)
            )
        return payout_batch

    def get_settlements(
        self,
        currency: str,
        date_start: str,
        date_end: str,
        status: str,
        limit: int = 100,
        offset: int = 0,
    ) -> [Settlement]:
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
        try:
            params = {
                "token": self.get_access_token(Facade.Merchant),
                "dateStart": date_start,
                "dateEnd": date_end,
                "currency": currency,
                "status": status,
                "limit": limit,
                "offset": offset,
            }
            response_json = self.__restcli.get("settlements", params)
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlements = []
            for settlement in response_json:
                settlements.append(Settlement(**settlement))
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlements

    def get_settlement(self, settlement_id: str) -> Settlement:
        """
        Retrieves a summary of the specified settlement.

        :param str settlement_id: Settlement Id
        :return: A BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("settlements/%s" % settlement_id, params)
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlement

    def get_settlement_reconciliation_report(
        self, settlement: Settlement
    ) -> Settlement:
        """
        Gets a detailed reconciliation report of the activity within the settlement period

        :param Settlement settlement: Settlement to generate report for.
        :return: A detailed BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        try:
            params = {"token": settlement.get_token()}
            response_json = self.__restcli.get(
                "settlements/%s" % settlement.get_id() + "/reconciliationReport", params
            )
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlement

    def create_subscription(self, subscription: Subscription) -> Subscription:
        """
        Create a BitPay Subscription.

        :param Subscription subscription: A Subscription object with request parameters defined.
        :return: A BitPay generated Subscription object.
        :rtype: Subscription
        :raises BitPayException
        :raises SubscriptionCreationException
        """
        try:
            subscription.set_token(self.get_access_token(Facade.Merchant))

            response_json = self.__restcli.post(
                "subscriptions", subscription.to_json(), True
            )
        except BitPayException as exe:
            raise SubscriptionCreationException(
                "failed to serialize Subscription object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            subscription = Subscription(**response_json)
        except Exception as exe:
            raise SubscriptionCreationException(
                "failed to deserialize BitPay server response "
                " (Subscription) : %s" % str(exe)
            )
        return subscription

    def get_subscription(self, subscription_id: str) -> Subscription:
        """
        Retrieve a BitPay subscription by subscription id using the specified facade.

        :param subscription_id: The id of the subscription to retrieve.
        :return: A BitPay Subscription object.
        :rtype: Subscription
        :raises BitPayException
        :raises SubscriptionQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get(
                "subscriptions/%s" % subscription_id, params
            )
        except BitPayException as exe:
            raise SubscriptionQueryException(
                "failed to serialize Subscription object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            subscription = Subscription(**response_json)
        except Exception as exe:
            raise SubscriptionQueryException(
                "failed to deserialize BitPay server response "
                " (Subscription) : %s" % str(exe)
            )
        return subscription

    def get_subscriptions(self, status: str = None) -> [Subscription]:
        """
        Retrieve a collection of BitPay subscriptions.

        :param str|None status: The status to filter the subscriptions.
        :return: A list of BitPay Subscription objects.
        :rtype: [Subscription]
        :raises BitPayException
        :raises SubscriptionQueryException
        """
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            if status:
                params["status"] = status
            response_json = self.__restcli.get("subscriptions", params)
        except BitPayException as exe:
            raise SubscriptionQueryException(
                "failed to serialize Subscription object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            subscriptions = []
            for subscription in response_json:
                subscriptions.append(Subscription(**subscription))
        except Exception as exe:
            raise SubscriptionQueryException(
                "failed to deserialize BitPay server response "
                " (Subscription) : %s" % str(exe)
            )
        return subscriptions

    def update_subscription(
        self, subscription: Subscription, subscription_id
    ) -> Subscription:
        """
        Update a BitPay Subscription.

        :param Subscription subscription: A Subscription object with the parameters to update defined.
        :param str subscription_id: The Id of the Subscription to update.
        :return: An updated Subscription object.
        :rtype: Subscription
        :raises BitPayException
        :raises SubscriptionUpdateException
        """
        try:
            subscription_token = self.get_subscription(
                subscription.get_id()
            ).get_token()
            subscription.set_token(subscription_token)

            response_json = self.__restcli.update(
                "subscriptions/%s" % subscription_id, subscription.to_json()
            )
        except BitPayException as exe:
            raise SubscriptionUpdateException(
                "failed to serialize Subscription object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            subscription = Subscription(**response_json)
        except Exception as exe:
            raise SubscriptionUpdateException(
                "failed to deserialize BitPay server response "
                " (Subscription) : %s" % str(exe)
            )
        return subscription

    def get_currencies(self) -> [Currency]:
        """
        Fetch the supported currencies.

        :return: A list of BitPay Invoice objects.
        :rtype: [Currency]
        :raises BitPayException
        :raises CurrencyQueryException
        """
        try:
            response_json = self.__restcli.get("currencies", None, False)
        except BitPayException as exe:
            raise CurrencyQueryException(
                "failed to serialize Currency object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            currencies = []
            for currency in response_json:
                currencies.append(Currency(**currency))
        except Exception as exe:
            raise CurrencyQueryException(
                "failed to deserialize BitPay server response "
                " (Currency) : %s" % str(exe)
            )
        return currencies

    def get_rates(self) -> [Rates]:
        """
        Retrieve the exchange rate table maintained by BitPay.  See https://bitpay.com/bitcoin-exchange-rates.

        :return: A Rates object populated with the BitPay exchange rate table.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__restcli.get("rates", None, False)
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            rates = []
            for rate in response_json:
                rates.append(Rate(**rate))
            rates = Rates(rates, self)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (Rates) : %s" % str(exe)
            )
        return rates

    def get_currency_rates(self, base_currency: str) -> [Rates]:
        """
        Retrieve all the rates for a given cryptocurrency

        :param str base_currency: The cryptocurrency for which you want to fetch the rates.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :return: A Rates object populated with the currency rates for the requested baseCurrency.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__restcli.get("rates/%s" % base_currency, None, False)
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            rates = []
            for rate in response_json:
                rates.append(Rate(**rate))
            rates = Rates(rates, self)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (Rates) : %s" % str(exe)
            )
        return rates

    def get_currency_pair_rate(self, base_currency: str, currency: str) -> Rate:
        """
        Retrieve the rate for a cryptocurrency / fiat pair

        :param str base_currency: The cryptocurrency for which you want to fetch the fiat-equivalent rate.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :param str currency: The fiat currency for which you want to fetch the baseCurrency rate
        :return: A Rate object populated with the currency rate for the requested baseCurrency.
        :rtype: Rate
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__restcli.get(
                "rates/%s" % base_currency + "/%s" % currency, None, False
            )
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe), exe.get_api_code()
            )

        try:
            rate = Rate(**response_json)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (Rate) : %s" % str(exe)
            )
        return rate
