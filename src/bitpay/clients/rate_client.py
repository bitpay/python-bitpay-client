from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.rate_query_exception import RateQueryException
from bitpay.models.rate.rate import Rate
from bitpay.models.rate.rates import Rates


class RateClient:
    __bitpay_client = BitPayClient

    def __init__(self, bitpay_client: BitPayClient):
        self.__bitpay_client = bitpay_client

    def get_rates(self) -> Rates:
        """
        Retrieve the exchange rate table maintained by BitPay. See https://bitpay.com/bitcoin-exchange-rates.

        :return: A Rates object populated with the BitPay exchange rate table.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__bitpay_client.get("rates", None, False)
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            rates = []
            for rate in response_json:
                rates.append(Rate(**rate))
            return Rates(rates=rates)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (Rates) : %s" % str(exe)
            )

    def get_currency_rates(self, base_currency: str) -> Rates:
        """
        Retrieve all the rates for a given cryptocurrency

        :param str base_currency: The cryptocurrency for which you want to fetch the rates.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :return: A Rates object populated with the currency rates for the requested baseCurrency.
        :rtype: [Rates]
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__bitpay_client.get(
                "rates/%s" % base_currency, None, False
            )
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            if isinstance(response_json, dict):
                response_json = [response_json]

            rates = []
            for rate in response_json:
                rates.append(Rate(**rate))
            return Rates(rates=rates)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (Rates) : %s" % str(exe)
            )

    def get_currency_pair_rate(self, base_currency: str, currency: str) -> Rate:
        """
        Retrieve the rate for a cryptocurrency / fiat pair

        :param str base_currency: The cryptocurrency for which you want to fetch the fiat-equivalent rate.
        Current supported values are BTC, BCH, ETH, XRP, DOGE and LTC
        :param str currency: The fiat currency for which you want to fetch the baseCurrency rate
        :return: A rate object populated with the currency rate for the requested baseCurrency.
        :rtype: Rate
        :raises BitPayException
        :raises RateQueryException
        """
        try:
            response_json = self.__bitpay_client.get(
                "rates/%s" % base_currency + "/%s" % currency, None, False
            )
        except BitPayException as exe:
            raise RateQueryException(
                "failed to serialize Rates object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return Rate(**response_json)
        except Exception as exe:
            raise RateQueryException(
                "failed to deserialize BitPay server response "
                " (rate) : %s" % str(exe)
            )
