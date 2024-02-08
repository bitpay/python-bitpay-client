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
    wbtc: SupportedTransactionCurrency = Field(
        alias="WBTC", default=SupportedTransactionCurrency()
    )
    dai: SupportedTransactionCurrency = Field(
        alias="DAI", default=SupportedTransactionCurrency()
    )
    euroc: SupportedTransactionCurrency = Field(
        alias="EUROC", default=SupportedTransactionCurrency()
    )
    matic: SupportedTransactionCurrency = Field(
        alias="MATIC", default=SupportedTransactionCurrency()
    )
    matic_e: SupportedTransactionCurrency = Field(
        alias="MATIC_e", default=SupportedTransactionCurrency()
    )
    eth_m: SupportedTransactionCurrency = Field(
        alias="ETH_m", default=SupportedTransactionCurrency()
    )
    usdc_m: SupportedTransactionCurrency = Field(
        alias="USDC_m", default=SupportedTransactionCurrency()
    )
    busd_m: SupportedTransactionCurrency = Field(
        alias="BUSD_m", default=SupportedTransactionCurrency()
    )
    dai_m: SupportedTransactionCurrency = Field(
        alias="DAI_m", default=SupportedTransactionCurrency()
    )
    wbtc_m: SupportedTransactionCurrency = Field(
        alias="WBTC_m", default=SupportedTransactionCurrency()
    )
    shib_m: SupportedTransactionCurrency = Field(
        alias="SHIB_m", default=SupportedTransactionCurrency()
    )
