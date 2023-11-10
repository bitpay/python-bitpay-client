import pytest

from bitpay.logger.bitpay_logger import BitPayLogger
from bitpay.logger.logger_provider import LoggerProvider

@pytest.mark.unit
def test_get_logger_should_returns_default_logger():
    assert isinstance(LoggerProvider.get_logger(), BitPayLogger)

@pytest.mark.unit
def test_set_logger():
    another_client = AnotherLogger()

    LoggerProvider.set_logger(another_client)

    assert isinstance(LoggerProvider.get_logger(), AnotherLogger)
    assert isinstance(LoggerProvider.get_logger(), AnotherLogger)


class AnotherLogger(BitPayLogger):
    def log_request(self, method: str, endpoint: str, json: str):
        super().log_request(method, endpoint, json)

    def log_response(self, method: str, endpoint: str, json: str):
        super().log_response(method, endpoint, json)

    def log_error(self, message: str):
        super().log_error(message)