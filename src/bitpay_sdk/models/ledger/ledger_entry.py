from ...models.ledger.buyer import Buyer


class LedgerEntry:
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

    def __init__(self):
        pass

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_timestamp(self):
        return self.__timestamp

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_tx_type(self):
        return self.__tx_type

    def set_tx_type(self, tx_type):
        self.__tx_type = tx_type

    def get_scale(self):
        return self.__scale

    def set_scale(self, scale):
        self.__scale = scale

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_support_request(self):
        return self.__support_request

    def set_support_request(self, support_request):
        self.__support_request = support_request

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_invoice_id(self):
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        self.__invoice_id = invoice_id

    def get_buyer_fields(self):
        return self.__buyer_fields

    def set_buyer_fields(self, buyer_fields: Buyer):
        self.__buyer_fields = buyer_fields

    def get_invoice_amount(self):
        return self.__invoice_amount

    def set_invoice_amount(self, invoice_amount):
        self.__invoice_amount = invoice_amount

    def get_invoice_currency(self):
        return self.__invoice_currency

    def set_invoice_currency(self, invoice_currency):
        self.__invoice_currency = invoice_currency

    def get_transaction_currency(self):
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency):
        self.__transaction_currency = transaction_currency

    def to_json(self):
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
            "buyerFields": self.get_buyer_fields(),
            "invoiceAmount": self.get_invoice_amount(),
            "invoiceCurrency": self.get_invoice_currency(),
            "transactionCurrency": self.get_transaction_currency()
        }
        return data
