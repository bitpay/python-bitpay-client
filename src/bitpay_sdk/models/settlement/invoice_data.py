from ...models.settlement.refund_info import RefundInfo


class InvoiceData:
    __order_id = None
    __date = None
    __price = None
    __currency = None
    __transaction_currency = None
    __over_paid_amount = None
    __payout_percentage = None
    __btc_price = None
    '''
    RefundInfo
    '''
    __refund_info = None

    def __init__(self):
        pass

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_transaction_currency(self):
        return self.__transaction_currency

    def set_transaction_currency(self, transaction_currency):
        self.__transaction_currency = transaction_currency

    def get_over_paid_amount(self):
        return self.__over_paid_amount

    def set_over_paid_amount(self, over_paid_amount):
        self.__over_paid_amount = over_paid_amount

    def get_payout_percentage(self):
        return self.__payout_percentage

    def set_payout_percentage(self, payout_percentage):
        self.__payout_percentage = payout_percentage

    def get_btc_price(self):
        return self.__btc_price

    def set_btc_price(self, btc_price):
        self.__btc_price = btc_price

    def get_refund_info(self):
        return self.__refund_info

    def set_refund_info(self, refund_info: RefundInfo):
        self.__refund_info = refund_info

    def to_json(self):
        data = {
            "orderId": self.get_order_id(),
            "date": self.get_date(),
            "price": self.get_price(),
            "currency": self.get_currency(),
            "transactionCurrency": self.get_transaction_currency(),
            "payoutPercentage": self.get_payout_percentage(),
            "refundInfo": self.get(),
            "btcPrice": self.get_id()
        }
        return data

