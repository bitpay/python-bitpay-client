class Item:
    __id = None
    __description = None
    __price = None
    __quantity = None

    def __init__(self):
        pass

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def to_json(self):
        data = {
            "id": self.get_id(),
            "description": self.get_description(),
            "price": self.get_price(),
            "quantity": self.get_quantity(),
        }
        return data


