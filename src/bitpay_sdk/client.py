import os
import json

from .config import Config
from .tokens import Tokens
from .models.facade import Facade
from .utils.rest_cli import RESTcli
from .models.invoice.invoice import Invoice
from .exceptions.bitpay_exception import BitPayException


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

    def create_invoice(self, invoice: Invoice, facade, sign_request=True):
        try:
            invoice.set_token(self.get_access_token(facade))
            invoice_json = invoice.to_json()
            response_json = self.__restcli.post("invoices", invoice_json, sign_request)
        except BitPayException as e:
            print(e)

    def get_invoice(self, invoice_id, facade, sign_request=True):
        try:
            params = {"token": self.get_access_token(facade)}
            response_json = self.__restcli.get("invoices/%s" % invoice_id, params, sign_request)
            return Invoice(**response_json)
        except BitPayException as e:
            print(e)

    def get_invoices(self, date_start, date_end, status, order_id, limit, offset):
        try:
            params = {"token": self.get_access_token(Facade.Merchant), "dateStart": date_start, "date_end": date_end}
            response_json = self.__restcli.get("invoices/", parameters=params)
        except BitPayException as e:
            print(e)

    def update_invoice(self, invoice_id, buyer_sms, sms_code, buyer_email):
        try:
            params = {'token': self.get_access_token(Facade.Merchant)}

            if buyer_sms & sms_code:
                pass

            if buyer_sms is not None:
                params['buyer_sms'] = buyer_sms

            if sms_code is not None:
                params['sms_code'] = sms_code

            if buyer_email is not None:
                params['buyer_email'] = buyer_email

            response_json = self.__restcli.update("invoices/%s" % invoice_id, json.dumps(params))
        except BitPayException as e:
            print(e)

    def cancel_invoice(self, invoice_id):
        try:
            params = {'token': self.get_access_token(Facade.Merchant)}
            response_json = self.__restcli.delete("invoices/%s" % invoice_id, params)
        except BitPayException as e:
            print(e)

    def get_invoice_webhook(self, invoice_id):
        try:
            self.get_invoice(invoice_id)
            params = {}
            # Conditions missing look from node
            response_json = self.__restcli.post("invoices/%s" % invoice_id + "/notifications", params)
        except BitPayException as e:
            print(e)
