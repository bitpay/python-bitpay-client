from typing import List, Union
from .currencies import Currencies
from bitpay.utils.model_util import ModelUtil
from ..bitpay_model import BitPayModel


class Wallet(BitPayModel):
    """
    supported wallets and supported currency details
    """

    key: Union[str, None] = None
    display_name: Union[str, None] = None
    avatar: Union[str, None] = None
    pay_pro: Union[bool, None] = False
    currencies: Union[List[Currencies], None] = None
    image: Union[str, None] = None

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
