import json
import os

import pytest

from requests import Response, PreparedRequest

from bitpay.clients.response_parser import ResponseParser
from bitpay.exceptions.bitpay_api_exception import BitPayApiException


@pytest.mark.unit
def test_handle_multiple_errors(mocker):
    with pytest.raises(BitPayApiException) as exc_info:
        with open(
                os.path.abspath(os.path.dirname(__file__))
                + "/response_with_errors.json",
                "r",
        ) as file:
            response_json = json.load(file)
        request = mocker.Mock(spec=PreparedRequest)
        request.method = "POST"
        request.url = "https://some-url.com"
        response = mocker.Mock(spec=Response)
        response.request = request
        response.json.return_value = response_json
        ResponseParser.response_to_json_string(response)

    assert str(exc_info.value) == "Missing required parameter. Missing required parameter."
