from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
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
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        if recipients.guid is None:
            recipients.guid = self.__guid_generator.execute()

        recipients.token = self.__token_container.get_access_token(Facade.PAYOUT)

        response = self.__bitpay_client.post("recipients", recipients.to_json(), True)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            recipients = []
            for recipient in response_json:
                recipients.append(PayoutRecipient(**recipient))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
            )

        return recipients

    def get(self, recipient_id: str) -> PayoutRecipient:
        """
        Retrieve a BitPay payout recipient by batch id using.The clients must have been
        previously authorized for the payout facade.

        :param str recipient_id: The id of the recipient to retrieve.
        :return: A BitPay PayoutRecipient object.
        :rtype: PayoutRecipient
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}
        response = self.__bitpay_client.get("recipients/%s" % recipient_id, params)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return PayoutRecipient(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
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
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {
            "token": self.__token_container.get_access_token(Facade.PAYOUT),
            "limit": str(limit),
            "offset": str(offset),
        }
        if status is not None:
            params["status"] = status

        response = self.__bitpay_client.get("recipients", params)
        response_json = ResponseParser.response_to_json_string(response)

        payout_recipients = []

        try:
            for payout_recipient in response_json:
                payout_recipients.append(PayoutRecipient(**payout_recipient))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
            )

        return payout_recipients

    def update(self, recipient_id: str, recipient: PayoutRecipient) -> PayoutRecipient:
        """
        Update a Payout Recipient.

        :param str recipient_id: The recipient id for the recipient to be updated.
        :param str recipient: A PayoutRecipient object with updated parameters defined.
        :return: The updated recipient object.
        :rtype: PayoutRecipient
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        recipient.token = self.__token_container.get_access_token(Facade.PAYOUT)
        recipient.guid = self.__guid_generator.execute()
        response = self.__bitpay_client.update(
            "recipients/%s" % recipient_id, recipient.to_json()
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            payout_recipient = PayoutRecipient(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
            )
            raise

        return payout_recipient

    def delete(self, recipient_id: str) -> bool:
        """
        Cancel a BitPay Payout recipient.

        :param str recipient_id: The id of the recipient to cancel.
        :return: True if the delete operation was successful, false otherwise.
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}

        try:
            response = self.__bitpay_client.delete(
                "recipients/%s" % recipient_id, params
            )
            response_json = ResponseParser.response_to_json_string(response)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
            )
            raise

        return response_json["status"].lower() == "success"

    def request_notification(self, recipient_id: str) -> bool:
        """
        Send a payout recipient notification

        :param str recipient_id: The id of the recipient to notify.
        :return: True if the notification was successfully sent, false otherwise.
        :rtype bool
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.PAYOUT)}

        try:
            response = self.__bitpay_client.post(
                "recipients/%s" % recipient_id + "/notifications", params
            )
            response_json = ResponseParser.response_to_json_string(response)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Payout Recipient", str(exe)
            )
            raise

        return response_json["status"].lower() == "success"
