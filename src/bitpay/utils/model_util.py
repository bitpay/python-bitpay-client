# mypy: disable-error-code="misc, union-attr, assignment, arg-type"
from typing import Any

from bitpay.exceptions.bitpay_exception import BitPayException


class ModelUtil:
    @staticmethod
    def get_field_value(
        key: str, value: Any, singular_fields: dict, list_fields: dict
    ) -> Any:
        """
        :param: singular fields key as field name (eg. "amountPaid"), value as type (eg. "str", Wallet, "bool", "int")
        :param: list fields key as field name (eg. "amountPaid"), value as type (of list eg. "str" means List[str])
        """
        if key in singular_fields:
            object_type = singular_fields.get(key)

            if value is None:
                return value

            if object_type == "float":
                if isinstance(value, float):
                    return value
                return float(value)

            if object_type == "int":
                if isinstance(value, int):
                    return value
                return int(value)

            if object_type == "bool":
                if isinstance(value, bool):
                    return value
                return bool(value)

            if isinstance(value, dict):
                value = object_type(**value)

            if isinstance(value, list):
                raise BitPayException("Wrong type value of " + key)

            return value

        if key in list_fields:
            object_type = list_fields.get(key)

            if object_type == "dict":
                if isinstance(value, dict):
                    return value
                return {value}

            if object_type == "str" or object_type == "list":
                if isinstance(value, list):
                    result = []
                    for element in value:
                        result.append(str(element))
                    return result
                return [value]

            if isinstance(value, dict):
                return [object_type(**value)]

            if isinstance(value, list):
                objs = []
                for obj in value:
                    if isinstance(obj, object_type):
                        objs.append(obj)
                    else:
                        objs.append(object_type(**obj))
                return objs

            if isinstance(value, object):
                return [value]

            raise BitPayException("Wrong type value of " + key)

        return value

    @staticmethod
    def to_json(model: object) -> dict:
        result = {}
        fields = vars(model)
        for name, value in fields.items():
            if not value:
                continue

            key = ModelUtil.remove_class_name_from_name(model, name)
            key = ModelUtil.convert_snake_case_fields_to_camel_case(key)

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

    @staticmethod
    def remove_class_name_from_name(model: object, name: str) -> str:
        return name.replace("_" + type(model).__name__ + "__", "")
