"""
Currencies
"""
from ...utils import key_utils
from ...models.wallet.currency_qr import CurrencyQr


class Currencies(object):
    """
    details of what currencies support payments for this wallet
    """

    __code = None
    __p2p = None
    __dapp_browser = None
    __pay_pro = None
    __qr = None
    __withdrawal_fee = None
    __wallet_connect = None
    __currencies = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["qr"]:
                    klass = CurrencyQr if key == "qr" else globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_code(self):
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_p2p(self):
        """
        Get method for to p2p
        :return: p2p
        """
        return self.__p2p

    def set_p2p(self, p2p):
        """
        Set method for to p2p
        :param p2p: p2p
        """
        self.__p2p = p2p

    def get_dapp_browser(self):
        """
        Get method for to dapp_browser
        :return: dapp_browser
        """
        return self.__dapp_browser

    def set_dapp_browser(self, dapp_browser):
        """
        Set method for to dapp_browser
        :param dapp_browser: dapp_browser
        """
        self.__dapp_browser = dapp_browser

    def get_pay_pro(self):
        """
        Get method for to pay_pro
        :return: pay_pro
        """
        return self.__pay_pro

    def set_pay_pro(self, pay_pro):
        """
        Set method for to pay_pro
        :param pay_pro: pay_pro
        """
        self.__pay_pro = pay_pro

    def get_qr(self):
        """
        Get method for to qr
        :return: qr
        """
        return self.__qr

    def set_qr(self, qr: CurrencyQr):
        """
        Set method for to qr
        :param qr: qr
        """
        self.__qr = qr

    def get_withdrawal_fee(self):
        """
        Get method for to withdrawal_fee
        :return: withdrawal_fee
        """
        return self.__withdrawal_fee

    def set_withdrawal_fee(self, withdrawal_fee):
        """
        Set method for to withdrawal_fee
        :param withdrawal_fee: withdrawal_fee
        """
        self.__withdrawal_fee = withdrawal_fee

    def get_wallet_connect(self):
        """
        Get method for to wallet_connect
        :return: wallet_connect
        """
        return self.__wallet_connect

    def set_wallet_connect(self, wallet_connect):
        """
        Set method for to wallet_connect
        :param wallet_connect: wallet_connect
        """
        self.__wallet_connect = wallet_connect

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "code": self.get_code(),
            "p2p": self.get_p2p(),
            "dappBrowser": self.get_dapp_browser(),
            "paypro": self.get_pay_pro(),
            "qr": self.get_qr(),
            "withdrawalFee": self.get_withdrawal_fee(),
            "walletConnect": self.get_wallet_connect(),
        }
        return data
