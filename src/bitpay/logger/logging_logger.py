import logging

from bitpay.logger.bitpay_logger import BitPayLogger


class LoggingLogger(BitPayLogger):
    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log_request(self, method: str, endpoint: str, json: dict) -> None:
        logging.info(
            "Request method: "
            + method
            + " Endpoint: "
            + endpoint
            + " Json: "
            + str(json)
        )

    def log_response(self, method: str, endpoint: str, json: dict) -> None:
        logging.info(
            "Response method: "
            + method
            + " Endpoint: "
            + endpoint
            + " Json: "
            + str(json)
        )

    def log_error(self, message: str) -> None:
        logging.error(message)
