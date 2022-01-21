from .payout_info import PayoutInfo
from .with_holdings import WithHoldings
from .settlement_ledger_entry import SettlementLedgerEntry


class Settlement:
    __id = None
    __account_id = None
    __currency = None
    __payout_info = None
    __status = None
    __date_created = None
    __date_executed = None
    __date_completed = None
    __opening_date = None
    __closing_date = None
    __opening_balance = None
    __ledger_entries_sum = None
    __with_holdings = None
    __with_holdings_sum = None
    __total_amount = None
    __ledger_entries = None
    __token = None

    def __init__(self):
        pass

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

    def get_account_id(self):
        """
        Get method for to account_id
        :return: account_id
        """
        return self.__account_id

    def set_account_id(self, account_id):
        """
        Set method for to account_id
        :param account_id: account_id
        """
        self.__account_id = account_id

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

    def get_payout_info(self):
        """
        Get method for to payout_info
        :return: payout_info
        """
        return self.__payout_info

    def set_payout_info(self, payout_info: PayoutInfo):
        """
        Set method for to payout_info
        :param payout_info: payout_info
        """
        self.__payout_info = payout_info

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

    def get_date_created(self):
        """
        Get method for to date_created
        :return: date_created
        """
        return self.__date_created

    def set_date_created(self, date_created):
        """
        Set method for to date_created
        :param date_created: date_created
        """
        self.__date_created = date_created

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

    def get_date_completed(self):
        """
        Get method for to date_completed
        :return: date_completed
        """
        return self.__date_completed

    def set_date_completed(self, date_completed):
        """
        Set method for to date_completed
        :param date_completed: date_completed
        """
        self.__date_completed = date_completed

    def get_opening_date(self):
        """
        Get method for to opening_date
        :return: opening_date
        """
        return self.__opening_date

    def set_opening_date(self, opening_date):
        """
        Set method for to opening_date
        :param opening_date: opening_date
        """
        self.__opening_date = opening_date

    def get_closing_date(self):
        """
        Get method for to closing_date
        :return: closing_date
        """
        return self.__closing_date

    def set_closing_date(self, closing_date):
        """
        Set method for to closing_date
        :param closing_date: closing_date
        """
        self.__closing_date = closing_date

    def get_opening_balance(self):
        """
        Get method for to opening_balance
        :return: opening_balance
        """
        return self.__opening_balance

    def set_opening_balance(self, opening_balance):
        """
        Set method for to opening_balance
        :param opening_balance: opening_balance
        """
        self.__opening_balance = opening_balance

    def get_ledger_entries_sum(self):
        """
        Get method for to ledger_entries_sum
        :return: ledger_entries_sum
        """
        return self.__ledger_entries_sum

    def set_ledger_entries_sum(self, ledger_entries_sum):
        """
        Set method for to ledger_entries_sum
        :param ledger_entries_sum: ledger_entries_sum
        """
        self.__ledger_entries_sum = ledger_entries_sum

    def get_with_holdings(self):
        """
        Get method for to with_holdings
        :return: with_holdings
        """
        return self.__with_holdings

    def set_with_holdings(self, with_holdings: WithHoldings):
        """
        Set method for to with_holdings
        :param with_holdings: with_holdings
        """
        self.__with_holdings = with_holdings

    def get_with_holdings_sum(self):
        """
        Get method for to with_holdings_sum
        :return: with_holdings_sum
        """
        return self.__with_holdings_sum

    def set_with_holdings_sum(self, with_holdings_sum):
        """
        Set method for to with_holdings_sum
        :param with_holdings_sum: with_holdings_sum
        """
        self.__with_holdings_sum = with_holdings_sum

    def get_total_amount(self):
        """
        Get method for to total_amount
        :return: total_amount
        """
        return self.__total_amount

    def set_total_amount(self, total_amount):
        """
        Set method for to total_amount
        :param total_amount: total_amount
        """
        self.__total_amount = total_amount

    def get_ledger_entries(self):
        """
        Get method for to ledger_entries
        :return: ledger_entries
        """
        return self.__ledger_entries

    def set_ledger_entries(self, ledger_entries: SettlementLedgerEntry):
        """
        Set method for to ledger_entries
        :param ledger_entries: ledger_entries
        """
        self.__ledger_entries = ledger_entries

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

    def to_json(self):
        """
        :return: data in json
        """
        data = {
            "id": self.get_label(),
            "accountId": self.get_bank_country(),
            "currency": self.get_name(),
            "payoutInfo": self.get_bank(),
            "status": self.get_swift(),
            "dateCreated": self.get_address(),
            "dateExecuted": self.get_city(),
            "dateCompleted": self.get_postal(),
            "openingDate": self.get_sort(),
            "closingDate": self.get_wire(),
            "openingBalance": self.get_bank_name(),
            "ledgerEntriesSum": self.get_bank_address(),
            "withHoldings": self.get_iban(),
            "withHoldingsSum": self.get_additional_information(),
            "totalAmount": self.get_account_holder_name(),
            "ledgerEntries": self.get_account_holder_address(),
            "token": self.get_account_holder_address2()
        }
        return data
