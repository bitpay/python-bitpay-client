import os
import json

from .config import Config
from .models.bill.bill import Bill
from .tokens import Tokens
from .models.facade import Facade
from .utils.rest_cli import RESTcli
from .models.wallet.wallet import Wallet
from .models.invoice.refund import Refund
from .models.invoice.invoice import Invoice
from .exceptions.bitpay_exception import BitPayException
from .exceptions.bill_query_exception import BillQueryException
from .exceptions.bill_update_exception import BillUpdateException
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
        except Exception as e:
            raise BitPayException("failed to initiate client: " + str(e))

    def build_config_from_file(self, config_file_path: str):
        try:
            self.__configuration = Config()

            if os.path.exists(config_file_path):
                try:
                    read_file = open(config_file_path, 'r')
                    json_data = json.loads(read_file.read())
                    self.__env = json_data['BitPayConfiguration']['Environment']
                    env_config = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]
                except Exception as e:
                    raise BitPayException("Error when reading configuration file", str(e))

                self.__configuration.set_environment(self.__env)
                self.__configuration.set_envconfig({self.__env: env_config})
            else:
                raise BitPayException("Configuration file not found")

        except Exception as e:
            raise BitPayException("failed to process configuration: " + str(e))

    def build_config(self, private_key_path: str, tokens: Tokens):
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
        except Exception as e:
            raise BitPayException("failed to process configuration: " + str(e))

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

            except Exception as e:
                raise BitPayException("When trying to load private key. Make sure the configuration details are "
                                      "correct and the private key and tokens are valid: ", str(e))

    def init(self):
        try:
            proxy = self.__configuration.get_envconfig()[self.__env]["proxy"]
            self.__restcli = RESTcli(self.__env, self.__ec_key, proxy)
            self.load_access_tokens()
            self.__currencies_info = self.load_currencies()
        except Exception as e:
            raise BitPayException("failed to deserialize BitPay server response (Token array): ", str(e))

    def load_currencies(self):
        try:
            return []
        except BitPayException as e:
            print(e)

    def load_access_tokens(self):
        try:
            self.clear_access_token_cache()
            self.__token_cache = self.__configuration.get_envconfig()[self.__env]["ApiTokens"]
        except Exception as e:
            raise BitPayException("When trying to load the tokens: ", str(e))

    def clear_access_token_cache(self):
        self.__token_cache = Tokens()

    def get_access_token(self, key: str):
        try:
            return self.__token_cache[key]
        except Exception as e:
            raise BitPayException("There is no token for the specified key: ", str(e))

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def create_invoice(self, invoice: Invoice, facade: str = Facade.Merchant, sign_request: bool = True) -> Invoice:
        try:
            invoice.set_token(self.get_access_token(facade))
            invoice_json = invoice.to_json()
            response_json = self.__restcli.post("invoices", invoice_json, sign_request)
        except BitPayException as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e), e.get_api_code())
        except Exception as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e))

        try:
            invoice = Invoice(**response_json)
        except Exception as e:
            raise InvoiceQueryException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))

        return invoice

    def get_invoice(self, invoice_id: str, facade: str = Facade.Merchant, sign_request: bool = True) -> Invoice:
        try:
            params = {"token": self.get_access_token(facade)}
            response_json = self.__restcli.get("invoices/%s" % invoice_id, params, sign_request)
        except BitPayException as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e), e.get_api_code())
        except Exception as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e))

        try:
            invoice = Invoice(**response_json)
        except Exception as e:
            raise InvoiceQueryException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))

        return invoice

    def get_invoices(self, date_start: str, date_end: str, status: str = None, order_id: str = None, limit: int = None,
                     offset: int = None) -> [Invoice]:
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "dateStart": date_start, "date_end": date_end}
            if status:
                params["status"] = status
            if order_id:
                params["order_id"] = order_id
            if limit:
                params["limit"] = limit
            if offset:
                params["offset"] = offset

            response_json = self.__restcli.get("invoices/", parameters=params)
        except BitPayException as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e), e.get_api_code())
        except Exception as e:
            raise InvoiceQueryException("failed to serialize Invoice object : %s" % str(e))

        try:
            invoices = []
            for invoice_data in response_json:
                invoices.append(Invoice(**invoice_data))
        except Exception as e:
            raise InvoiceQueryException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))

        return invoices

    def update_invoice(self, invoice_id: str, buyer_email: str) -> Invoice:
        try:
            params = {'token': self.get_access_token(Facade.Merchant), 'buyer_email': buyer_email}
            response_json = self.__restcli.update("invoices/%s" % invoice_id, params)
        except BitPayException as e:
            raise InvoiceUpdateException("failed to serialize Invoice object : %s" % str(e), e.get_api_code())
        except Exception as e:
            raise InvoiceUpdateException("failed to serialize Invoice object : %s" % str(e))

        try:
            invoice = Invoice(**response_json)
        except Exception as e:
            raise InvoiceUpdateException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))

        return invoice

    def cancel_invoice(self, invoice_id: str) -> Invoice:
        try:
            params = {'token': self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.delete("invoices/%s" % invoice_id, params)
        except BitPayException as e:
            raise InvoiceCancellationException("failed to serialize Invoice object : %s" % str(e),
                                               e.get_api_code())
        except Exception as e:
            raise InvoiceCancellationException("failed to serialize Invoice object : %s" % str(e))

        try:
            invoice = Invoice(**response_json)
        except Exception as e:
            raise InvoiceCancellationException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))
        return invoice

    def request_invoice_notifications(self, invoice_id: str) -> bool:
        try:
            invoice = self.get_invoice(invoice_id)
        except Exception as e:
            raise InvoiceNotificationException(f"Invoice with ID: " + {invoice_id} + " Not Found : ",
                                               str(e))
        params = {"token": invoice.get_token()}

        try:
            response_json = self.__restcli.post("invoices/%s" % invoice_id + "/notifications", params)
        except Exception as e:
            raise InvoiceNotificationException("failed to deserialize BitPay server response (Invoice) : %s" % str(e))

        return response_json.lower() == "success"

    def create_refund(self, invoice_id: str, amount: float, currency: str, preview: bool = False,
                      immediate: bool = False, buyer_pays_refund_fee: bool = False) -> Refund:
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "invoiceId": invoice_id, "amount": amount,
                      "currency": currency, "preview": preview, "immediate": immediate,
                      "buyerPaysRefundFee": buyer_pays_refund_fee}

            response_json = self.__restcli.post("refunds", params, True)
        except BitPayException as e:
            raise RefundCreationException("failed to serialize refund object :  %s" % str(e),
                                          e.get_api_code())
        except Exception as e:
            raise RefundCreationException("failed to serialize refund object : %s" % str(e))

        try:
            refund = Refund(**response_json)
        except Exception as e:
            raise RefundCreationException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refund

    def get_refund(self, refund_id: str) -> Refund:
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("refunds/%s" % refund_id, params)
        except BitPayException as e:
            raise RefundQueryException("failed to serialize refund object :  %s" % str(e),
                                       e.get_api_code())
        except Exception as e:
            raise RefundQueryException("failed to serialize refund object : %s" % e)
        try:
            refund = Refund(**response_json)
        except Exception as e:
            raise RefundQueryException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refund

    def get_refunds(self, invoice_id: str) -> [Refund]:
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "invoiceId": invoice_id}
            response_json = self.__restcli.get("refunds", params)
        except BitPayException as e:
            raise RefundQueryException("failed to serialize refund object :  %s" % str(e),
                                       e.get_api_code())
        except Exception as e:
            raise RefundQueryException("failed to serialize refund object : %s" % str(e))

        try:
            # refunds = Refund(**response_json)
            refunds = []
            for refund_data in response_json:
                refunds.append(Invoice(**refund_data))
        except Exception as e:
            raise RefundQueryException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refunds

    def update_refund(self, refund_id: str, status: str) -> Refund:
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "status": status}

            response_json = self.__restcli.update("refunds/%s" % refund_id, params)
        except BitPayException as e:
            raise RefundUpdateException("failed to serialize refund object :  %s" % str(e),
                                        e.get_api_code())
        except Exception as e:
            raise RefundUpdateException("failed to serialize refund object : %s" % str(e))

        try:
            refund = Refund(**response_json)
        except Exception as e:
            raise RefundUpdateException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refund

    def cancel_refund(self, refund_id: str) -> Refund:
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.delete("refunds/%s" % refund_id, params)
        except BitPayException as e:
            raise RefundCancellationException("failed to serialize refund object :  %s" % str(e),
                                              e.get_api_code())
        except Exception as e:
            raise RefundCancellationException("failed to serialize refund object : %s" % str(e))

        try:
            refund = Refund(**response_json)
        except Exception as e:
            raise RefundCancellationException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refund

    #  TODO
    def request_refund_notification(self, refund_id: str) -> bool:
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.post("refunds/%s" % refund_id + "/notifications", params, True)
        except BitPayException as e:
            raise RefundNotificationException("failed to serialize refund object :  %s" % str(e),
                                              e.get_api_code())
        except Exception as e:
            raise RefundNotificationException("failed to serialize refund object : %s" % str(e))

        try:
            refund = Refund(**response_json)
        except Exception as e:
            raise RefundNotificationException("failed to deserialize BitPay server response (Refund) : %s" % str(e))

        return refund

    def get_supported_wallets(self) -> [Wallet]:
        try:
            response_json = self.__restcli.get("supportedWallets/", None)
        except BitPayException as e:
            raise WalletQueryException("failed to serialize wallet object :  %s" % str(e),
                                       e.get_api_code())
        except Exception as e:
            raise WalletQueryException("failed to serialize wallet object : %s" % str(e))

        try:
            wallet = Wallet(**response_json)
        except Exception as e:
            raise WalletQueryException("failed to deserialize BitPay server response (Wallet) : %s" % str(e))

        return wallet

    def create_bill(self, bill: Bill, facade: str = Facade.Merchant, sign_request: bool = True) -> Bill:
        try:
            bill.get_token(self.get_access_token(facade))
            response_json = self.__restcli.post("bills", bill, sign_request)
        except BitPayException as e:
            raise BillCreationException("failed to serialize bill object :  %s" % str(e),
                                        e.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as e:
            raise BillCreationException("failed to deserialize BitPay server response (Bill) : %s" % str(e))

        return bill

    def get_bills(self, status: str = None) -> [Bill]:
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            if status:
                params["status"] = status
            response_json = self.__restcli.get("bills", params, True)
        except BitPayException as e:
            raise BillQueryException("failed to serialize bill object :  %s" % str(e),
                                     e.get_api_code())

        try:
            bills = Bill(**response_json)
        except Exception as e:
            raise BillQueryException("failed to deserialize BitPay server response (Bill) : %s" % str(e))

        return bills

    def get_bill(self, bill_id: str) -> Bill:
        try:
            params = {"token": self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.get("bills/%s" % bill_id, params)
        except BitPayException as e:
            raise BillQueryException("failed to serialize bill object :  %s" % str(e),
                                     e.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as e:
            raise BillQueryException("failed to deserialize BitPay server response (Bill) : %s" % str(e))
        return bill

    def update_bill(self, bill: Bill, bill_id: str) -> Bill:
        try:
            response_json = self.__restcli.update("bills/%s" % bill_id, bill)
        except BitPayException as e:
            raise BillUpdateException("failed to serialize bill object :  %s" % str(e),
                                      e.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as e:
            raise BillUpdateException("failed to deserialize BitPay server response (Bill) : %s" % str(e))
        return bill

    #  TODO
    def deliver_bill(self, bill_id: str, bill_token: str) -> bool:
        try:
            params = {
                "token": bill_token
            }
            response_json = self.__restcli.post("bills/%s" % bill_id + "/deliveries", params)
        except BitPayException as e:
            raise BillDeliveryException("failed to serialize bill object :  %s" % str(e),
                                        e.get_api_code())

        try:
            bill = Bill(**response_json)
        except Exception as e:
            raise BillDeliveryException("failed to deserialize BitPay server response (Bill) : %s" % str(e))
        return bill


