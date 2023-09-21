# mypy: disable-error-code="misc, union-attr, assignment, arg-type"
from typing import Any

from bitpay.exceptions.bitpay_exception import BitPayException


class ModelUtil:
    @staticmethod
    def to_json(model: object) -> dict:
        result = {}
        fields = vars(model)
        for name, value in fields.items():
            if not value:
                continue

            key = ModelUtil.convert_snake_case_fields_to_camel_case(name)

            if isinstance(value, (int, float, str, bool)):
                result[key] = value
            elif isinstance(value, dict):
                result[key] = ModelUtil.to_json(value)
            elif isinstance(value, (list, tuple)):
                result[key] = []
                for item in value:
                    if isinstance(item, (int, float, str, bool)):
                        result[key].append(item)
                    else:
                        result[key].append(ModelUtil.to_json(item))
            else:
                result[key] = ModelUtil.to_json(value)

        return result

    @staticmethod
    def convert_snake_case_fields_to_camel_case(key: str) -> str:
        words = key.split("_")
        key = words[0] + "".join(word[:1].upper() + word[1:] for word in words[1:])
        return key
