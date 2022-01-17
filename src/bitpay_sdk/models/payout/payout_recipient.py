class PayoutRecipient:
    __email = None
    __label = None
    __notification_url = None

    __status = None
    __id = None
    __shopper_id = None
    __token = None

    def __init__(self, email, label, notification_url):
        self.__email = email
        self.__label = label
        self.__notification_url = notification_url

    def get_email(self):
        """
        Get method for email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_label(self):
        """
        Get method for to label
        :return: label
        """
        return self.__label

    def set_label(self, label):
        """
        Set method for to label
        :param label: label
        """
        self.__label = label

    def get_notification_url(self):
        """
        Get method for to notification_url
        :return: notification_url
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        Set method for to notification_url
        :param notification_url: notification_url
        """
        self.__notification_url = notification_url

    def get_status(self):
        """
        Get method for status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for status
        :param status: status
        """
        self.__status = status

    def get_id(self):
        """
        Get method for id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for id
        :param id: id
        """
        self.__id = id

    def get_shopper_id(self):
        """
        Get method for to shopper_id
        :return: shopper_id
        """
        return self.__shopper_id

    def set_shopper_id(self, shopper_id):
        """
        Set method for to shopper_id
        :param shopper_id: shopper_id
        """
        self.__shopper_id = shopper_id

    def get_token(self):
        """
        Get method for to token
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
            "email": self.get_email(),
            "label": self.get_label(),
            "notificationURL": self.get_notification_url(),
            "status": self.get_status(),
            "id": self.get_id(),
            "shopperId": self.get_shopper_id(),
            "token": self.get_token()
        }
        return data
