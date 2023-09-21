from typing import List
from bitpay.models.bitpay_model import BitPayModel
from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_group_failed import PayoutGroupFailed


class PayoutGroup(BitPayModel):
    payouts: List[Payout] = []
    failed: List[PayoutGroupFailed] = []
