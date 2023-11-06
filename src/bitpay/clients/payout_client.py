from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.models.facade import Facade
from bitpay.models.payout.payout import Payout
from bitpay.models.payout.payout_group import PayoutGroup
from bitpay.models.payout.payout_group_failed import PayoutGroupFailed
from bitpay.utils.token_container import TokenContainer


class PayoutClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer

    def __init__(self, bitpay_client: BitPayClient, token_container: TokenContainer):
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container

    def submit(self, payout: Payout) -> Payout:
        """
        Submit a BitPay Payout.

        :param Payout payout: A Payout object with request parameters defined.
        :return: A BitPay generated Payout object.
        :rtype: Payout
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        payout.token = self.__token_container.get_access_token(Facade.PAYOUT)
        response = self.__bitpay_client.post("payouts", payout.to_json(), True)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout", str(exe)
            )
            raise

        return payout

    def get(self, payout_id: str) -> Payout:
        """
        Retrieve a BitPay payout by payout id using.The clients must have been
        previously authorized for the payout facade.

        :param str payout_id: The id of the payout to retrieve.
        :return: A BitPay generated Payout object.
        :rtype Payout
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        response = self.__bitpay_client.get("payouts/%s" % payout_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout", str(exe)
            )
            raise

        return payout

    def get_payouts(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[str] = None,
        reference: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[Payout]:
        """
        Retrieve a collection of BitPay payouts.

        :param str start_date: The start date for the query.
        :param str end_date: The end date for the query.
        :param str status: The status to filter (optional).
        :param str reference: The optional reference specified at payout request creation.
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Offset for paging
        :return: A list of BitPay Payout objects.
        :rtype [Payout]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        if status is not None:
            params["status"] = status
        if reference is not None:
            params["reference"] = reference
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        response = self.__bitpay_client.get("payouts", params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            payouts = []
            for payout in response_json:
                payouts.append(Payout(**payout))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout", str(exe)
            )
            raise

        return payouts

    def cancel(self, payout_id: str) -> bool:
        """
        Cancel a BitPay Payout.

        :param str payout_id: The id of the payout to cancel.
        :return: True if payout was successfully canceled, false otherwise.
        :rtype: bool
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        response = self.__bitpay_client.delete("payouts/%s" % payout_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return response_json["status"].lower() == "success"
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout", str(exe)
            )
            raise

    def request_notification(self, payout_id: str) -> bool:
        """
        Send a payout notification

        :param str payout_id: The id of the payout to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype: bool
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        response = self.__bitpay_client.post(
            "payouts/%s" % payout_id + "/notifications", params
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return response_json["status"].lower() == "success"
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout", str(exe)
            )
            raise

    @staticmethod
    def get_payout_group_response(
        response_json: dict, response_type: str
    ) -> PayoutGroup:
        payouts = []
        for payout in response_json[response_type]:
            payouts.append(Payout(**payout))

        try:
            failed = []
            for fail in response_json["failed"]:
                failed.append(PayoutGroupFailed(**fail))

            return PayoutGroup(payouts=payouts, failed=failed)
        except Exception:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "Unable to parse payouts"
            )

    def create_group(self, payouts: List[Payout]) -> PayoutGroup:
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        instructions = []

        for payout in payouts:
            instructions.append(payout.to_json())

        params["instructions"] = instructions
        response = self.__bitpay_client.post("payouts/group", params)
        response_json = ResponseParser.response_to_json_string(response)
        return self.get_payout_group_response(response_json, "created")

    def cancel_group(self, group_id: str) -> PayoutGroup:
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        response = self.__bitpay_client.delete("payouts/group/" + group_id, params)
        response_json = ResponseParser.response_to_json_string(response)
        return self.get_payout_group_response(response_json, "cancelled")
