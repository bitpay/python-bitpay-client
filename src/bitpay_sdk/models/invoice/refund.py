from .refund_params import RefundParams
from ...utils import key_utils


class Refund(object):

    __guid = None
    __refund_email = None
    __amount = None
    __currency = None
    __token = None
    __id = None
    __request_date = None
    __status = None
    __params = None

    __invoice_id = None
    __preview = None
    __immediate = None
    __buyer_pays_refund_fee = None
    __refund_fee = None
    __last_refund_notification = None
    __invoice = None

    def __init__(self, refund_email: str = "", amount: float = 0.0, currency: str = "", token: str = "", **kwargs):
        self.__refund_email = refund_email
        self.__amount = amount
        self.__currency = currency
        self.__token = token
        self.__params = RefundParams()

        for key, value in kwargs.items():
            try:
                if key in ["refundParams"]:
                    klass = globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(self, 'set_%s' % key_utils.change_camel_case_to_snake_case(key))(value)
            except AttributeError as e:
                print(e)

    def get_guid(self):
        return self.__guid

    def set_guid(self, guid):
        self.__guid = guid

    def get_invoice_id(self):
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        self.__invoice_id = invoice_id

    def get_preview(self):
        return self.__preview

    def set_preview(self, preview):
        self.__preview = preview

    def get_immediate(self):
        return self.__immediate

    def set_immediate(self, immediate):
        self.__immediate = immediate

    def get_buyer_pays_refund_fee(self):
        return self.__buyer_pays_refund_fee

    def set_buyer_pays_refund_fee(self, buyer_pays_refund_fee):
        self.__buyer_pays_refund_fee = buyer_pays_refund_fee

    def get_refund_fee(self):
        return self.__refund_fee

    def set_refund_fee(self, refund_fee):
        self.__refund_fee = refund_fee

    def get_last_refund_notification(self):
        return self.__last_refund_notification

    def set_last_refund_notification(self, last_refund_notification):
        self.__last_refund_notification = last_refund_notification

    def get_invoice(self):
        return self.__invoice

    def set_invoice(self, invoice):
        self.__invoice = invoice

    def get_refund_email(self):
        return self.__refund_email

    def set_refund_email(self, refund_email):
        self.__refund_email = refund_email

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_request_date(self):
        return self.__request_date

    def set_request_date(self, request_date):
        self.__request_date = request_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_params(self):
        return self.__params

    def set_params(self, params: RefundParams):
        self.__params = params

    def to_json(self):
        data = {
            "guid": self.get_guid(),
            "refundEmail": self.get_refund_email(),
            "amount": self.get_amount(),
            "currency": self.get_currency(),
            "token": self.get_token(),
            "id": self.get_id(),
            "requestDate": self.get_request_date(),
            "status": self.get_status(),
            "params": self.get_params(),
            "refundFee": self.get_refund_fee(),
            "buyerPaysRefundFee": self.get_buyer_pays_refund_fee(),
            "lastRefundNotification": self.get_last_refund_notification(),
            "invoice": self.get_invoice(),
            "immediate": self.get_immediate(),
            "preview": self.get_preview(),
            "invoiceId": self.get_invoice_id()
        }
        return data
