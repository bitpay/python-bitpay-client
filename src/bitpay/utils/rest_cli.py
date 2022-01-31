"""
HTTP methods
"""
import json
import urllib
import requests

from .. import env
from ..exceptions.bitpay_exception import BitPayException
from .key_utils import get_compressed_public_key_from_pem, sign


class RESTcli:
    __client = ""
    __baseurl = ""
    __eckey = ""
    __identity = ""
    __proxy = ""

    def __init__(self, environment, eckey, proxy=None):
        self.__eckey = eckey
        self.__baseurl = env.TESTURL if environment == env.TEST else env.PRODURL
        self.__proxy = proxy
        self.init()

    def init(self):
        try:
            config = {
                "base_url": self.__baseurl,
                "defaults": {
                    "headers": {
                        "x-accept-version": env.BITPAYAPIVERSION,
                        "x-bitpay-plugin-info": env.BITPAYPLUGININFO,
                        "x-bitpay-api-frame": env.BITPAYAPIFRAME,
                        "x-bitpay-api-frame-version": env.BITPAYAPIFRAMEVERSION,
                    },
                },
            }
            if self.__proxy != "":
                config["proxy"] = self.__proxy

        except BitPayException as e:
            print(e)

    def post(self, uri, form_data, signature_required=True):
        """
        :param uri: Url at which user wants to post the data
        :param form_data: the data to be posted
        :param signature_required: Signature of the full request URL concatenated
        with the request body
        :return: json response
        """
        full_url = self.__baseurl + uri
        form_data = json.dumps(form_data)

        headers = {
            "content-type": "application/json",
            "X-accept-version": "2.0.0",
            "X-bitpay-plugin-info": env.BITPAYPLUGININFO,
            "X-bitpay-api-frame": env.BITPAYAPIFRAME,
            "X-bitpay-api-frame-version": env.BITPAYAPIFRAMEVERSION,
        }

        if signature_required:
            headers["x-signature"] = sign(full_url + form_data, self.__eckey)
            headers["x-identity"] = get_compressed_public_key_from_pem(self.__eckey)

        response = requests.post(full_url, data=form_data, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def get(self, uri, parameters=None, signature_required=True):
        """

        :param uri: Url from which user wants to get the data
        :param parameters: These are query parameters
        :param signature_required: Signature of the full request URL concatenated
        :return: json response
        """
        full_url = self.__baseurl + uri
        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        headers = {
            "content-type": "application/json",
            "X-accept-version": "2.0.0",
            "X-bitpay-plugin-info": env.BITPAYPLUGININFO,
            "X-bitpay-api-frame": env.BITPAYAPIFRAME,
            "X-bitpay-api-frame-version": env.BITPAYAPIFRAMEVERSION,
        }

        if signature_required:
            headers["x-signature"] = sign(full_url, self.__eckey)
            headers["x-identity"] = get_compressed_public_key_from_pem(self.__eckey)

        response = requests.get(full_url, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def delete(self, uri, parameters=None):
        """

        :param uri: Url from which user wants to delete the data
        :param parameters: These are query parameters
        :return: json response
        """
        full_url = self.__baseurl + uri

        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url, self.__eckey)

        headers = {
            "content-type": "application/json",
            "X-Identity": xidentity,
            "X-Signature": xsignature,
            "X-accept-version": "2.0.0",
            "X-bitpay-plugin-info": env.BITPAYPLUGININFO,
            "X-bitpay-api-frame": env.BITPAYAPIFRAME,
            "X-bitpay-api-frame-version": env.BITPAYAPIFRAMEVERSION,
        }

        response = requests.delete(full_url, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def update(self, uri, form_data):
        """
        :param uri: Url from which user wants to delete the data
        :param form_data: the data to be updated
        :return: json response
        """
        full_url = self.__baseurl + uri
        form_data = json.dumps(form_data)

        xidentity = get_compressed_public_key_from_pem(self.__eckey)
        xsignature = sign(full_url + form_data, self.__eckey)

        headers = {
            "content-type": "application/json",
            "X-Identity": xidentity,
            "X-Signature": xsignature,
            "X-accept-version": "2.0.0",
            "X-bitpay-plugin-info": env.BITPAYPLUGININFO,
            "X-bitpay-api-frame": env.BITPAYAPIFRAME,
            "X-bitpay-api-frame-version": env.BITPAYAPIFRAMEVERSION,
        }

        response = requests.put(full_url, data=form_data, headers=headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def response_to_json_string(self, response):
        # if not response:
        #     raise BitPayException("Error: HTTP response is null")

        response_obj = response.json()
        if "status" in response_obj:
            if response_obj["status"] == "error":
                raise BitPayException(
                    "Error: " + response_obj["error"], response_obj["code"]
                )

        if "error" in response_obj:
            raise BitPayException(
                "Error: " + response_obj["error"], response_obj["code"]
            )
        elif "errors" in response_obj:
            message = ""
            for error in response_obj["errors"]:
                message += "\n" + str(error)
            raise BitPayException("Errors: " + message)

        if "success" in response_obj:
            return response_obj["success"]

        if "data" in response_obj:
            return response_obj["data"]

        return response_obj
