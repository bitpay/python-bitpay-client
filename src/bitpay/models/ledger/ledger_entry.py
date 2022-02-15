"""
LedgerEntry
"""
from ...models.ledger.buyer import Buyer
from ...utils.key_utils import change_camel_case_to_snake_case


class LedgerEntry:
    """
    Ledger entry
    """

    __type = None
    __amount = None
    __code = None
    __timestamp = None
    __currency = None
    __tx_type = None
    __scale = None
    __id = None
    __support_request = None
    __description = None
    __invoice_id = None

    # Buyer
    __buyer_fields = Buyer()

    __invoice_amount = None
    __invoice_currency = None
    __transaction_currency = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["buyerFields"]:
                    klass = (
                        Buyer
                        if key == "buyerFields"
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

    def get_type(self):
        """
        Get method for to type
        :return: type
        """
        return self.__type

    def set_type(self, type):
        """
        Set method for to type
        :param type: type
        """
        self.__type = type

    def get_amount(self):
        """
        Get method for to amount
        :return: amount
        """
        return self.__amount

    def set_amount(self, amount):
        """
        Set method for to amount
        :param amount: amount
        """
        self.__amount = amount

    def get_code(self):
        """
        Get method for to code
        :return: code
        """
        return self.__code

    def set_code(self, code):
        """
        Set method for to code
        :param code: code
        """
        self.__code = code

    def get_timestamp(self):
        """
        Get method for to timestamp
        :return: timestamp
        """
        return self.__timestamp

    def set_timestamp(self, timestamp):
        """
        Set method for to timestamp
        :param timestamp: timestamp
        """
        self.__timestamp = timestamp

    def get_currency(self):
        """
        Get method for to currency
        :return: currency
        """
        return self.__currency

    def set_currency(self, currency):
        """
        Set method for to currency
        :param currency: currency
        """
        self.__currency = currency

    def get_tx_type(self):
        """
        Get method for to tx_type
        :return: tx_type
        """
        return self.__tx_type

    def set_tx_type(self, tx_type):
        """
        Set method for to tx_type
        :param tx_type: tx_type
        """
        self.__tx_type = tx_type

    def get_scale(self):
        """
        Get method for to scale
        :return: scale
        """
        return self.__scale

    def set_scale(self, scale):
        """
        Set method for to scale
        :param scale: scale
        """
        self.__scale = scale

    def get_id(self):
        """
        Get method for to id
        :return: id
        """
        return self.__id

    def set_id(self, id):
        """
        Set method for to id
        :param id: id
        """
        self.__id = id

    def get_support_request(self):
        """
        Get method for to support_request
        :return: support_request
        """
        return self.__support_request

    def set_support_request(self, support_request):
        """
        Set method for to support_request
        :param support_request: support_request
        """
        self.__support_request = support_request

    def get_description(self):
        """
        Get method for to description
        :return: description
        """
        return self.__description

    def set_description(self, description):
        """
        Set method for to description
        :param description: description
        """
        self.__description = description

    def get_invoice_id(self):
        """
        Get method for to invoice_id
        :return: invoice_id
        """
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        """
        Set method for to invoice_id
        :param invoice_id: invoice_id
        """
        self.__invoice_id = invoice_id

    def get_buyer_fields(self):
        """
        Get method for to buyer_fields
        :return: buyer_fields
        """
        return self.__buyer_fields

    def set_buyer_fields(self, buyer_fields: Buyer):
        """
        Set method for to buyer_fields
        :param buyer_fields: buyer_fields
        """
        self.__buyer_fields = buyer_fields

    def get_invoice_amount(self):
        """
        Get method for to invoice_amount
        :return: invoice_amount
        """
        return self.__invoice_amount

    def set_invoice_amount(self, invoice_amount):
        """
        Set method for to invoice_amount
        :param invoice_amount: invoice_amount
        """
        self.__invoice_amount = invoice_amount

    def get_invoice_currency(self):
        """
        Get method for to invoice_currency
        :return: invoice_currency
        """
        return self.__invoice_currency

    def set_invoice_currency(self, invoice_currency):
        """
        Set method for to invoice_currency
        :param invoice_currency: invoice_currency
        """
        self.__invoice_currency = invoice_currency

    def get_transaction_currency(self):
        """
        Get method for to transaction_currency
        :return: transaction_currency
        """
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency):
        """
        Set method for to transaction_currency
        :param transaction_currency: transaction_currency
        """
        self.__transaction_currency = transaction_currency

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "type": self.get_type(),
            "amount": self.get_amount(),
            "code": self.get_code(),
            "timestamp": self.get_timestamp(),
            "currency": self.get_currency(),
            "txType": self.get_tx_type(),
            "scale": self.get_scale(),
            "id": self.get_id(),
            "supportRequest": self.get_support_request(),
            "description": self.get_description(),
            "invoiceId": self.get_invoice_id(),
            "buyerFields": self.get_buyer_fields().to_json(),
            "invoiceAmount": self.get_invoice_amount(),
            "invoiceCurrency": self.get_invoice_currency(),
            "transactionCurrency": self.get_transaction_currency(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
