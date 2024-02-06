"""
Rates
"""

from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.rate.rate import Rate
from bitpay.models.currency import Currency
from bitpay.exceptions.bitpay_exception import BitPayException
from typing import List, Optional


class Rates(BitPayModel):
    """
    Rates:Rates are exchange rates, representing the number of fiat
    currency units equivalent to one BTC.
    """

    rates: List[Rate] = []

    def update(self, rate_client) -> None:  # type: ignore
        rates = rate_client.get_rates()
        self.rates = rates.rates

    def get_rate(self, currency_code: str) -> Optional[float]:
        """
        :raises BitPayGenericException
        """
        if Currency.is_valid(currency_code) is False:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "currency code must be a type of Model.Currency"
            )

        val = None
        for rate_obj in self.rates:
            if rate_obj.code == currency_code:
                val = rate_obj.rate
        return val
