from bitpay.client import Client
from bitpay.logger.bitpay_logger import BitPayLogger
from bitpay.logger.logger_provider import LoggerProvider


class UseLogger:

    def execute(self) -> None:
        LoggerProvider.set_logger(BitPayLogger())
        client = Client.create_pos_client(self, "someToken")

        client.get_invoice(self, "someId")
