from typing import List

from bitpay.client.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.settlement_query_exception import SettlementQueryException
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
        currency: str = None,
        date_start: str = None,
        date_end: str = None,
        status: str = None,
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
        :raises BitPayException
        :raises SettlementQueryException
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "limit": limit,
                "offset": offset,
            }

            if date_start is not None:
                params["dateStart"] = date_start

            if date_end is not None:
                params["dateEnd"] = date_end

            if currency is not None:
                params["currency"] = currency

            if status is not None:
                params["status"] = status

            response_json = self.__bitpay_client.get("settlements", params)
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlements = []
            for settlement in response_json:
                settlements.append(Settlement(**settlement))
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlements

    def get(self, settlement_id: str) -> Settlement:
        """
        Retrieves a summary of the specified settlement.

        :param str settlement_id: Settlement Id
        :return: A BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.get(
                "settlements/%s" % settlement_id, params
            )
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlement

    def get_reconciliation_report(self, settlement: Settlement) -> Settlement:
        """
        Gets a detailed reconciliation report of the activity within the settlement period

        :param Settlement settlement: Settlement to generate report for.
        :return: A detailed BitPay Settlement object.
        :rtype: Settlement
        :raises BitPayException
        :raises SettlementQueryException
        """
        try:
            params = {"token": settlement.get_token()}
            response_json = self.__bitpay_client.get(
                "settlements/%s" % settlement.get_id() + "/reconciliationReport", params
            )
        except BitPayException as exe:
            raise SettlementQueryException(
                "failed to serialize Settlement object :  %s" % str(exe),
                exe.get_api_code(),
            )

        try:
            settlement = Settlement(**response_json)
        except Exception as exe:
            raise SettlementQueryException(
                "failed to deserialize BitPay server response "
                " (Settlement) : %s" % str(exe)
            )
        return settlement
