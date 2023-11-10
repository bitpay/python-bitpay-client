from typing import List

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
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
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "currency": currency,
            "startDate": start_date,
            "endDate": end_date,
        }
        response = self.__bitpay_client.get("ledgers/%s" % currency, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(LedgerEntry(**ledger))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Ledger", str(exe)
            )
            raise

        return ledgers

    def get_ledgers(self) -> List[Ledger]:
        """
        Retrieve a list of ledgers using the merchant facade.

        :return: A list of Ledger objects populated with the currency and
        current balance of each one.
        :rtype [Ledger]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
        response = self.__bitpay_client.get("ledgers", params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            ledgers = []
            for ledger in response_json:
                ledgers.append(Ledger(**ledger))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Ledger", str(exe)
            )
            raise

        return ledgers
