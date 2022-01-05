class Shopper:
    __user = None

    def __init__(self):
        pass

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def to_json(self):
        data = {
            "user": self.get_user()
        }
        return data
