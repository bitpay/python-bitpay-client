import os
import json
from .config import Config
from .tokens import Tokens
from .models.facade import Facade
from .utils.rest_cli import RESTcli
from .models.invoice.invoice import Invoice
from .exceptions.bitpay_exception import BitPayException


class Client:
    __configuration = ""
    __env = ""
    __eckey = ""
    __token_cache = ""
    __restcli = None

    def __init__(self, config_file_path):
        self.build_config_from_file(config_file_path)
        self.init_keys()
        self.init()

    def build_config_from_file(self, config_file_path):
        self.__configuration = Config()

        if os.path.exists(config_file_path):

            try:
                read_file = open(config_file_path, 'r')
                content = read_file.read()
                json_data = json.loads(content)
                self.__configuration.set_environment(json_data['BitPayConfiguration']['Environment'])
                self.__env = self.__configuration.get_environment()
                tokens = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]["ApiTokens"]
                private_key_path = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]["PrivateKeyPath"]
                private_key_secret = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]["PrivateKeySecret"]
                proxy = json_data["BitPayConfiguration"]["EnvConfig"][self.__env]["proxy"]

                env_config = {self.__env: {
                    "PrivateKeyPath": private_key_path,
                    "PrivateKeySecret": private_key_secret,
                    "ApiTokens": tokens,
                    "Proxy": proxy
                }}
                self.__configuration.set_envconfig(env_config)

            except BitPayException as e:
                print(e)

        else:
            raise BitPayException("Configuration file not found")

    def init_keys(self):
        private_key_path = self.__configuration.get_envconfig()[self.__env]["PrivateKeyPath"]
        try:
            if not self.__eckey:
                with open(private_key_path) as f:
                    self.__eckey = f.read()

        except BitPayException as e:
            raise BitPayException("failed to build configuration : ")

    def init(self):
        try:
            proxy = self.__configuration.get_envconfig()[self.__env]["Proxy"]
            self.__restcli = RESTcli(self.__env, self.__eckey, proxy)
            self.load_access_tokens()
            # TODO :load currencies
        except BitPayException as e:
            print(e)

    def load_access_tokens(self):
        try:
            self.clear_access_token_cache()
            self.__token_cache = self.__configuration.get_envconfig()[self.__env]["ApiTokens"]
        except BitPayException as e:
            print(e)

    def clear_access_token_cache(self):
        self.__token_cache = Tokens()

    def create_invoice(self, invoice: Invoice, facade, sign_request=True):
        try:
            invoice.set_token(self.get_access_token(facade))
            print(invoice)
            invoice_json = invoice.to_json()

            response = self.__restcli.post("invoices", invoice_json, sign_request)
            print(response)

        except BitPayException as e:
            print(e)

    def get_invoice(self, invoice_id, facade, sign_request=True):
        try:
            params = {"token": self.get_access_token(facade)}
            response_json = self.__restcli.get("invoices/%s" % invoice_id, params, sign_request)
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

    def get_access_token(self, key: str):
        try:
            return self.__token_cache[key]
        except BitPayException as e:
            print(e)
