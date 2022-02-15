"""
SettlementLedgerEntry: ledger entries in the settlement,
"""
from .invoice_data import InvoiceData
from ...utils.key_utils import change_camel_case_to_snake_case


class SettlementLedgerEntry:
    """
    SettlementLedgerEntry
    """

    __code = None
    __invoice_id = None
    __amount = None
    __timestamp = None
    __description = None
    __reference = None
    __invoice_data = InvoiceData()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in [
                    "invoiceData",
                ]:
                    klass = globals()[key[0].upper() + key[1:]]
                    value = klass(**value)
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_code(self):
        """
        Get method for the code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for the code
        :param code: code
        """
        self.__code = code

    def get_invoice_id(self):
        """
        Get method for the invoice_id
        :return: invoice_id
        """
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        """
        Set method for the invoice_id
        :param invoice_id: invoice_id
        """
        self.__invoice_id = invoice_id

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

    def get_timestamp(self):
        """
        Get method for the timestamp
        :return: timestamp
        """
        return self.__timestamp

    def set_timestamp(self, timestamp):
        """
        Set method for the timestamp
        :param timestamp: timestamp
        """
        self.__timestamp = timestamp

    def get_description(self):
        """
        Get method for the description
        :return: description
        """
        return self.__description

    def set_description(self, description):
        """
        Set method for the description
        :param description: description
        """
        self.__description = description

    def get_reference(self):
        """
        Get method for the reference
        :return: reference
        """
        return self.__reference

    def set_reference(self, reference):
        """
        Set method for the reference
        :param reference: reference
        """
        self.__reference = reference

    def get_invoice_data(self):
        """
        Get method for the invoice_data
        :return: invoice_data
        """
        return self.__invoice_data

    def set_invoice_data(self, invoice_data: InvoiceData):
        """
        Set method for the invoice_data
        :param invoice_data: invoice_data
        """
        self.__invoice_data = invoice_data

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "code": self.get_code(),
            "invoiceId": self.get_invoice_id(),
            "amount": self.get_amount(),
            "timestamp": self.get_timestamp(),
            "description": self.get_description(),
            "reference": self.get_reference(),
            "invoiceData": self.get_invoice_data().to_json(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
