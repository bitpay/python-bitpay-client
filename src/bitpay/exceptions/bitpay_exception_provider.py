from typing import Union

from bitpay.exceptions.bitpay_api_exception import BitPayApiException
from bitpay.exceptions.bitpay_generic_exception import BitPayGenericException
from bitpay.exceptions.bitpay_validation_exception import BitPayValidationException
from bitpay.logger.logger_provider import LoggerProvider


class BitPayExceptionProvider:
    @staticmethod
    def throw_generic_exception_with_message(message: str) -> None:
        BitPayExceptionProvider.log_error_message(message)
        raise BitPayGenericException(message)

    @staticmethod
    def throw_api_exception_with_message(
        message: str, code: Union[str, None] = None
    ) -> None:
        BitPayExceptionProvider.log_error_message(message)
        raise BitPayApiException(message, code)

    @staticmethod
    def throw_validation_exception(message: str) -> None:
        BitPayExceptionProvider.log_error_message(message)
        raise BitPayValidationException(message)

    @staticmethod
    def throw_missing_parameter_exception() -> None:
        message = "Missing required parameter"
        BitPayExceptionProvider.log_error_message(message)
        raise BitPayValidationException(message)

    @staticmethod
    def throw_deserialize_resource_exception(
        resource: str, exception_message: str
    ) -> None:
        message = "Failed to deserialize BitPay server response ( %s ) : %s" % (
            resource,
            exception_message,
        )
        BitPayExceptionProvider.throw_generic_exception_with_message(message)

    @staticmethod
    def throw_deserialize_exception(exception_message: str) -> None:
        message = "Failed to deserialize BitPay server response : " + exception_message
        BitPayExceptionProvider.throw_generic_exception_with_message(message)

    @staticmethod
    def throw_encode_exception(exception_message: str) -> None:
        message = "Failed to encode params : " + exception_message
        BitPayExceptionProvider.throw_generic_exception_with_message(message)

    @staticmethod
    def throw_serialize_resource_exception(
        resource: str, exception_message: str
    ) -> None:
        message = "Failed to serialize ( %s ) : %s" % (resource, exception_message)
        BitPayExceptionProvider.throw_generic_exception_with_message(message)

    @staticmethod
    def throw_serialize_params_exception(error_message: str) -> None:
        message = "Failed to serialize params : " + error_message
        BitPayExceptionProvider.throw_generic_exception_with_message(message)

    @staticmethod
    def throw_invalid_currency_exception(currency_code: str) -> None:
        message = "Currency code %s must be a type of Model.Currency" % currency_code
        BitPayExceptionProvider.throw_validation_exception(message)

    @staticmethod
    def log_error_message(message: str) -> None:
        LoggerProvider.get_logger().log_error(message)
