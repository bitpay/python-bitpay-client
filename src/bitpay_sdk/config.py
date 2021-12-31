class Config:
    __environment = ""
    __envconfig = ""

    def __init__(self):
        pass

    def get_environment(self):
        return self.__environment

    def set_environment(self, environment):
        self.__environment = environment

    def get_envconfig(self):
        return self.__envconfig

    def set_envconfig(self, envconfig):
        self.__envconfig = envconfig
