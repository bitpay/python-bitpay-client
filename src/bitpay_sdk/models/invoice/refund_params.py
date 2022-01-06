class RefundParams(object):

    __requester_type = ""
    __requester_email = ""
    __amount = 0.0
    __currency = ""
    __email = ""
    __purchaser_notify_email = ""
    __refund_address = ""
    __support_request_eid = ""

    def __init__(self):
        pass

    def get_requester_type(self):
        return self.__requester_type

    def set_requester_type(self, requester_type):
        self.__requester_type = requester_type

    def get_requester_email(self):
        return self.__requester_email

    def set_requester_email(self, requester_email):
        self.__requester_email = requester_email

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_purchaser_notify_email(self):
        return self.__purchaser_notify_email

    def set_purchaser_notify_email(self, purchaser_notify_email):
        self.__purchaser_notify_email = purchaser_notify_email

    def get_refund_address(self):
        return self.__refund_address

    def set_refund_address(self, refund_address):
        self.__refund_address = refund_address

    def get_support_request_eid(self):
        return self.__support_request_eid

    def set_support_request_eid(self, support_request_eid):
        self.__support_request_eid = support_request_eid

    def to_json(self):
        data = {
            # TODO: Add more data
            "requesterType": self.get_requester_type(),
            "requesterEmail": self.get_requester_email(),
            "amount": self.get_amount(),
            "currency": self.get_currency(),
            "email": self.get_email(),
            "purchaserNotifyEmail": self.get_purchaser_notify_email(),
            "refundAddress": self.get_refund_address(),
        }

        return data
