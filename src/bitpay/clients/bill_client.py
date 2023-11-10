from typing import List, Optional

from bitpay.clients.bitpay_client import BitPayClient
from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.exceptions.bitpay_generic_exception import BitPayGenericException
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
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        bill.token = self.__token_container.get_access_token(facade)
        response = self.__bitpay_client.post("bills", bill.to_json(), sign_request)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return Bill(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Bill", str(exe)
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
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(facade)}
        response = self.__bitpay_client.get("bills/%s" % bill_id, params, sign_request)
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return Bill(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Bill", str(exe)
            )

    def get_bills(self, status: Optional[str] = None) -> List[Bill]:
        """
        Retrieve a collection of BitPay bills.

        :param str status: The status to filter the bills.
        :return: A list of BitPay Bill objects.
        :rtype: [Bill]
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": self.__token_container.get_access_token(Facade.MERCHANT)}
        if status is not None:
            params["status"] = status
        response = self.__bitpay_client.get("bills", params, True)
        response_json = ResponseParser.response_to_json_string(response)

        bills = []

        try:
            for bill_data in response_json:
                bills.append(Bill(**bill_data))
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Bill", str(exe)
            )

        return bills

    def update(self, bill: Bill, bill_id: str) -> Bill:
        """
        Update a BitPay Bill.

        :param Bill bill: A Bill object with the parameters to update defined.
        :param str bill_id: The Id of the Bill to update.
        :return: An updated Bill object.
        :rtype: Bill
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        if bill.token is None:
            BitPayExceptionProvider.throw_missing_parameter_exception()

        response = self.__bitpay_client.update("bills/%s" % bill_id, bill.to_json())
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return Bill(**response_json)
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Bill", str(exe)
            )

    def deliver(self, bill_id: str, bill_token: str) -> bool:
        """
        Deliver a BitPay Bill.

        :param str bill_id: The id of the requested bill.
        :param str bill_token: The token of the requested bill.
        :return: A response status returned from the API.
        :rtype: bool
        :raises BitPayApiException
        :raises BitPayGenericException
        """
        params = {"token": bill_token}
        response = self.__bitpay_client.post(
            "bills/%s" % bill_id + "/deliveries", params
        )
        response_json = ResponseParser.response_to_json_string(response)

        try:
            return response_json.lower() == "success"
        except Exception as exe:
            BitPayExceptionProvider.throw_deserialize_resource_exception(
                "Bill", str(exe)
            )
            raise BitPayGenericException
