"""
class Config
"""


class Config:
    """
    class Config that set and get configurations
    """

    __environment = ""
    __envconfig = ""

    def __init__(self):
        pass

    def get_environment(self):
        """
        Get method for to environment
        :return: environment
        """
        return self.__environment

    def set_environment(self, environment):
        """
        Set method for to environment
        :param environment: environment
        """
        self.__environment = environment

    def get_envconfig(self):
        """
        Get method for to envconfig
        :return: envconfig
        """
        return self.__envconfig

    def set_envconfig(self, envconfig):
        """
        Set method for to envconfig
        :param envconfig: envconfig
        """
        self.__envconfig = envconfig
