from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.facade import Facade
from bitpay.models.settlement.settlement import Settlement
from bitpay.utils.token_container import TokenContainer


class SettlementClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer

    def __init__(self, bitpay_client: BitPayClient, token_container: TokenContainer):
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container

    def get_settlements(
        self,
        currency: Optional[str] = None,
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> List[Settlement]:
        """
        Retrieves settlement reports for the calling merchant filtered by query. The `limit`
        and `offset` parameters specify pages for large query sets.

        :param str currency: The three digit currency string for the ledger to retrieve.
        :param str date_start: The start date for the query.
        :param str date_end: The end date for the query.
        :param str status: Can be `processing`, `completed`, or `failed`.
        :param int limit: Maximum number of settlements to retrieve.
        :param int offset: Offset for paging
        :return: A list of BitPay Settlement objects
        :rtype: [Settlement]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.MERCHANT),
            "limit": limit,
            "offset": offset,
        }

        if date_start is not None:
            params["startDate"] = date_start

        if date_end is not None:
            params["endDate"] = date_end

        if currency is not None:
            params["currency"] = currency

        if status is not None:
            params["status"] = status

        response = self.__bitpay_client.get("settlements", params, True)
        response_json = ResponseParser.response_to_json_string(response)

        settlements = []

        try:
            for settlement in response_json:
                settlements.append(Settlement(**settlement))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Settlement", str(exe)
            )

        return settlements

    def get(self, settlement_id: str) -> Settlement:
        """
        Retrieves a summary of the specified settlement.

        :param str settlement_id: Settlement Id
        :return: A BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
        response = self.__bitpay_client.get("settlements/%s" % settlement_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Settlement", str(exe)
            )
            raise

        return settlement

    def get_reconciliation_report(
        self, settlement_id: str, settlement_token: str
    ) -> Settlement:
        """
        Gets a detailed reconciliation report of the activity within the settlement period

        :param str settlement_id: Settlement id to generate report for.
        :param str settlement_token: Settlement token to generate report for.
        :return: A detailed BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": settlement_token}
        response = self.__bitpay_client.get(
            "settlements/%s" % settlement_id + "/reconciliationReport", params
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Settlement", str(exe)
            )
            raise

        return settlement
