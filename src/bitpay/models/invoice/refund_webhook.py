"""
Refund Webhook
"""


class RefundWebhook:
    """
    Refund Webhook
    """

    __id = None
    __invoice = None
    __support_request = None
    __status = None
    __amount = None
    __currency = None
    __last_refund_notification = None
    __refund_fee = None
    __immediate = None
    __buyer_pays_refund_fee = None
    __request_date = None

    def __init__(self):
        pass

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

    def get_support_request(self):
        """
        Get method for the support_request
        :return: support_request
        """
        return self.__support_request

    def set_support_request(self, support_request):
        """
        Set method for the support_request
        :param support_request: support_request
        """
        self.__support_request = support_request

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

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "id": self.get_id(),
            "invoice": self.get_invoice(),
            "supportRequest": self.get_amount(),
            "status": self.get_currency(),
            "amount": self.get_amount(),
            "currency": self.get_id(),
            "lastRefundNotification": self.get_request_date(),
            "refundFee": self.get_status(),
            "immediate": self.get_immediate(),
            "buyerPaysRefundFee": self.get_refund_fee(),
            "requestDate": self.get_buyer_pays_refund_fee()
        }
        data = {key: value for key, value in data.items() if value}
        return data
