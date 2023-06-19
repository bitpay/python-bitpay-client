from typing import List

from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_group_failed import PayoutGroupFailed


class PayoutGroup:
    __payouts: List[Payout] = []
    __failed: List[PayoutGroupFailed] = []

    def __init__(self, payouts: List[Payout], failed: List[PayoutGroupFailed]):
        self.__payouts = payouts
        self.__failed = failed

    def get_payouts(self) -> List[Payout]:
        return self.__payouts

    def set_payouts(self, value: List[Payout]) -> None:
        self.__payouts = value

    def get_failed(self) -> List[PayoutGroupFailed]:
        return self.__failed

    def set_failed(self, value: List[PayoutGroupFailed]) -> None:
        self.__failed = value
