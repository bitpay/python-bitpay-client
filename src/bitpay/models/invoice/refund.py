"""
Refund
"""
from .refund_params import RefundParams
from ...utils import key_utils


class Refund:
    """
    Refund an invoice
    """

    __guid = None
    __refund_email = None
    __amount = None
    __currency = None
    __token = None
    __id = None
    __request_date = None
    __status = None
    __params = RefundParams()

    __invoice_id = None
    __preview = None
    __immediate = None
    __reference = None
    __buyer_pays_refund_fee = None
    __refund_fee = None
    __last_refund_notification = None
    __invoice = None

    def __init__(
        self,
        refund_email: str = "",
        amount: float = 0.0,
        currency: str = "",
        token: str = "",
        **kwargs
    ):
        self.set_refund_email(refund_email)
        self.set_amount(amount)
        self.set_currency(currency)
        self.set_token(token)

        for key, value in kwargs.items():
            try:
                if key in ["refundParams"]:
                    klass = globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(
                    self, "set_%s" % key_utils.change_camel_case_to_snake_case(key)
                )(value)
            except AttributeError:
                pass

    def get_guid(self):
        """
        Get method for the guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid):
        """
        Set method for the guid
        :param guid: guid
        """
        self.__guid = guid

    def get_invoice_id(self):
        """
        Get method for the invoice_id
        :return: invoice_id
        """
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        """
        Set method for the invoice_id
        :param invoice_id: invoice_id
        """
        self.__invoice_id = invoice_id

    def get_preview(self):
        """
        Get method for the preview
        :return: preview
        """
        return self.__preview

    def set_preview(self, preview):
        """
        Set method for the preview
        :param preview: preview
        """
        self.__preview = preview

    def get_immediate(self):
        """
        Get method for the immediate
        :return: immediate
        """
        return self.__immediate

    def set_immediate(self, immediate):
        """
        Set method for the immediate
        :param immediate: immediate
        """
        self.__immediate = immediate

    def get_reference(self):
        """
        Get method for the reference
        :return: reference
        """
        return self.__reference

    def set_reference(self, reference):
        """
        Set method for the reference
        :param reference: reference
        """
        self.__reference = reference

    def get_buyer_pays_refund_fee(self):
        """
        Get method for the buyer_pays_refund_fee
        :return: buyer_pays_refund_fee
        """
        return self.__buyer_pays_refund_fee

    def set_buyer_pays_refund_fee(self, buyer_pays_refund_fee):
        """
        Set method for the buyer_pays_refund_fee
        :param buyer_pays_refund_fee: buyer_pays_refund_fee
        """
        self.__buyer_pays_refund_fee = buyer_pays_refund_fee

    def get_refund_fee(self):
        """
        Get method for the refund_fee
        :return: refund_fee
        """
        return self.__refund_fee

    def set_refund_fee(self, refund_fee):
        """
        Set method for the refund_fee
        :param refund_fee: refund_fee
        """
        self.__refund_fee = refund_fee

    def get_last_refund_notification(self):
        """
        Get method for the last_refund_notification
        :return: last_refund_notification
        """
        return self.__last_refund_notification

    def set_last_refund_notification(self, last_refund_notification):
        """
        Set method for the last_refund_notification
        :param last_refund_notification: last_refund_notification
        """
        self.__last_refund_notification = last_refund_notification

    def get_invoice(self):
        """
        Get method for the invoice
        :return: invoice
        """
        return self.__invoice

    def set_invoice(self, invoice):
        """
        Set method for the invoice
        :param invoice: invoice
        """
        self.__invoice = invoice

    def get_refund_email(self):
        """
        Get method for the refund_email
        :return: refund_email
        """
        return self.__refund_email

    def set_refund_email(self, refund_email):
        """
        Set method for the refund_email
        :param refund_email: refund_email
        """
        self.__refund_email = refund_email

    def get_amount(self):
        """
        Get method for the amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount):
        """
        Set method for the amount
        :param amount: amount
        """
        self.__amount = amount

    def get_currency(self):
        """
        Get method for the currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for the currency
        :param currency: currency
        """
        self.__currency = currency

    def get_token(self):
        """
        Get method for the token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for the token
        :param token: token
        """
        self.__token = token

    def get_id(self):
        """
        Get method for the id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for the id
        :param id: id
        """
        self.__id = id

    def get_request_date(self):
        """
        Get method for the request_date
        :return: request_date
        """
        return self.__request_date

    def set_request_date(self, request_date):
        """
        Set method for the request_date
        :param request_date: request_date
        """
        self.__request_date = request_date

    def get_status(self):
        """
        Get method for the status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for the status
        :param status: status
        """
        self.__status = status

    def get_params(self):
        """
        Get method for the params
        :return: params
        """
        return self.__params

    def set_params(self, params: RefundParams):
        """
        Set method for the params
        :param params: params
        """
        self.__params = params

    def to_json(self):
        """
        :return: data in json
        """
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
            "reference": self.get_reference(),
            "preview": self.get_preview(),
            "invoiceId": self.get_invoice_id(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
