class CurrencyQr:
    __type = None
    __collapsed = None

    def __init__(self):
        pass

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_collapsed(self):
        return self.__collapsed

    def set_collapsed(self, collapsed):
        self.__collapsed = collapsed

    def to_json(self):
        data = {
            "type": self.get_type(),
            "collapsed": self.get_collapsed()
        }
        return data
