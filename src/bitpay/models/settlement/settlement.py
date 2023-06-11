"""
Settlement: Settlements are transfers of payment profits from BitPay to bank
accounts and cryptocurrency wallets owned by merchants, partners, etc. This
endpoint exposes reports detailing these settlements.
"""
from typing import List, Optional

from .payout_info import PayoutInfo
from .with_holdings import WithHoldings
from .settlement_ledger_entry import SettlementLedgerEntry
from bitpay.utils.key_utils import change_camel_case_to_snake_case
from bitpay.utils.model_util import ModelUtil


class Settlement:
    """
    Settlement
    """

    __id = None
    __account_id = None
    __currency = None
    __payout_info = None
    __status = None
    __date_created = None
    __date_executed = None
    __date_completed = None
    __opening_date = None
    __closing_date = None
    __opening_balance = None
    __ledger_entries_sum = None
    __withholdings = None
    __withholdings_sum = None
    __total_amount = None
    __ledger_entries: Optional[List[SettlementLedgerEntry]] = None
    __token = None
    __amount_usd_unlocked = None

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            try:
                value = ModelUtil().get_field_value(
                    key,
                    value,
                    {
                        "payoutInfo": PayoutInfo,
                        "openingBalance": "float",
                        "ledgerEntriesSum": "float",
                        "withHoldingsSum": "float",
                        "totalAmount": "float",
                    },
                    {
                        "withholdings": WithHoldings,
                        "ledgerEntries": SettlementLedgerEntry,
                    },
                )
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_id(self) -> Optional[str]:
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id: Optional[str]) -> None:
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_account_id(self) -> Optional[str]:
        """
        Get method for to account_id
        :return: account_id
        """
        return self.__account_id

    def set_account_id(self, account_id: Optional[str]) -> None:
        """
        Set method for to account_id
        :param account_id: account_id
        """
        self.__account_id = account_id

    def get_currency(self) -> Optional[str]:
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency: Optional[str]) -> None:
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_payout_info(self) -> Optional[PayoutInfo]:
        """
        Get method for to payout_info
        :return: payout_info
        """
        return self.__payout_info

    def set_payout_info(self, payout_info: Optional[PayoutInfo]) -> None:
        """
        Set method for to payout_info
        :param payout_info: payout_info
        """
        self.__payout_info = payout_info

    def get_status(self) -> Optional[str]:
        """
        Get method for to status
        :return: status
        """
        return self.__status

    def set_status(self, status: Optional[str]) -> None:
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_date_created(self) -> Optional[str]:
        """
        Get method for to date_created
        :return: date_created
        """
        return self.__date_created

    def set_date_created(self, date_created: Optional[str]) -> None:
        """
        Set method for to date_created
        :param date_created: date_created
        """
        self.__date_created = date_created

    def get_date_executed(self) -> Optional[str]:
        """
        Get method for to date_executed
        :return: date_executed
        """
        return self.__date_executed

    def set_date_executed(self, date_executed: Optional[str]) -> None:
        """
        Set method for to date_executed
        :param date_executed: date_executed
        """
        self.__date_executed = date_executed

    def get_date_completed(self) -> Optional[str]:
        """
        Get method for to date_completed
        :return: date_completed
        """
        return self.__date_completed

    def set_date_completed(self, date_completed: Optional[str]) -> None:
        """
        Set method for to date_completed
        :param date_completed: date_completed
        """
        self.__date_completed = date_completed

    def get_opening_date(self) -> Optional[str]:
        """
        Get method for to opening_date
        :return: opening_date
        """
        return self.__opening_date

    def set_opening_date(self, opening_date: Optional[str]) -> None:
        """
        Set method for to opening_date
        :param opening_date: opening_date
        """
        self.__opening_date = opening_date

    def get_closing_date(self) -> Optional[str]:
        """
        Get method for to closing_date
        :return: closing_date
        """
        return self.__closing_date

    def set_closing_date(self, closing_date: Optional[str]) -> None:
        """
        Set method for to closing_date
        :param closing_date: closing_date
        """
        self.__closing_date = closing_date

    def get_opening_balance(self) -> Optional[float]:
        """
        Get method for to opening_balance
        :return: opening_balance
        """
        return self.__opening_balance

    def set_opening_balance(self, opening_balance: Optional[float]) -> None:
        """
        Set method for to opening_balance
        :param opening_balance: opening_balance
        """
        self.__opening_balance = opening_balance

    def get_ledger_entries_sum(self) -> Optional[float]:
        """
        Get method for to ledger_entries_sum
        :return: ledger_entries_sum
        """
        return self.__ledger_entries_sum

    def set_ledger_entries_sum(self, ledger_entries_sum: Optional[float]) -> None:
        """
        Set method for to ledger_entries_sum
        :param ledger_entries_sum: ledger_entries_sum
        """
        self.__ledger_entries_sum = ledger_entries_sum

    def get_withholdings(self) -> Optional[List[WithHoldings]]:
        """
        Get method for to withholdings
        :return: List[WithHoldings]
        """
        return self.__withholdings

    def set_withholdings(self, withholdings: List[WithHoldings]) -> None:
        """
        Set method for to withholdings
        :param withholdings: withholdings
        """
        self.__withholdings = withholdings

    def get_withholdings_sum(self) -> Optional[float]:
        """
        Get method for to withholdings_sum
        :return: withholdings_sum
        """
        return self.__withholdings_sum

    def set_withholdings_sum(self, withholdings_sum: Optional[float]) -> None:
        """
        Set method for to withholdings_sum
        :param withholdings_sum: withholdings_sum
        """
        self.__withholdings_sum = withholdings_sum

    def get_total_amount(self) -> Optional[float]:
        """
        Get method for to total_amount
        :return: total_amount
        """
        return self.__total_amount

    def set_total_amount(self, total_amount: Optional[float]) -> None:
        """
        Set method for to total_amount
        :param total_amount: total_amount
        """
        self.__total_amount = total_amount

    def get_ledger_entries(self) -> Optional[List[SettlementLedgerEntry]]:
        """
        Get method for to ledger_entries
        :return: ledger_entries
        """
        return self.__ledger_entries

    def set_ledger_entries(
        self, ledger_entries: Optional[List[SettlementLedgerEntry]]
    ) -> None:
        """
        Set method for to ledger_entries
        :param ledger_entries: ledger_entries
        """
        self.__ledger_entries = ledger_entries

    def get_token(self) -> Optional[str]:
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token: Optional[str]) -> None:
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)
