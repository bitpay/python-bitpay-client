from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.exceptions.bill_creation_exception import BillCreationException
from bitpay.exceptions.bill_delivery_exception import BillDeliveryException
from bitpay.exceptions.bill_query_exception import BillQueryException
from bitpay.exceptions.bill_update_exception import BillUpdateException
from bitpay.exceptions.bitpay_exception import BitPayException
from bitpay.models.bill.bill import Bill
from bitpay.models.facade import Facade
from bitpay.utils.token_container import TokenContainer


class BillClient:
    __bitpay_client = BitPayClient
    __token_container = TokenContainer

    def __init__(
        self, bitpay_client: BitPayClient, token_container: TokenContainer
    ) -> None:
        self.__bitpay_client = bitpay_client
        self.__token_container = token_container

    def create(
        self, bill: Bill, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Bill:
        """
        Create a BitPay Bill.

        :param Bill bill: A Bill object with request parameters defined.
        :param str facade: The facade used to create it.
        :param bool sign_request: Signed request.
        :return: A BitPay generated Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillCreationException
        """
        try:
            bill.token = self.__token_container.get_access_token(facade)
            response_json = self.__bitpay_client.post(
                "bills", bill.to_json(), sign_request
            )
        except BitPayException as exe:
            raise BillCreationException(
                "failed to serialize bill object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return Bill(**response_json)
        except Exception as exe:
            raise BillCreationException(
                "failed to deserialize BitPay server response (Bill) : %s" % str(exe)
            )

    def get(
        self, bill_id: str, facade: Facade = Facade.MERCHANT, sign_request: bool = True
    ) -> Bill:
        """
        Retrieve a BitPay bill by bill id using the specified facade.

        :param str bill_id: The id of the bill to retrieve.
        :param str facade: The facade used to create it.
        :param bool sign_request: Signed request.
        :return: A BitPay Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(facade)}
            response_json = self.__bitpay_client.get(
                "bills/%s" % bill_id, params, sign_request
            )
        except BitPayException as exe:
            raise BillQueryException(
                "failed to serialize bill object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return Bill(**response_json)
        except Exception as exe:
            raise BillQueryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )

    def get_bills(self, status: Optional[str] = None) -> List[Bill]:
        """
        Retrieve a collection of BitPay bills.

        :param str status: The status to filter the bills.
        :return: A list of BitPay Bill objects.
        :rtype: [Bill]
        :raises BitPayException
        :raises BillQueryException
        """
        try:
            params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
            if status is not None:
                params["status"] = status
            response_json = self.__bitpay_client.get("bills", params, True)
        except BitPayException as exe:
            raise BillQueryException(
                "failed to serialize bill object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            bills = []
            for bill_data in response_json:
                bills.append(Bill(**bill_data))
        except Exception as exe:
            raise BillQueryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )

        return bills

    def update(self, bill: Bill, bill_id: str) -> Bill:
        """
        Update a BitPay Bill.

        :param Bill bill: A Bill object with the parameters to update defined.
        :param str bill_id: The Id of the Bill to update.
        :return: An updated Bill object.
        :rtype: Bill
        :raises BitPayException
        :raises BillUpdateException
        """
        try:
            if bill.token is None:
                raise BillUpdateException("missing Bill token")

            response_json = self.__bitpay_client.update(
                "bills/%s" % bill_id, bill.to_json()
            )
        except BitPayException as exe:
            raise BillUpdateException(
                "failed to serialize bill object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return Bill(**response_json)
        except Exception as exe:
            raise BillUpdateException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )

    def deliver(self, bill_id: str, bill_token: str) -> bool:
        """
        Deliver a BitPay Bill.

        :param str bill_id: The id of the requested bill.
        :param str bill_token: The token of the requested bill.
        :return: A response status returned from the API.
        :rtype: bool
        :raises BitPayException
        :raises BillDeliveryException
        """
        try:
            params = {"token": bill_token}
            response_json = self.__bitpay_client.post(
                "bills/%s" % bill_id + "/deliveries", params
            )
        except BitPayException as exe:
            raise BillDeliveryException(
                "failed to serialize bill object :  %s" % str(exe),
                api_code=exe.get_api_code(),
            )

        try:
            return response_json.lower() == "success"
        except Exception as exe:
            raise BillDeliveryException(
                "failed to deserialize BitPay server response" " (Bill) : %s" % str(exe)
            )
