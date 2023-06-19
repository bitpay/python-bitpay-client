import json
import urllib
from typing import Dict, Any, Optional

import requests
from requests import Response

from bitpay.config import Config
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.utils.key_utils import sign, get_compressed_public_key_from_pem
from urllib.parse import urlparse


class BitPayClient:
    __headers: Dict[str, str] = {}
    __base_url: str
    __ec_key: Optional[str] = None
    __proxy: Optional[str] = None

    def __init__(
        self, base_url: str, ec_key: Optional[str] = None, proxy: Optional[str] = None
    ):
        self.__base_url = base_url
        self.__ec_key = ec_key
        self.__proxy = proxy
        self.init()

    def init(self) -> None:
        try:
            self.__headers = {
                "x-accept-version": Config.BITPAY_API_VERSION.value,
                "x-bitpay-plugin-info": Config.BITPAY_PLUGIN_INFO.value,
                "x-bitpay-api-frame": Config.BITPAY_API_FRAME.value,
                "x-bitpay-api-frame-version": Config.BITPAY_API_FRAME_VERSION.value,
                "content-type": "application/json",
                "X-accept-version": "2.0.0",
            }
            if self.__proxy is not None:
                self.__headers["proxy"] = self.__proxy

        except BitPayException as e:
            print(e)

    def post(
        self, uri: str, form_data: Any = {}, signature_required: bool = True
    ) -> dict:
        """
        :param uri: Url at which user wants to post the data
        :param form_data: the data to be posted
        :param signature_required: Signature of the full request URL concatenated
        with the request body
        :return: json response
        """
        full_url = self.__base_url + uri
        form_data = json.dumps(form_data)
        if signature_required:
            self.__headers["x-signature"] = sign(full_url + form_data, self.__ec_key)
            self.__headers["x-identity"] = get_compressed_public_key_from_pem(
                self.__ec_key
            )

        response = requests.post(full_url, data=form_data, headers=self.__headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def get(
        self,
        uri: str,
        parameters: Optional[dict] = None,
        signature_required: bool = True,
    ) -> dict:
        """

        :param uri: Url from which user wants to get the data
        :param parameters: These are query parameters
        :param signature_required: Signature of the full request URL concatenated
        :return: json response
        """
        full_url = self.__base_url + uri
        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        if signature_required:
            self.__headers["x-signature"] = sign(full_url, self.__ec_key)
            self.__headers["x-identity"] = get_compressed_public_key_from_pem(
                self.__ec_key
            )

        response = requests.get(full_url, headers=self.__headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def delete(self, uri: str, parameters: Optional[dict] = None) -> dict:
        """

        :param uri: Url from which user wants to delete the data
        :param parameters: These are query parameters
        :return: json response
        """
        full_url = self.__base_url + uri

        if parameters is not None:
            full_url = "%s?%s" % (full_url, urllib.parse.urlencode(parameters))

        self.__headers["x-signature"] = sign(full_url, self.__ec_key)
        self.__headers["x-identity"] = get_compressed_public_key_from_pem(self.__ec_key)

        response = requests.delete(full_url, headers=self.__headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def update(self, uri: str, form_data: Any = {}) -> dict:
        """
        :param uri: Url from which user wants to delete the data
        :param form_data: the data to be updated
        :return: json response
        """

        full_url = self.__base_url + uri
        form_data = json.dumps(form_data)

        self.__headers["x-signature"] = sign(full_url + form_data, self.__ec_key)
        self.__headers["x-identity"] = get_compressed_public_key_from_pem(self.__ec_key)

        response = requests.put(full_url, data=form_data, headers=self.__headers)
        json_response = self.response_to_json_string(response)
        return json_response

    def response_to_json_string(self, response: Response) -> Any:
        if not response.json():
            raise BitPayException("Error: HTTP response is null")

        response_obj = response.json()
        if "status" in response_obj:
            if response_obj["status"] == "error":
                raise BitPayException(
                    "Error: " + response_obj["error"], response_obj["code"]
                )

        if "error" in response_obj:
            raise BitPayException("Error: " + response_obj["error"])
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
