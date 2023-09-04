from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.payout_cancellation_exception import PayoutCancellationException
from bitpay.exceptions.payout_creation_exception import PayoutCreationException
from bitpay.exceptions.payout_exception import PayoutException
from bitpay.exceptions.payout_notification_exception import PayoutNotificationException
from bitpay.exceptions.payout_query_exception import PayoutQueryException
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
        :raises BitPayException
        :raises PayoutCreationException
        """
        try:
            payout.token = self.__token_container.get_access_token(Facade.PAYOUT)
            response_json = self.__bitpay_client.post("payouts", payout.to_json(), True)
        except BitPayException as exe:
            raise PayoutCreationException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutCreationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payout

    def get(self, payout_id: str) -> Payout:
        """
        Retrieve a BitPay payout by payout id using.The clients must have been
        previously authorized for the payout facade.

        :param str payout_id: The id of the payout to retrieve.
        :return: A BitPay generated Payout object.
        :rtype Payout
        :raises BitPayException
        :raises PayoutQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
            response_json = self.__bitpay_client.get("payouts/%s" % payout_id, params)
        except BitPayException as exe:
            raise PayoutQueryException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            payout = Payout(**response_json)
        except Exception as exe:
            raise PayoutQueryException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
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
        :raises BitPayException
        :raises PayoutQueryException
        """
        try:
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

            response_json = self.__bitpay_client.get("payouts", params)
        except BitPayException as exe:
            raise PayoutQueryException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            payouts = []
            for payout in response_json:
                payouts.append(Payout(**payout))
        except Exception as exe:
            raise PayoutQueryException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )
        return payouts

    def cancel(self, payout_id: str) -> bool:
        """
        Cancel a BitPay Payout.

        :param str payout_id: The id of the payout to cancel.
        :return: True if payout was successfully canceled, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutCancellationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
            response_json = self.__bitpay_client.delete(
                "payouts/%s" % payout_id, params
            )
        except BitPayException as exe:
            raise PayoutCancellationException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return response_json["status"].lower() == "success"
        except Exception as exe:
            raise PayoutCancellationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )

    def request_notification(self, payout_id: str) -> bool:
        """
        Send a payout notification

        :param str payout_id: The id of the payout to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises PayoutNotificationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
            response_json = self.__bitpay_client.post(
                "payouts/%s" % payout_id + "/notifications", params
            )
        except BitPayException as exe:
            raise PayoutNotificationException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return response_json["status"].lower() == "success"
        except Exception as exe:
            raise PayoutNotificationException(
                "failed to deserialize BitPay server response "
                " (Payout) : %s" % str(exe)
            )

    @staticmethod
    def get_payout_group_response(
        response_json: dict, response_type: str
    ) -> PayoutGroup:
        try:
            payouts = []
            for payout in response_json[response_type]:
                payouts.append(Payout(**payout))

            failed = []
            for fail in response_json["failed"]:
                failed.append(PayoutGroupFailed(**fail))

            return PayoutGroup(payouts=payouts, failed=failed)
        except Exception:
            raise PayoutException("Unable to parse payouts")

    def create_group(self, payouts: List[Payout]) -> PayoutGroup:
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        instructions = []

        try:
            for payout in payouts:
                instructions.append(payout.to_json())

            params["instructions"] = instructions

            response_json = self.__bitpay_client.post("payouts/group", params)
            return self.get_payout_group_response(response_json, "created")
        except BitPayException as exe:
            raise PayoutCreationException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

    def cancel_group(self, group_id: str) -> PayoutGroup:
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        try:
            response_json = self.__bitpay_client.delete(
                "payouts/group/" + group_id, params
            )
            return self.get_payout_group_response(response_json, "cancelled")
        except BitPayException as exe:
            raise PayoutCancellationException(
                "failed to serialize Payout object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
