from typing import Dict

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.currency_query_exception import CurrencyQueryException
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
        :raises BitPayException
        :raises CurrencyQueryException
        """
        try:
            response_json = self.__bitpay_client.get("currencies", None, False)
        except BitPayException as exe:
            raise CurrencyQueryException(
                "failed to serialize Currency object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            currencies = {}
            for currency in response_json:
                currency_obj = Currency(**currency)
                currencies[currency_obj.code] = currency_obj
        except Exception as exe:
            raise CurrencyQueryException(
                "failed to deserialize BitPay server response "
                " (Currency) : %s" % str(exe)
            )
        return currencies
