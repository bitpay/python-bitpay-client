"""
MinerFeesItem
"""
from typing import Optional

from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class MinerFeesItem:
    """
    The total amount of fees that the purchaser will pay to cover BitPay's
     UTXO sweep cost for an invoice. The key is the currency and the value is
      an amount in satoshis. This is referenced as "Network Cost" on an invoice,
    see this support article for more information
    """

    __satoshis_per_byte = None
    __total_fee = None
    __fiat_amount = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil.get_field_value(
                    key,
                    value,
                    {
                        "satoshisPerByte": "float",
                        "totalFee": "float",
                        "fiatAmount": "float",
                    },
                    {},
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_satoshis_per_byte(self) -> Optional[float]:
        """
        Get method for the satoshis_per_byte
        :return: satoshis_per_byte
        """
        return self.__satoshis_per_byte

    def set_satoshis_per_byte(self, satoshis_per_byte: Optional[float]) -> None:
        """
        Set method for the satoshis_per_byte
        :param satoshis_per_byte: satoshis_per_byte
        """
        self.__satoshis_per_byte = satoshis_per_byte

    def get_total_fee(self) -> Optional[float]:
        """
        Get method for the total_fee
        :return: total_fee
        """
        return self.__total_fee

    def set_total_fee(self, total_fee: Optional[float]) -> None:
        """
        Set method for the total_fee
        :param total_fee: total_fee
        """
        self.__total_fee = total_fee

    def get_fiat_amount(self) -> Optional[float]:
        """
        Get method for the fiat_amount
        :return: fiat_amount
        """
        return self.__fiat_amount

    def set_fiat_amount(self, fiat_amount: Optional[float]) -> None:
        """
        Set method for the fiat_amount
        :param fiat_amount: fiat_amount
        """
        self.__fiat_amount = fiat_amount

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
