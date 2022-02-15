"""
Subscription: Subscriptions are repeat billing agreements with specific buyers.
BitPay sends bill emails to buyers identified in active subscriptions according
to the specified schedule.
"""
from .bill_data import BillData
from ...utils.key_utils import change_camel_case_to_snake_case


class Subscription:
    """
    Subscription
    """

    __id = None
    __status = None
    """
     BillData
    """
    __bill_data = None
    __schedule = None
    __next_delivery = None
    __created_date = None
    __token = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["billData"]:
                    klass = globals()[key[0].upper() + key[1:]]

                    if isinstance(value, list):
                        objs = []
                        for obj in value:
                            objs.append(klass(**obj))
                        value = objs
                    else:
                        value = klass(**value)
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_id(self):
        """
        Get method for the id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_status(self):
        """
        Get method for the status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_bill_data(self):
        """
        Get method for the bill_data
        :return: bill_data
        """
        return self.__bill_data

    def set_bill_data(self, bill_data: BillData):
        """
        Set method for to bill_data
        :param bill_data: bill_data
        """
        self.__bill_data = bill_data

    def get_schedule(self):
        """
        Get method for the schedule
        :return: schedule
        """
        return self.__schedule

    def set_schedule(self, schedule):
        """
        Set method for to schedule
        :param schedule: schedule
        """
        self.__schedule = schedule

    def get_next_delivery(self):
        """
        Get method for the next_delivery
        :return: next_delivery
        """
        return self.__next_delivery

    def set_next_delivery(self, next_delivery):
        """
        Set method for to next_delivery
        :param next_delivery: next_delivery
        """
        self.__next_delivery = next_delivery

    def get_created_date(self):
        """
        Get method for the created_date
        :return: created_date
        """
        return self.__created_date

    def set_created_date(self, created_date):
        """
        Set method for to created_date
        :param created_date: created_date
        """
        self.__created_date = created_date

    def get_token(self):
        """
        Get method for the token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "id": self.get_id(),
            "status": self.get_status(),
            "billData": self.get_bill_data().to_json(),
            "schedule": self.get_schedule(),
            "nextDelivery": self.get_next_delivery(),
            "createdDate": self.get_created_date(),
            "token": self.get_token(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
