from ...utils.key_utils import change_camel_case_to_snake_case


class Shopper(object):
    __user = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def to_json(self):
        data = {
            "user": self.get_user()
        }
        return data
