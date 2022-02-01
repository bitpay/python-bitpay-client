"""
Rates
"""
from .rate import Rate
from ..currency import Currency
from ...exceptions.bitpay_exception import BitPayException
from ...utils.key_utils import change_camel_case_to_snake_case


class Rates:
    """
    Rates:Rates are exchange rates, representing the number of fiat
    currency units equivalent to one BTC.
    """

    __bp = None
    __rates = None

    def __init__(self, rates, b_p, **kwargs):
        self.set_bp(b_p)
        self.set_rates(rates)

        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_bp(self):
        """
        Get method for the bp
        :return: bp
        """
        return self.__bp

    def set_bp(self, b_p):
        """
        Set method for the b_p
        :param b_p: b_p
        """
        self.__bp = b_p

    def set_rates(self, rates):
        """
        Set method for the rates
        :param rates: rates
        """
        self.__rates = rates

    def get_rates(self):
        rates = []
        for rate in self.__rates:
            if isinstance(rate, Rate):
                rates.append(rate.to_json())
            else:
                rates.append(rate)
        return rates

    def update(self):
        self.__rates = self.__bp.get_rates().get_rates()

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
