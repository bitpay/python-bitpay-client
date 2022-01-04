import urllib
import requests
from dotenv import load_dotenv, dotenv_values
from ..exceptions.bitpay_exception import BitPayException
from .key_utils import get_compressed_public_key_from_pem, sign


load_dotenv()
env = dotenv_values()


class RESTcli:
    __client = ""
    __baseurl = ""
    __eckey = ""
    __identity = ""
    __proxy = ""

    def __init__(self, environment, eckey, proxy=None):
        self.__eckey = eckey
        self.__baseurl = env["TestUrl"] if environment == env["Test"] else env["ProdUrl"]
        self.__proxy = proxy
        self.init()

    def init(self):
        try:
            config = {
                'base_url': self.__baseurl,
                'defaults': {
                    'headers': {
                        'x-accept-version': env["BitpayApiVersion"],
                        'x-bitpay-plugin-info': env["BitpayPluginInfo"],
                        'x-bitpay-api-frame': env["BitpayApiFrame"],
                        'x-bitpay-api-frame-version': env["BitpayApiFrameVersion"],
                    },
                }
            }
            if self.__proxy != '':
                config['proxy'] = self.__proxy

        except BitPayException as e:
            print(e)

    def post(self, uri, form_data, signature_required=True):
        full_url = self.__baseurl + uri
        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url, self.__eckey)

        headers = {"content-type": "application/json",
                   'X-accept-version': '2.0.0', 'X-bitpay-plugin-info': env['BitpayPluginInfo'],
                   'X-bitpay-api-frame': env['BitpayApiFrame'],
                   'X-bitpay-api-frame-version': env['BitpayApiFrameVersion']}

        if signature_required:
            headers['x-signature'] = xsignature
            headers['x-identity'] = xidentity
        response = requests.post(full_url, data=form_data, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def get(self, uri, parameters=None, signature_required=True):
        full_url = self.__baseurl + uri

        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url, self.__eckey)

        headers = {"content-type": "application/json",
                   'X-accept-version': '2.0.0', 'X-bitpay-plugin-info': env['BitpayPluginInfo'],
                   'X-bitpay-api-frame': env['BitpayApiFrame'],
                   'X-bitpay-api-frame-version': env['BitpayApiFrameVersion']}

        if signature_required:
            headers['x-signature'] = xsignature
            headers['x-identity'] = xidentity

        response = requests.get(full_url, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def delete(self, uri, parameters=None):
        full_url = self.__baseurl + uri

        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url, self.__eckey)

        headers = {"content-type": "application/json", 'X-Identity': xidentity, 'X-Signature': xsignature,
                   'X-accept-version': '2.0.0', 'X-bitpay-plugin-info': env['BitpayPluginInfo'],
                   'X-bitpay-api-frame': env['BitpayApiFrame'],
                   'X-bitpay-api-frame-version': env['BitpayApiFrameVersion']}

        response = requests.delete(full_url, data=parameters, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def update(self, uri, form_data=[]):
        full_url = self.__baseurl + uri

        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url, self.__eckey)

        headers = {"content-type": "application/json", 'X-Identity': xidentity, 'X-Signature': xsignature,
                   'X-accept-version': '2.0.0', 'X-bitpay-plugin-info': env['BitpayPluginInfo'],
                   'X-bitpay-api-frame': env['BitpayApiFrame'],
                   'X-bitpay-api-frame-version': env['BitpayApiFrameVersion']}

        response = requests.put(full_url, data=form_data, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def response_to_json_string(self, response):
        return response.json()['data']
