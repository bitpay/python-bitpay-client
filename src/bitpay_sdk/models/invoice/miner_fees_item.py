class MinerFeesItem:
    __satoshis_per_byte = None
    __total_fee = None

    def __init__(self):
        pass

    def get_satoshis_per_byte(self):
        return self.__satoshis_per_byte

    def set_satoshis_per_byte(self, satoshis_per_byte):
        self.__satoshis_per_byte = satoshis_per_byte

    def get_total_fee(self):
        return self.__total_fee

    def set_total_fee(self, total_fee):
        self.__total_fee = total_fee

    def to_json(self):
        data = {
            "satoshisPerByte": self.get_satoshis_per_byte(),
            "totalFee": self.get_total_fee()
        }
        return data
