from bitpay.exceptions.bitpay_generic_exception import BitPayGenericException
from bitpay.logger.bitpay_logger import BitPayLogger


class LoggerProvider:
    __logger = None

    def __init__(self) -> None:
        raise BitPayGenericException("This class should not be instantiated.")

    @staticmethod
    def get_logger() -> BitPayLogger:
        if LoggerProvider.__logger is None:
            LoggerProvider.__logger = BitPayLogger()
        return LoggerProvider.__logger

    @staticmethod
    def set_logger(logger: BitPayLogger) -> None:
        LoggerProvider.__logger = logger
