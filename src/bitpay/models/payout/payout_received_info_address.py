"""
PayoutReceivedInfoAddress
"""
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutReceivedInfoAddress:
    """
    PayoutReceivedInfoAddress
    """

    __address1 = None
    __address2 = None
    __locality = None
    __region = None
    __postal_code = None
    __country = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_address1(self):
        """
        Get method for to address1
        :return: address1
        """
        return self.__address1

    def set_address1(self, address1):
        """
        Set method for to address1
        :param address1: address1
        """
        self.__address1 = address1

    def get_address2(self):
        """
        Get method for to address2
        :return: address2
        """
        return self.__address2

    def set_address2(self, address2):
        """
        Set method for to address2
        :param address2: address2
        """
        self.__address2 = address2

    def get_locality(self):
        """
        Get method for to locality
        :return: locality
        """
        return self.__locality

    def set_locality(self, locality):
        """
        Set method for to locality
        :param locality: locality
        """
        self.__locality = locality

    def get_region(self):
        """
        Get method for to region
        :return: region
        """
        return self.__region

    def set_region(self, region):
        """
        Set method for to region
        :param region: region
        """
        self.__region = region

    def get_postal_code(self):
        """
        Get method for to postal_code
        :return: postal_code
        """
        return self.__postal_code

    def set_postal_code(self, postal_code):
        """
        Set method for to postal_code
        :param postal_code: postal_code
        """
        self.__postal_code = postal_code

    def get_country(self):
        """
        Get method for to country
        :return: country
        """
        return self.__country

    def set_country(self, country):
        """
        Set method for to country
        :param country: country
        """
        self.__country = country

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "address1": self.get_address1(),
            "address2": self.get_address2(),
            "locality": self.get_locality(),
            "region": self.get_region(),
            "postalCode": self.get_postal_code(),
            "country": self.get_country(),
        }
        return data
