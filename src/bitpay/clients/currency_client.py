from typing import Dict

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.currency import Currency


class CurrencyClient:
    __bitpay_client = BitPayClient

    def __init__(self, bitpay_client: BitPayClient):
        self.__bitpay_client = bitpay_client

    def get_currencies(self) -> Dict[str, Currency]:
        """
        Fetch the supported currencies.

        :return: A list of BitPay Invoice objects.
        :rtype: [Currency]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        response = self.__bitpay_client.get("currencies", None, False)
        response_json = ResponseParser.response_to_json_string(response)

        currencies = {}

        try:
            for currency in response_json:
                currency_obj = Currency(**currency)
                currencies[currency_obj.code] = currency_obj
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Currency", str(exe)
            )

        return currencies
