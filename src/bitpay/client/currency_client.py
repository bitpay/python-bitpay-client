from bitpay.client.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.currency_query_exception import CurrencyQueryException
from bitpay.models.currency import Currency


class CurrencyClient:
    __bitpay_client = BitPayClient

    def __init__(self, bitpay_client: BitPayClient):
        self.__bitpay_client = bitpay_client

    def get_currencies(self):
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
