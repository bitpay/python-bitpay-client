"""
Rates
"""
from .rate import Rate
from ..currency import Currency
from ...client.rate_client import RateClient
from ...exceptions.bitpay_exception import BitPayException
from typing import List


class Rates:
    """
    Rates:Rates are exchange rates, representing the number of fiat
    currency units equivalent to one BTC.
    """

    __rates = List[Rate]

    def __init__(self, rates: List[Rate]):
        self.__rates = rates

    def get_rates(self):
        return self.__rates

    def update(self, rate_client: RateClient):
        self.__rates = rate_client.get_rates().get_rates()

    def get_rate(self, currency_code):
        if not Currency.is_valid(currency_code):
            raise BitPayException("currency code must be a type of Model.Currency")

        val = None
        for rate_obj in self.__rates:
            if rate_obj.get_code == currency_code:
                val = rate_obj.get_rate()
        return val

    def to_json(self):
        """
        :return: data in json
        """
        data = {"rates": self.get_rates()}
        return data
