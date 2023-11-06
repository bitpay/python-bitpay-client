from typing import Any

from requests import Response

from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.logger.logger_provider import LoggerProvider


class ResponseParser:
    @staticmethod
    def response_to_json_string(response: Response) -> Any:
        """
        :raises BitPayApiException
        """
        if not response.json():
            BitPayExceptionProvider.throw_api_exception_with_message(
                "HTTP response is null"
            )

        response_obj = response.json()

        request = response.request
        LoggerProvider.get_logger().log_response(
            request.method, request.url, response_obj
        )

        if "status" in response_obj:
            if response_obj["status"] == "error":
                BitPayExceptionProvider.throw_api_exception_with_message(
                    response_obj["error"], response_obj["code"]
                )

        if "error" in response_obj:
            BitPayExceptionProvider.throw_api_exception_with_message(
                response_obj["error"]
            )

        if "success" in response_obj:
            return response_obj["success"]

        if "data" in response_obj:
            return response_obj["data"]

        return response_obj
