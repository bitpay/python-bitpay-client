from datetime import datetime
from typing import Union

from pydantic import BaseModel, field_validator, ConfigDict

from bitpay.exceptions.bitpay_exception_provider import BitPayExceptionProvider
from bitpay.utils.model_util import ModelUtil


def snake_to_camel(snake_case: str) -> str:
    return ModelUtil.convert_snake_case_fields_to_camel_case(snake_case)


class BitPayModel(BaseModel):
    model_config = ConfigDict(alias_generator=snake_to_camel, populate_by_name=True)

    def to_json(self) -> dict:
        """
        :return: data in json
        """
        return self.model_dump(exclude_unset=True, by_alias=True)

    def serialize_datetime_to_iso8601(self, dt: datetime) -> str:
        return dt.isoformat(timespec="microseconds")[:-4] + "Z"

    @field_validator("currency", check_fields=False)
    def validate_currency(cls, currency_code: Union[str, None]) -> Union[str, None]:
        """
        :raises BitPayGenericException
        """
        from bitpay.models.currency import Currency

        if currency_code is None:
            return currency_code
        currency_code = currency_code.upper()
        if Currency.is_valid(currency_code) is False:
            BitPayExceptionProvider.throw_generic_exception_with_message(
                "currency code must be a type of Model.Currency"
            )
        return currency_code
