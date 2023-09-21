"""
SupportedTransactionCurrencies
"""
from pydantic import Field

from .supported_transaction_currency import SupportedTransactionCurrency
from ..bitpay_model import BitPayModel


class SupportedTransactionCurrencies(BitPayModel):
    """
    currency selected for payment
    """

    btc: SupportedTransactionCurrency = Field(
        alias="BTC", default=SupportedTransactionCurrency()
    )
    bch: SupportedTransactionCurrency = Field(
        alias="BCH", default=SupportedTransactionCurrency()
    )
    eth: SupportedTransactionCurrency = Field(
        alias="ETH", default=SupportedTransactionCurrency()
    )
    usdc: SupportedTransactionCurrency = Field(
        alias="USDC", default=SupportedTransactionCurrency()
    )
    gusd: SupportedTransactionCurrency = Field(
        alias="GUSD", default=SupportedTransactionCurrency()
    )
    busd: SupportedTransactionCurrency = Field(
        alias="BUSD", default=SupportedTransactionCurrency()
    )
    pax: SupportedTransactionCurrency = Field(
        alias="PAX", default=SupportedTransactionCurrency()
    )
    xrp: SupportedTransactionCurrency = Field(
        alias="XRP", default=SupportedTransactionCurrency()
    )
    doge: SupportedTransactionCurrency = Field(
        alias="DOGE", default=SupportedTransactionCurrency()
    )
    ltc: SupportedTransactionCurrency = Field(
        alias="LTC", default=SupportedTransactionCurrency()
    )
