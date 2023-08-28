from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.refund_cancellation_exception import RefundCancellationException
from bitpay.exceptions.refund_creation_exception import RefundCreationException
from bitpay.exceptions.refund_notification_exception import RefundNotificationException
from bitpay.exceptions.refund_query_exception import RefundQueryException
from bitpay.exceptions.refund_update_exception import RefundUpdateException
from bitpay.models.facade import Facade
from bitpay.models.invoice.refund import Refund
from bitpay.utils.guid_generator import GuidGenerator
from bitpay.utils.token_container import TokenContainer


class RefundClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer
    __guid_generator = GuidGenerator

    def __init__(
        self,
        bitpay_client: BitPayClient,
        token_container: TokenContainer,
        guid_generator: GuidGenerator,
    ):
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container
        self.__guid_generator = guid_generator

    def create(
        self,
        invoice_id: str,
        amount: float,
        preview: bool = False,
        immediate: bool = False,
        buyer_pays_refund_fee: bool = False,
        reference: Optional[str] = None,
        guid: Optional[str] = None,
    ) -> Refund:
        """
        Create a refund for a BitPay invoice.

        :param str invoice_id: The BitPay invoice Id having the associated refund to be created.
        :param float amount: Amount to be refunded in the currency indicated.
        :param bool preview: Whether to create the refund request as a preview (which will not be
         acted on until status is updated)
        :param bool immediate: Whether funds should be removed from merchant ledger immediately on
        submission or at time of processing
        :param bool buyer_pays_refund_fee: Whether the buyer should pay the refund fee (default is
        merchant)
        :param str reference: Present only if specified in the request to create the refund.
        This is your reference label for this refund. It will be passed-through on each response for you to identify
        the refund in your system. Maximum string length is 100 characters.
        :param str guid: Variable provided by the merchant and designed to be used by the merchant
        to correlate the refund with a refund ID in their system.
        :return: An updated Refund Object
        :rtype: Refund
        :raises BitPayException
        :raises RefundCreationException
        """
        try:
            if guid is None:
                guid = self.__guid_generator.execute()

            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "invoiceId": invoice_id,
                "guid": guid,
                "amount": amount,
                "preview": preview,
                "immediate": immediate,
                "buyerPaysRefundFee": buyer_pays_refund_fee,
            }

            if reference is not None:
                params["reference"] = reference

            response_json = self.__bitpay_client.post("refunds", params, True)
        except BitPayException as exe:
            raise RefundCreationException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundCreationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundCreationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def get(self, refund_id: str) -> Refund:
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.get("refunds/%s" % refund_id, params)
        except BitPayException as exe:
            raise RefundQueryException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundQueryException("failed to serialize refund object : %s" % exe)
        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundQueryException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def get_by_guid(self, guid: str) -> Refund:
        """
        Retrieve a previously made refund request on a BitPay invoice.

        :param str guid: The BitPay refund GUID.
        :return: BitPay Refund object with the associated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.get("refunds/guid/%s" % guid, params)
        except BitPayException as exe:
            raise RefundQueryException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundQueryException("failed to serialize refund object : %s" % exe)
        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundQueryException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def get_refunds(self, invoice_id: str) -> List[Refund]:
        """
        Retrieve a previously made refund request on a BitPay invoice.

        :param str invoice_id: The BitPay refund ID.
        :return: BitPay Refund object with the associated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundQueryException
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "invoiceId": invoice_id,
            }
            response_json = self.__bitpay_client.get("refunds", params)
        except BitPayException as exe:
            raise RefundQueryException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundQueryException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            refunds = []
            for refund_data in response_json:
                refunds.append(Refund(**refund_data))
        except Exception as exe:
            raise RefundQueryException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

        return refunds

    def update(self, refund_id: str, status: str) -> Refund:
        """
        Update the status of a BitPay invoice refund.

        :param str refund_id: BitPay refund ID.
        :param str status: The new status for the refund to be updated
        :return: A BitPay generated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundUpdateException
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "status": status,
            }

            response_json = self.__bitpay_client.update(
                "refunds/%s" % refund_id, params
            )
        except BitPayException as exe:
            raise RefundUpdateException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundUpdateException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundUpdateException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def update_by_guid(self, refund_guid: str, status: str) -> Refund:
        """
        Update the status of a BitPay invoice refund.

        :param str refund_guid: BitPay refund GUID.
        :param str status: The new status for the refund to be updated
        :return: A BitPay generated Refund object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundUpdateException
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.MERCHANT),
                "status": status,
            }

            response_json = self.__bitpay_client.update(
                "refunds/guid/%s" % refund_guid, params
            )
        except BitPayException as exe:
            raise RefundUpdateException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundUpdateException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundUpdateException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def cancel(self, refund_id: str) -> Refund:
        """
        Cancel a previously submitted refund request on a BitPay invoice.

        :param str refund_id: The refund Id for the refund to be canceled.
        :return: Cancelled refund Object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundCancellationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.delete(
                "refunds/%s" % refund_id, params
            )
        except BitPayException as exe:
            raise RefundCancellationException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundCancellationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundCancellationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def cancel_by_guid(self, guid: str) -> Refund:
        """
        Cancel a previously submitted refund request on a BitPay invoice.

        :param str guid: The refund GUID for the refund to be canceled.
        :return: Cancelled refund Object.
        :rtype: Refund
        :raises BitPayException
        :raises RefundCancellationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.delete(
                "refunds/guid/%s" % guid, params
            )
        except BitPayException as exe:
            raise RefundCancellationException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundCancellationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return Refund(**response_json)
        except Exception as exe:
            raise RefundCancellationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )

    def request_notification(self, refund_id: str) -> bool:
        """
        Send a refund notification.

        :param str refund_id: BitPay refund ID to notify.
        :return: True if the webhook was successfully requested, false otherwise.
        :rtype: bool
        :raises BitPayException
        :raises RefundNotificationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            response_json = self.__bitpay_client.post(
                "refunds/%s" % refund_id + "/notifications", params, True
            )
        except BitPayException as exe:
            raise RefundNotificationException(
                "failed to serialize refund object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        except Exception as exe:
            raise RefundNotificationException(
                "failed to serialize refund object : %s" % str(exe)
            )

        try:
            return response_json["status"].lower() == "success"
        except Exception as exe:
            raise RefundNotificationException(
                "failed to deserialize BitPay server response"
                " (Refund) : %s" % str(exe)
            )
