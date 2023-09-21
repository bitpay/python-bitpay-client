from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.exceptions.payout_recipient_cancellation_exception import (
    PayoutRecipientCancellationException,
)
from bitpay.exceptions.payout_recipient_creation_exception import (
    PayoutRecipientCreationException,
)
from bitpay.exceptions.payout_recipient_notification_exception import (
    PayoutRecipientNotificationException,
)
from bitpay.exceptions.payout_recipient_query_exception import (
    PayoutRecipientQueryException,
)
from bitpay.exceptions.payout_recipient_update_exception import (
    PayoutRecipientUpdateException,
)
from bitpay.models.facade import Facade
from bitpay.models.payout.payout_recipient import PayoutRecipient
from bitpay.models.payout.payout_recipients import PayoutRecipients
from bitpay.utils.guid_generator import GuidGenerator
from bitpay.utils.token_container import TokenContainer


class PayoutRecipientClient:
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

    def submit(self, recipients: PayoutRecipients) -> List[PayoutRecipient]:
        """
        Submit BitPay Payout Recipients.

        :param PayoutRecipient recipients:
        :return: A PayoutRecipients object with request parameters defined.
        :rtype: [PayoutRecipient]
        :raises BitPayException
        :raises PayoutRecipientCreationException
        """
        try:
            if recipients.guid is None:
                recipients.guid = self.__guid_generator.execute()

            recipients.token = self.__token_container.get_access_token(Facade.PAYOUT)

            response_json = self.__bitpay_client.post(
                "recipients", recipients.to_json(), True
            )
        except BitPayException as exe:
            raise PayoutRecipientCreationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            recipients = []
            for recipient in response_json:
                recipients.append(PayoutRecipient(**recipient))
        except Exception as exe:
            raise PayoutRecipientCreationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return recipients

    def get(self, recipient_id: str) -> PayoutRecipient:
        """
        Retrieve a BitPay payout recipient by batch id using.The clients must have been
        previously authorized for the payout facade.

        :param str recipient_id: The id of the recipient to retrieve.
        :return: A BitPay PayoutRecipient object.
        :rtype: PayoutRecipient
        :raises BitPayException
        :raises PayoutRecipientQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
            response_json = self.__bitpay_client.get(
                "recipients/%s" % recipient_id, params
            )
        except BitPayException as exe:
            raise PayoutRecipientQueryException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return PayoutRecipient(**response_json)
        except Exception as exe:
            raise PayoutRecipientQueryException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )

    def get_recipients(
        self, status: Optional[str] = None, limit: int = 100, offset: int = 0
    ) -> List[PayoutRecipient]:
        """
        Retrieve a collection of BitPay Payout Recipients.

        :param str status: The recipient status you want to query on.
        :param int limit: Maximum results that the query will return (useful for paging results).
        :param int offset: Offset for paging
        :return: A list of BitPayRecipient objects.
        :rtype: [PayoutRecipient]
        :raises BitPayException
        :raises PayoutRecipientQueryException
        """
        try:
            params = {
                "token": self.__token_container.get_access_token(Facade.PAYOUT),
                "limit": str(limit),
                "offset": str(offset),
            }
            if status is not None:
                params["status"] = status

            response_json = self.__bitpay_client.get("recipients", params)
        except BitPayException as exe:
            raise PayoutRecipientQueryException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            payout_recipients = []
            for payout_recipient in response_json:
                payout_recipients.append(PayoutRecipient(**payout_recipient))
        except Exception as exe:
            raise PayoutRecipientQueryException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return payout_recipients

    def update(self, recipient_id: str, recipient: PayoutRecipient) -> PayoutRecipient:
        """
        Update a Payout Recipient.

        :param str recipient_id: The recipient id for the recipient to be updated.
        :param str recipient: A PayoutRecipient object with updated parameters defined.
        :return: The updated recipient object.
        :rtype: PayoutRecipient
        :raises BitPayException
        :raises PayoutRecipientUpdateException
        """
        try:
            recipient.token = self.__token_container.get_access_token(Facade.PAYOUT)
            recipient.guid = self.__guid_generator.execute()
            response_json = self.__bitpay_client.update(
                "recipients/%s" % recipient_id, recipient.to_json()
            )
        except BitPayException as exe:
            raise PayoutRecipientUpdateException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            payout_recipient = PayoutRecipient(**response_json)
        except Exception as exe:
            raise PayoutRecipientUpdateException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return payout_recipient

    def delete(self, recipient_id: str) -> bool:
        """
        Cancel a BitPay Payout recipient.

        :param str recipient_id: The id of the recipient to cancel.
        :return: True if the delete operation was successful, false otherwise.
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        except BitPayException as exe:
            raise PayoutRecipientCancellationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )
        try:
            response_json = self.__bitpay_client.delete(
                "recipients/%s" % recipient_id, params
            )
        except Exception as exe:
            raise PayoutRecipientCancellationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return response_json["status"].lower() == "success"

    def request_notification(self, recipient_id: str) -> bool:
        """
        Send a payout recipient notification

        :param str recipient_id: The id of the recipient to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype bool
        :raises BitPayException
        :raises PayoutRecipientNotificationException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        except BitPayException as exe:
            raise PayoutRecipientNotificationException(
                "failed to serialize PayoutRecipients object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            response_json = self.__bitpay_client.post(
                "recipients/%s" % recipient_id + "/notifications", params
            )
        except Exception as exe:
            raise PayoutRecipientNotificationException(
                "failed to deserialize BitPay server response "
                " (PayoutRecipients) : %s" % str(exe)
            )
        return response_json["status"].lower() == "success"
