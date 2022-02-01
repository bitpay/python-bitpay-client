"""
RefundParams
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class RefundParams:
    """
    Refund Params
    """

    __requester_type = ""
    __requester_email = ""
    __amount = 0.0
    __currency = ""
    __email = ""
    __purchaser_notify_email = ""
    __refund_address = ""
    __support_request_eid = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_requester_type(self):
        """
        Get method for the requester_type
        :return: requester_type
        """
        return self.__requester_type

    def set_requester_type(self, requester_type):
        """
        Set method for the requester_type
        :param requester_type: requester_type
        """
        self.__requester_type = requester_type

    def get_requester_email(self):
        """
        Get method for the requester_email
        :return: requester_email
        """
        return self.__requester_email

    def set_requester_email(self, requester_email):
        """
        Set method for the requester_email
        :param requester_email: requester_email
        """
        self.__requester_email = requester_email

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

    def get_email(self):
        """
        Get method for the email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for the email
        :param email: email
        """
        self.__email = email

    def get_purchaser_notify_email(self):
        """
        Get method for the purchaser_notify_email
        :return: purchaser_notify_email
        """
        return self.__purchaser_notify_email

    def set_purchaser_notify_email(self, purchaser_notify_email):
        """
        Set method for the purchaser_notify_email
        :param purchaser_notify_email: purchaser_notify_email
        """
        self.__purchaser_notify_email = purchaser_notify_email

    def get_refund_address(self):
        """
        Get method for the refund_address
        :return: refund_address
        """
        return self.__refund_address

    def set_refund_address(self, refund_address):
        """
        Set method for the refund_address
        :param refund_address: refund_address
        """
        self.__refund_address = refund_address

    def get_support_request_eid(self):
        """
        Get method for the support_request_eid
        :return: support_request_eid
        """
        return self.__support_request_eid

    def set_support_request_eid(self, support_request_eid):
        """
        Set method for the support_request_eid
        :param support_request_eid: support_request_eid
        """
        self.__support_request_eid = support_request_eid

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "requesterType": self.get_requester_type(),
            "requesterEmail": self.get_requester_email(),
            "amount": self.get_amount(),
            "currency": self.get_currency(),
            "email": self.get_email(),
            "purchaserNotifyEmail": self.get_purchaser_notify_email(),
            "refundAddress": self.get_refund_address(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
