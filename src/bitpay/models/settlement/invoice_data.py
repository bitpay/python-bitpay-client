"""
InvoiceData: Object containing relevant information from the paid invoice
"""
from ...models.settlement.refund_info import RefundInfo
from ...utils.key_utils import change_camel_case_to_snake_case


class InvoiceData:
    """
    invoice data
    """

    __order_id = None
    __date = None
    __price = None
    __currency = None
    __transaction_currency = None
    __over_paid_amount = None
    __payout_percentage = None
    __buyer_email_address = None
    __btc_price = None
    """
    RefundInfo
    """
    __refund_info = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key in ["refundInfo"]:
                    klass = globals()[key[0].upper() + key[1:]]

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

    def get_order_id(self):
        """
        Get method for to order_id
        :return: order_id
        """
        return self.__order_id

    def set_order_id(self, order_id):
        """
        Set method for to order_id
        :param order_id: order_id
        """
        self.__order_id = order_id

    def get_buyer_email_address(self):
        """
        Get method for to buyer_email_address
        :return: buyer_email_address
        """
        return self.__buyer_email_address

    def set_buyer_email_address(self, buyer_email_address):
        """
        Set method for to buyer_email_address
        :param buyer_email_address: buyer_email_address
        """
        self.__buyer_email_address = buyer_email_address

    def get_date(self):
        """
        Get method for to date
        :return: date
        """
        return self.__date

    def set_date(self, date):
        """
        Set method for to date
        :param date: date
        """
        self.__date = date

    def get_price(self):
        """
        Get method for to price
        :return: price
        """
        return self.__price

    def set_price(self, price):
        """
        Set method for to price
        :param price: price
        """
        self.__price = price

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

    def get_over_paid_amount(self):
        """
        Get method for to over_paid_amount
        :return: over_paid_amount
        """
        return self.__over_paid_amount

    def set_over_paid_amount(self, over_paid_amount):
        """
        Set method for to over_paid_amount
        :param over_paid_amount: over_paid_amount
        """
        self.__over_paid_amount = over_paid_amount

    def get_payout_percentage(self):
        """
        Get method for to payout_percentage
        :return: payout_percentage
        """
        return self.__payout_percentage

    def set_payout_percentage(self, payout_percentage):
        """
        Set method for to payout_percentage
        :param payout_percentage: transaction_currency
        """
        self.__payout_percentage = payout_percentage

    def get_btc_price(self):
        """
        Get method for to btc_price
        :return: btc_price
        """
        return self.__btc_price

    def set_btc_price(self, btc_price):
        """
        Set method for to btc_price
        :param btc_price: btc_price
        """
        self.__btc_price = btc_price

    def get_refund_info(self):
        """
        Get method for to refund_info
        :return: refund_info
        """
        return self.__refund_info

    def set_refund_info(self, refund_info: RefundInfo):
        """
        Set method for to refund_info
        :param refund_info: refund_info
        """
        self.__refund_info = refund_info

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "orderId": self.get_order_id(),
            "date": self.get_date(),
            "price": self.get_price(),
            "currency": self.get_currency(),
            "transactionCurrency": self.get_transaction_currency(),
            "buyerEmailAddress": self.get_buyer_email_address(),
            "payoutPercentage": self.get_payout_percentage(),
            "refundInfo": self.get_refund_info().to_json(),
            "btcPrice": self.get_btc_price(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
