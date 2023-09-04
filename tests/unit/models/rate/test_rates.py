from typing import List

import pytest

from bitpay.clients.rate_client import RateClient
from bitpay.models.rate.rate import Rate
from bitpay.models.rate.rates import Rates


@pytest.mark.unit
def test_constructor():
    rate = 12.23
    rates_list: List[Rate] = [
        Rate(code="BCH", rate=10.23),
        Rate(code="USD", rate=rate),
    ]
    rates = Rates(rates=rates_list)

    assert rates.get_rate("USD") == rate


@pytest.mark.unit
def test_update(mocker):
    expected_rate = 10.23
    rate_client = mocker.Mock(spec=RateClient)
    rate_client.get_rates.return_value = Rates(rates=
        [Rate(code="BCH", rate=expected_rate)]
    )

    rates = Rates(rates=[Rate(code="USD", rate=123.45)])

    assert rates.get_rate("BCH") is None
    rates.update(rate_client=rate_client)
    assert rates.get_rate("BCH") == expected_rate
