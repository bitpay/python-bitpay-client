from ...utils.key_utils import change_camel_case_to_snake_case


class MinerFeesItem(object):
    __satoshis_per_byte = None
    __total_fee = None
    __fiat_amount = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, 'set_%s' % change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_satoshis_per_byte(self):
        return self.__satoshis_per_byte

    def set_satoshis_per_byte(self, satoshis_per_byte):
        self.__satoshis_per_byte = satoshis_per_byte

    def get_total_fee(self):
        return self.__total_fee

    def set_total_fee(self, total_fee):
        self.__total_fee = total_fee

    def get_fiat_amount(self):
        return self.__fiat_amount

    def set_fiat_amount(self, fiat_amount):
        self.__fiat_amount = fiat_amount

    def to_json(self):
        data = {
            "satoshisPerByte": self.get_satoshis_per_byte(),
            "totalFee": self.get_total_fee(),
            "fiatAmount": self.get_fiat_amount()
        }
        return data
