# TODO Client import ?
from .rate import Rate
from ..currency import Currency
from src.bitpay_sdk.client import Client
from ...exceptions.bitpay_exception import BitPayException


class Rates:
    __bp = None
    __rates = None

    def __init__(self, rates, bp: Client):
        self.__bp = bp
        self.__rates = rates

    def get_rates(self):
        rates = []
        for rate in self.__rates:
            if hasattr(rate, Rate):
                rates.append(rate.to_json())
            else:
                rates.append(rate)
        return rates

    def update(self):
        self.__rates = self.__bp.get_rates().get_rates()

    def get_rate(self, currency_code):
        if Currency.is_valid(currency_code):
            raise BitPayException("currency code must be a type of Model.Currency")

        for rate_obj in self.__rates:
            if rate_obj.get_code == currency_code:
                val = rate_obj.get_rate()
        return val

    def to_json(self):
        """
        :return: data in json
        """
        data ={
            'rates': self.get_rates()
        }
        return data
