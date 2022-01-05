class SupportedTransactionCurrency:
    __enabled = None

    def __init__(self):
        pass

    def get_enabled(self):
        return self.__enabled

    def set_enabled(self, enabled):
        self.__enabled = enabled

    def to_json(self):
        data = {
            "enabled": self.get_enabled(),
        }
        return data
