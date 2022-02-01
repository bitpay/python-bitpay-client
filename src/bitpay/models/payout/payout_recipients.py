"""
PayoutRecipients
"""
from .payout_recipient import PayoutRecipient
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutRecipients:
    """
    PayoutRecipients
    """

    __guid = ""
    __recipients = []
    __token = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in [
                    "recipients",
                ]:
                    klass = (
                        PayoutRecipient
                        if key == "recipients"
                        else globals()[key[0].upper() + key[1:]]
                    )
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

    def set_recipients(self, recipients: [PayoutRecipient]):
        """
        Set method for recipients
        :param recipients: recipients
        """
        self.__recipients = recipients

    def to_json(self):
        """
        :return: data in json
        """
        recipients = []
        for recipient in self.get_recipients():
            recipients.append(recipient.to_json())
        data = {
            "guid": self.get_guid(),
            "token": self.get_token(),
            "recipients": recipients,
        }
        data = {key: value for key, value in data.items() if value}
        return data
