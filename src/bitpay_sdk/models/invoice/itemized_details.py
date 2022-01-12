from ...utils import key_utils


class ItemizedDetails:

    __amount = None
    __description = None
    __is_fee = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % key_utils.change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_is_fee(self):
        return self.__is_fee

    def set_is_fee(self, is_fee):
        self.__is_fee = is_fee

    def to_json(self):
        data = {
            "amount": self.get_amount(),
            "description": self.get_description(),
            "is_fee": self.get_is_fee()
        }
        return data
