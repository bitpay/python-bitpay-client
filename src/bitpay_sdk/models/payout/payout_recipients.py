from .payout_recipient import PayoutRecipient


class PayoutRecipients:
    __guid = ""
    __recipients = []
    __token = ""

    def __init__(self):
        pass

    def get_guid(self):
        """
        Get method for guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid):
        """
        Set method for guid
        :param guid: guid
        """
        self.__guid = guid

    def get_token(self):
        """
        Get method for token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for token
        :param token: token
        """
        self.__token = token

    def get_recipients(self):
        """
        Get method for recipients
        :return: recipients
        """
        return self.__recipients

    def set_recipients(self, recipients: PayoutRecipient):
        """
        Set method for recipients
        :param recipients: recipients
        """
        self.__recipients = recipients

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "guid": self.get_guid(),
            "token": self.get_token(),
            "recipients": self.get_recipients()
        }
        return data
