from typing import List

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.ledger_query_exception import LedgerQueryException
from bitpay.models.facade import Facade
from bitpay.models.ledger.ledger import Ledger
from bitpay.models.ledger.ledger_entry import LedgerEntry
from bitpay.utils.token_container import TokenContainer


class LedgerClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer

    def __init__(self, bitpay_client: BitPayClient, token_container: TokenContainer):
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container

    def get_entries(
        self, currency: str, start_date: str, end_date: str
    ) -> List[LedgerEntry]:
        """
        Retrieve a list of ledgers by date range using the merchant facade.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str start_date: The first date for the query filter.
        :param str end_date: The last date for the query filter.
        :return: A LedgerEntry object populated with the BitPay ledger entries list.
        :rtype: [LedgerEntry]
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "currency": currency,
                "startDate": start_date,
                "endDate": end_date,
            }
            response_json = self.__bitpay_client.get("ledgers/%s" % currency, params)
        except BitPayException as exe:
            raise LedgerQueryException(
                "failed to serialize Ledger object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(LedgerEntry(**ledger))
        except Exception as exe:
            raise LedgerQueryException(
                "failed to deserialize BitPay server response "
                "(Ledger) : %s" % str(exe)
            )
        return ledgers

    def get_ledgers(self) -> List[Ledger]:
        """
        Retrieve a list of ledgers using the merchant facade.

        :return: A list of Ledger objects populated with the currency and
        current balance of each one.
        :rtype [Ledger]
        :raises BitPayException
        :raises LedgerQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.get("ledgers", params)
        except BitPayException as exe:
            raise LedgerQueryException(
                "failed to serialize Ledger object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(Ledger(**ledger))
        except Exception as exe:
            raise LedgerQueryException(
                "failed to deserialize BitPay server response"
                " (Ledger) : %s" % str(exe)
            )
        return ledgers
