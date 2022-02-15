"""
PayoutBatch
"""
from .payout_instruction import PayoutInstruction
from ..currency import Currency
from ...exceptions.bitpay_exception import BitPayException
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutBatch:
    """
    PayoutBatch
    """

    __token = ""

    __amount = 0.0
    __currency = ""
    __effective_date = None
    __instructions = []
    __ledger_currency = ""

    __reference = ""
    __notification_URL = ""
    __notification_email = ""
    __email = ""
    __recipient_id = ""
    __shopper_id = ""
    __label = ""
    __message = ""
    __redirect_url = None
    __id = None
    __account = None
    __support_phone = None
    __status = None
    __percent_fee = None
    __fee = None
    __deposit_total = None
    __rate = None
    __btc = None
    __request_date = None
    __date_executed = None
    __exchange_rates = None
    __ignore_emails = None
    __guid = None

    def __init__(
        self, currency=None, effective_date=None, ledger_currency=None, **kwargs
    ):
        self.set_effective_date(effective_date)
        if currency:
            self.set_currency(currency)
        if ledger_currency:
            self.set_ledger_currency(ledger_currency)

        for key, value in kwargs.items():
            try:
                if key in ["instructions"]:

                    klass = (
                        PayoutInstruction
                        if key == "instructions"
                        else globals()[key[0].upper() + key[1:]]
                    )

                    if isinstance(value, list):
                        objs = []
                        for obj in value:
                            obj["method"] = 100  # Just skip the method check
                            obj["method_value"] = None
                            objs.append(klass(**obj))
                        value = objs
                    else:
                        value = klass(**value)
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass
        self.compute_and_set_amount()

    def compute_and_set_amount(self):
        amount = 0.0
        if self.__instructions:
            for instruction in self.__instructions:
                instruction_amount = instruction.get_amount()
                if instruction_amount:
                    amount += instruction_amount
        self.__amount = amount

    def get_instructions(self) -> [PayoutInstruction]:
        """
        Get method for to instructions
        :return: instructions
        """
        return self.__instructions

    def set_instructions(self, instructions: [PayoutInstruction]):
        """
        Set method for to instructions
        :param instructions: instructions
        """
        self.__instructions = instructions
        self.compute_and_set_amount()

    def get_token(self):
        """
        Get method for to token
        :return: token
        """
        return self.__token

    def set_token(self, token):
        """
        Set method for to token
        :param token: token
        """
        self.__token = token

    def get_guid(self):
        """
        Get method for to guid
        :return: guid
        """
        return self.__guid

    def set_guid(self, guid):
        """
        Set method for to guid
        :param guid: guid
        """
        self.__guid = guid

    def get_ignore_emails(self):
        """
        Get method for to ignore_emails
        :return: ignore_emails
        """
        return self.__ignore_emails

    def set_ignore_emails(self, ignore_emails):
        """
        Set method for to ignore_emails
        :param ignore_emails: ignore_emails
        """
        self.__ignore_emails = ignore_emails

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
        if not Currency.is_valid(currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__currency = currency

    def get_effective_date(self):
        """
        Get method for to effective_date
        :return: effective_date
        """
        return self.__effective_date

    def set_effective_date(self, effective_date):
        """
        Set method for to effective_date
        :param effective_date: effective_date
        """
        self.__effective_date = effective_date

    def get_reference(self):
        """
        Get method for to reference
        :return: reference
        """
        return self.__reference

    def set_reference(self, reference):
        """
        Set method for to reference
        :param reference: reference
        """
        self.__reference = reference

    def get_notification_email(self):
        """
        Get method for to notification_email
        :return: notification_email
        """
        return self.__notification_email

    def set_notification_email(self, notification_email):
        """
        Set method for to notification_email
        :param notification_email: notification_email
        """
        self.__notification_email = notification_email

    def get_notification_u_r_l(self):
        """
        Get method for to notification_URL
        :return: notification_URL
        """
        return self.__notification_URL

    def set_notification_u_r_l(self, notification_URL):
        """
        Set method for to notification_URL
        :param notification_URL: notification_URL
        """
        self.__notification_URL = notification_URL

    def get_redirect_url(self):
        """
        Get method for to redirect_url
        :return: redirect_url
        """
        return self.__redirect_url

    def set_redirect_url(self, redirect_url):
        """
        Set method for to redirect_url
        :param redirect_url: redirect_url
        """
        self.__redirect_url = redirect_url

    def get_ledger_currency(self):
        """
        Get method for to ledger_currency
        :return: ledger_currency
        """
        return self.__ledger_currency

    def set_ledger_currency(self, ledger_currency):
        """
        Set method for to ledger_currency
        :param ledger_currency: ledger_currency
        """
        if not Currency.is_valid(ledger_currency):
            raise BitPayException("currency code must be a type of Model.Currency")
        self.__ledger_currency = ledger_currency

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

    def get_shopper_id(self):
        """
        Get method for to shopper_id
        :return: shopper_id
        """
        return self.__shopper_id

    def set_shopper_id(self, shopper_id):
        """
        Set method for to shopper_id
        :param shopper_id: shopper_id
        """
        self.__shopper_id = shopper_id

    def get_recipient_id(self):
        """
        Get method for to recipient_id
        :return: recipient_id
        """
        return self.__recipient_id

    def set_recipient_id(self, recipient_id):
        """
        Set method for to recipient_id
        :param recipient_id: recipient_id
        """
        self.__recipient_id = recipient_id

    def get_exchange_rates(self):
        """
        Get method for to exchange_rates
        :return: exchange_rates
        """
        return self.__exchange_rates

    def set_exchange_rates(self, exchange_rates: PayoutInstruction):
        """
        Set method for to exchange_rates
        :param exchange_rates: exchange_rates
        """
        self.__exchange_rates = exchange_rates

    def get_account(self):
        """
        Get method for to account
        :return: account
        """
        return self.__account

    def set_account(self, account):
        """
        Set method for to account
        :param account: account
        """
        self.__account = account

    def get_email(self):
        """
        Get method for to email
        :return: email
        """
        return self.__email

    def set_email(self, email):
        """
        Set method for to email
        :param email: email
        """
        self.__email = email

    def get_label(self):
        """
        Get method for to label
        :return: label
        """
        return self.__label

    def set_label(self, label):
        """
        Set method for to label
        :param label: label
        """
        self.__label = label

    def get_support_phone(self):
        """
        Get method for to support_phone
        :return: support_phone
        """
        return self.__support_phone

    def set_support_phone(self, support_phone):
        """
        Set method for to support_phone
        :param support_phone: support_phone
        """
        self.__support_phone = support_phone

    def get_status(self):
        """
        Get method for to status
        :return: status
        """
        return self.__status

    def set_status(self, status):
        """
        Set method for to status
        :param status: status
        """
        self.__status = status

    def get_message(self):
        """
        Get method for to message
        :return: message
        """
        return self.__message

    def set_message(self, message):
        """
        Set method for to message
        :param message: message
        """
        self.__message = message

    def get_percent_fee(self):
        """
        Get method for to percent_fee
        :return: percent_fee
        """
        return self.__percent_fee

    def set_percent_fee(self, percent_fee):
        """
        Set method for to percent_fee
        :param percent_fee: percent_fee
        """
        self.__percent_fee = percent_fee

    def get_fee(self):
        """
        Get method for to fee
        :return: fee
        """
        return self.__fee

    def set_fee(self, fee):
        """
        Set method for to fee
        :param fee: fee
        """
        self.__fee = fee

    def get_deposit_total(self):
        """
        Get method for to deposit_total
        :return: deposit_total
        """
        return self.__deposit_total

    def set_deposit_total(self, deposit_total):
        """
        Set method for to deposit_total
        :param deposit_total: deposit_total
        """
        self.__deposit_total = deposit_total

    def get_rate(self):
        """
        Get method for to rate
        :return: rate
        """
        return self.__rate

    def set_rate(self, rate):
        """
        Set method for to rate
        :param rate: rate
        """
        self.__rate = rate

    def get_btc(self):
        """
        Get method for to btc
        :return: btc
        """
        return self.__btc

    def set_btc(self, btc):
        """
        Set method for to btc
        :param btc: btc
        """
        self.__btc = btc

    def get_request_date(self):
        """
        Get method for to code
        :return: code
        """
        return self.__request_date

    def set_request_date(self, request_date):
        """
        Set method for to request_date
        :param request_date: request_date
        """
        self.__request_date = request_date

    def get_date_executed(self):
        """
        Get method for to date_executed
        :return: date_executed
        """
        return self.__date_executed

    def set_date_executed(self, date_executed):
        """
        Set method for to date_executed
        :param date_executed: date_executed
        """
        self.__date_executed = date_executed

    def to_json(self):
        """
        :return: data in json
        """
        instructions = []
        for instruction in self.get_instructions():
            instructions.append(instruction.to_json())
        data = {
            "token": self.get_token(),
            "amount": self.get_amount(),
            "currency": self.get_currency(),
            "effectiveDate": self.get_effective_date(),
            "ledgerCurrency": self.get_ledger_currency(),
            "reference": self.get_reference(),
            "notificationURL": self.get_notification_u_r_l(),
            "notificationEmail": self.get_notification_email(),
            "email": self.get_email(),
            "recipientId": self.get_recipient_id(),
            "shopperId": self.get_shopper_id(),
            "instructions": instructions,
            "label": self.get_label(),
            "message": self.get_message(),
            "id": self.get_id(),
            "status": self.get_status(),
            "requestDate": self.get_request_date(),
            "exchangeRates": self.get_exchange_rates(),
            "dateExecuted": self.get_date_executed(),
            "rate": self.get_rate(),
            "depositTotal": self.get_deposit_total(),
            "fee": self.get_fee(),
            "percentFee": self.get_percent_fee(),
            "supportPhone": self.get_support_phone(),
            "account": self.get_account(),
            "redirectUrl": self.get_redirect_url(),
            "btc": self.get_btc(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
