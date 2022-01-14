"""
Class Client
package Bitpay
author  Antonio Buedo
version 1.0.0
See bitpay.com/api for more information.
"""
import os
import json

from .config import Config
from .exceptions.invoice_creation_exception import InvoiceCreationException
from .tokens import Tokens
from .models.facade import Facade
from .models.bill.bill import Bill
from .utils.rest_cli import RESTcli
from .models.ledger.ledger import Ledger
from .models.wallet.wallet import Wallet
from .models.invoice.refund import Refund
from .models.invoice.invoice import Invoice
from .models.ledger.ledger_entry import LedgerEntry
from .exceptions.bitpay_exception import BitPayException
from .exceptions.bill_query_exception import BillQueryException
from .exceptions.bill_update_exception import BillUpdateException
from .exceptions.ledger_query_exception import LedgerQueryException
from .exceptions.wallet_query_exception import WalletQueryException
from .exceptions.refund_query_exception import RefundQueryException
from .exceptions.bill_creation_exception import BillCreationException
from .exceptions.bill_delivery_exception import BillDeliveryException
from .exceptions.refund_update_exception import RefundUpdateException
from .exceptions.invoice_query_exception import InvoiceQueryException
from .exceptions.invoice_update_exception import InvoiceUpdateException
from .exceptions.refund_creation_exception import RefundCreationException
from .exceptions.refund_notification_exception import RefundNotificationException
from .exceptions.refund_cancellation_exception import RefundCancellationException
from .exceptions.invoice_cancellation_exception import InvoiceCancellationException
from .exceptions.invoice_notification_exception import InvoiceNotificationException


class Client:
    """
     * Class Client
     * @package Bitpay
     * @author  Antonio Buedo
     * @version 1.0.0
     * See bitpay.com/api for more information.
    """
    __configuration = None
    __env = None
    __ec_key = None
    __token_cache = None
    __currencies_info = []
    __restcli = None

    def __init__(self, config_file_path, environment=None, private_key=None, tokens=None):
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
                    read_file = open(config_file_path, 'r')
                    json_data = json.loads(read_file.read())
                    self.__env = json_data['BitPayConfiguration']['Environment']
                    env_config = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]
                    read_file.close()
                except Exception as exe:
                    raise BitPayException("Error when reading configuration file", str(exe))

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
                read_file = open(private_key_path, 'r')
                plain_private_key = read_file.read()
                self.__ec_key = plain_private_key
            else:
                raise BitPayException("Private Key file not found")

            env_config = {
                "PrivateKeyPath": private_key_path,
                "PrivateKey": plain_private_key,
                "ApiTokens": tokens
            }
            self.__configuration.set_environment(self.__env)
            self.__configuration.set_envconfig({self.__env: env_config})
        except Exception as exe:
            raise BitPayException("failed to process configuration: " + str(exe))

    def init_keys(self):
        if not self.__ec_key:
            try:
                private_key_path = self.__configuration.get_envconfig()[self.__env]["PrivateKeyPath"]
                if os.path.exists(private_key_path):
                    with open(private_key_path) as f:
                        self.__ec_key = f.read()
                else:
                    plain_private_key = self.__configuration.get_envconfig()[self.__env]["PrivateKey"]
                    if plain_private_key:
                        self.__ec_key = plain_private_key

            except Exception as exe:
                raise BitPayException("When trying to load private key. Make sure the "
                                      "configuration details are correct and the private key"
                                      " and tokens are valid: ", str(exe))

    def init(self):
        try:
            proxy = self.__configuration.get_envconfig()[self.__env]["proxy"]
            self.__restcli = RESTcli(self.__env, self.__ec_key, proxy)
            self.load_access_tokens()
            self.__currencies_info = self.load_currencies()
        except Exception as exe:
            raise BitPayException("failed to deserialize BitPay server response"
                                  " (Token array): ", str(exe))

    def load_currencies(self):
        try:
            return []
        except BitPayException as exe:
            print(exe)

    def load_access_tokens(self):
        try:
            self.clear_access_token_cache()
            self.__token_cache = self.__configuration.get_envconfig()[self.__env]["ApiTokens"]
        except Exception as exe:
            raise BitPayException("When trying to load the tokens: ", str(exe))

    def clear_access_token_cache(self):
        self.__token_cache = Tokens()

    def get_access_token(self, key: str):
        try:
            return self.__token_cache[key]
        except Exception as exe:
            raise BitPayException("There is no token for the specified key: "
                                  , str(exe))

    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////

    def create_invoice(self, invoice: Invoice, facade: str = Facade.Merchant,
                       sign_request: bool = True) -> Invoice:
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
            raise InvoiceCreationException("failed to serialize Invoice object : "
                                           "%s" % str(exe), exe.get_api_code())
        except Exception as exe:
            raise InvoiceCreationException("failed to serialize Invoice object : %s" % str(exe))

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceCreationException("failed to deserialize BitPay server response "
                                           "(Invoice) : %s" % str(exe))

        return invoice

    def get_invoice(self, invoice_id: str, facade: str = Facade.Merchant,
                    sign_request: bool = True) -> Invoice:
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
            response_json = self.__restcli.get("invoices/%s" % invoice_id, params, sign_request)
        except BitPayException as exe:
            raise InvoiceQueryException("failed to serialize Invoice object : "
                                        "%s" % str(exe), exe.get_api_code())
        except Exception as exe:
            raise InvoiceQueryException("failed to serialize Invoice object :"
                                        " %s" % str(exe))

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceQueryException("failed to deserialize BitPay server response"
                                        " (Invoice) : %s" % str(exe))

        return invoice

    def get_invoices(self, date_start: str, date_end: str, status: str = None,
                     order_id: str = None, limit: int = None,
                     offset: int = None) -> [Invoice]:
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
            params = {"token": self.get_access_token(Facade.Merchant),
                      "dateStart": date_start, "date_end": date_end}
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
            raise InvoiceQueryException("failed to serialize Invoice object : %s"
                                        % str(exe), exe.get_api_code())
        except Exception as exe:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(exe))

        try:
            invoices = []
            for invoice_data in response_json:
                invoices.append(Invoice(**invoice_data))
        except Exception as exe:
            raise InvoiceQueryException("failed to deserialize BitPay server "
                                        "response (Invoice) : %s" % str(exe))

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
            params = {'token': self.get_access_token(Facade.Merchant),
                      'buyer_email': buyer_email}
            response_json = self.__restcli.update("invoices/%s" % invoice_id, params)
        except BitPayException as exe:
            raise InvoiceUpdateException("failed to serialize Invoice object :"
                                         " %s" % str(exe), exe.get_api_code())
        except Exception as exe:
            raise InvoiceUpdateException("failed to serialize Invoice object : %s" % str(exe))

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceUpdateException("failed to deserialize BitPay server response"
                                         " (Invoice) : %s" % str(exe))

        return invoice

    def cancel_invoice(self, invoice_id: str) -> Invoice:
        """
        Delete a previously created BitPay invoice.

        :param str invoice_id: The Id of the BitPay invoice to be canceled.
        :return: A BitPay generated Invoice object.
        :rtype: Invoice
        :raises BitPayException
        :raises InvoiceCancellationException
        """
        try:
            params = {'token': self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.delete("invoices/%s" % invoice_id, params)
        except BitPayException as exe:
            raise InvoiceCancellationException("failed to serialize Invoice object : %s" % str(exe),
                                               exe.get_api_code())
        except Exception as exe:
            raise InvoiceCancellationException("failed to serialize Invoice object : %s" % str(exe))

        try:
            invoice = Invoice(**response_json)
        except Exception as exe:
            raise InvoiceCancellationException("failed to deserialize BitPay server"
                                               " response (Invoice) : %s" % str(exe))
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
            raise InvoiceNotificationException(f"Invoice with ID: " + {invoice_id} + " Not Found : ",
                                               str(exe))
        params = {"token": invoice.get_token()}

        try:
            response_json = self.__restcli.post("invoices/%s" % invoice_id + "/notifications", params)
        except Exception as exe:
            raise InvoiceNotificationException("failed to deserialize BitPay server"
                                               " response (Invoice) : %s" % str(exe))

        return response_json.lower() == "success"

    def create_refund(self, invoice_id: str, amount: float, currency: str, preview: bool = False,
                      immediate: bool = False, buyer_pays_refund_fee: bool = False) -> Refund:
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
            params = {"token": self.get_access_token(Facade.Merchant),
                      "invoiceId": invoice_id, "amount": amount,
                      "currency": currency, "preview": preview, "immediate": immediate,
                      "buyerPaysRefundFee": buyer_pays_refund_fee}

            response_json = self.__restcli.post("refunds", params, True)
        except BitPayException as exe:
            raise RefundCreationException("failed to serialize refund object :  %s" % str(exe),
                                          exe.get_api_code())
        except Exception as exe:
            raise RefundCreationException("failed to serialize refund object : %s" % str(exe))

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundCreationException("failed to deserialize BitPay server response"
                                          " (Refund) : %s" % str(exe))

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
            raise RefundQueryException("failed to serialize refund object :  %s" % str(exe),
                                       exe.get_api_code())
        except Exception as exe:
            raise RefundQueryException("failed to serialize refund object : %s" % exe)
        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundQueryException("failed to deserialize BitPay server response"
                                       " (Refund) : %s" % str(exe))

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
            params = {"token": self.get_access_token(Facade.Merchant), "invoiceId": invoice_id}
            response_json = self.__restcli.get("refunds", params)
        except BitPayException as exe:
            raise RefundQueryException("failed to serialize refund object :  %s" % str(exe),
                                       exe.get_api_code())
        except Exception as exe:
            raise RefundQueryException("failed to serialize refund object : %s" % str(exe))

        try:
            # refunds = Refund(**response_json)
            refunds = []
            for refund_data in response_json:
                refunds.append(Invoice(**refund_data))
        except Exception as exe:
            raise RefundQueryException("failed to deserialize BitPay server response"
                                       " (Refund) : %s" % str(exe))

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
            raise RefundUpdateException("failed to serialize refund object :  %s" % str(exe),
                                        exe.get_api_code())
        except Exception as exe:
            raise RefundUpdateException("failed to serialize refund object : %s" % str(exe))

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundUpdateException("failed to deserialize BitPay server response"
                                        " (Refund) : %s" % str(exe))

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
            raise RefundCancellationException("failed to serialize refund object :  %s" % str(exe),
                                              exe.get_api_code())
        except Exception as exe:
            raise RefundCancellationException("failed to serialize refund object : %s" % str(exe))

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundCancellationException("failed to deserialize BitPay server response"
                                              " (Refund) : %s" % str(exe))

        return refund

    #  TODO
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
            response_json = self.__restcli.post("refunds/%s" % refund_id + "/notifications", params, True)
        except BitPayException as exe:
            raise RefundNotificationException("failed to serialize refund object :  %s" % str(exe),
                                              exe.get_api_code())
        except Exception as exe:
            raise RefundNotificationException("failed to serialize refund object : %s" % str(exe))

        try:
            refund = Refund(**response_json)
        except Exception as exe:
            raise RefundNotificationException("failed to deserialize BitPay server response"
                                              " (Refund) : %s" % str(exe))

        return refund

    def get_supported_wallets(self) -> [Wallet]:
        """
        Retrieve all supported wallets.

        :return: A list of wallet objets.
        :rtype: [Wallet]
        :raises BitPayException
        :raises WalletQueryException
        """
        try:
            response_json = self.__restcli.get("supportedWallets/", None)
        except BitPayException as exe:
            raise WalletQueryException("failed to serialize wallet object :  %s" % str(exe),
                                       exe.get_api_code())
        except Exception as exe:
            raise WalletQueryException("failed to serialize wallet object : %s" % str(exe))

        try:
            wallet = Wallet(**response_json)
        except Exception as exe:
            raise WalletQueryException("failed to deserialize BitPay server response (Wallet) : %s" % str(exe))

        return wallet

    def create_bill(self, bill: Bill, facade: str = Facade.Merchant,
                    sign_request: bool = True) -> Bill:
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
            bill.get_token(self.get_access_token(facade))
            response_json = self.__restcli.post("bills", bill, sign_request)
        except BitPayException as exe:
            raise BillCreationException("failed to serialize bill object :  %s" % str(exe),
                                        exe.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillCreationException("failed to deserialize BitPay server response (Bill) : %s" % str(exe))

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
            raise BillQueryException("failed to serialize bill object :  %s" % str(exe),
                                     exe.get_api_code())

        try:
            bills = Bill(**response_json)
        except Exception as exe:
            raise BillQueryException("failed to deserialize BitPay server response"
                                     " (Bill) : %s" % str(exe))

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
            raise BillQueryException("failed to serialize bill object :  %s" % str(exe),
                                     exe.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillQueryException("failed to deserialize BitPay server response"
                                     " (Bill) : %s" % str(exe))
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
            response_json = self.__restcli.update("bills/%s" % bill_id, bill)
        except BitPayException as exe:
            raise BillUpdateException("failed to serialize bill object :  %s" % str(exe),
                                      exe.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillUpdateException("failed to deserialize BitPay server response"
                                      " (Bill) : %s" % str(exe))
        return bill

    #  TODO
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
            params = {
                "token": bill_token
            }
            response_json = self.__restcli.post("bills/%s" % bill_id + "/deliveries", params)
        except BitPayException as exe:
            raise BillDeliveryException("failed to serialize bill object :  %s" % str(exe),
                                        exe.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as exe:
            raise BillDeliveryException("failed to deserialize BitPay server response"
                                        " (Bill) : %s" % str(exe))
        return bill

    def get_ledger(self, currency: str, start_date: str, end_date: str) -> [Ledger]:
        """
        Retrieve a list of ledgers by date range using the merchant facade.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str start_date: The first date for the query filter.
        :param str end_date: The last date for the query filter.
        :return: A Ledger object populated with the BitPay ledger entries list.
        :rtype: [Ledger]
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
            raise LedgerQueryException("failed to serialize Ledger object :  %s" % str(exe),
                                       exe.get_api_code())

        try:
            ledger = LedgerEntry(**response_json)
        except Exception as exe:
            raise LedgerQueryException("failed to deserialize BitPay server response "
                                       "(Ledger) : %s" % str(exe))
        return ledger

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
            raise LedgerQueryException("failed to serialize Ledger object :  %s" % str(exe),
                                       exe.get_api_code())

        try:
            ledgers = Ledger(**response_json)
        except Exception as exe:
            raise LedgerQueryException("failed to deserialize BitPay server response"
                                       " (Ledger) : %s" % str(exe))
        return ledgers
