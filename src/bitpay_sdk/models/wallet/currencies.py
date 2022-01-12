from ...models.wallet.currency_qr import CurrencyQr
from ...utils import key_utils


class Currencies(object):
    __code = None
    __p2p = None
    __dapp_browser = None
    __pay_pro = None
    __qr = None
    __withdrawal_fee = None
    __wallet_connect = None
    __currencies = None

    def __init__(self, **kwargs):

        # TODO: Recheck
        for key, value in kwargs.items():
            try:
                if key in ["currencies"]:
                    klass = globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(self, 'set_%s' % key_utils.change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_p2p(self):
        return self.__p2p

    def set_p2p(self, p2p):
        self.__p2p = p2p

    def get_dapp_browser(self):
        return self.__dapp_browser

    def set_dapp_browser(self, dapp_browser):
        self.__dapp_browser = dapp_browser

    def get_pay_pro(self):
        return self.__pay_pro

    def set_pay_pro(self, pay_pro):
        self.__pay_pro = pay_pro

    def get_qr(self):
        return self.__qr

    def set_qr(self, qr: CurrencyQr):
        self.__qr = qr

    def get_withdrawal_fee(self):
        return self.__withdrawal_fee

    def set_withdrawal_fee(self, withdrawal_fee):
        self.__withdrawal_fee = withdrawal_fee

    def get_wallet_connect(self):
        return self.__wallet_connect

    def set_wallet_connect(self, wallet_connect):
        self.__wallet_connect = wallet_connect

    def to_json(self):
        data = {
            'code': self.get_code(),
            'p2p': self.get_p2p(),
            'dappBrowser': self.get_dapp_browser(),
            'paypro': self.get_pay_pro(),
            'qr': self.get_qr(),
            'withdrawalFee': self.get_withdrawal_fee(),
            'walletConnect': self.get_wallet_connect()
        }
        return data
