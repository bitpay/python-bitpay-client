"""
Currencies
"""

from typing import Union
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.wallet.currency_qr import CurrencyQr


class Currencies(BitPayModel):
    """
    details of what currencies support payments for this wallet
    """

    code: Union[str, None] = None
    p2p: Union[bool, None] = False
    dapp_browser: Union[bool, None] = False
    pay_pro: Union[bool, None] = False
    qr: Union[CurrencyQr, None] = None
    image: Union[str, None] = None
    withdrawal_fee: Union[str, None] = None
    wallet_connect: Union[bool, None] = False
