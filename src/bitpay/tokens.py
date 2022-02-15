"""
New tokens are provided with each response from the API. For example,
creating a new Invoice with one token will provide a new, second token
that grants access to view and interact with that Invoice exclusively. If not using
BitPay's Client Libraries, you will need to keep track of these tokens on your own.
"""
from .models.facade import Facade


class Tokens:
    """
    Tokens
    """

    __merchant = ""
    __payout = ""

    def __init__(self, merchant=None, payout=None):
        """
        :param merchant:The broadest set of capabilities against a merchant organization.
        Allows for create, search,and view actions for Invoices and Bills; ledger download,
        as well as the creation of new merchant or pos tokens associated with the account.
        :param payout:The BitPay Payout service enables businesses to payout fleets of users
        globally in one common format using digital currency, to any internet-connected user,
        regardless of country or banking status.
        The payout recipient could be an individual, or a company or a vendor that offered their
        services or payout employees. This resource allows merchants to submit individual
        cryptocurrency payout requests to active bitpay recipients. The typical use case for this
        resource would be a company who wants to offer cryptocurrency withdrawals to their
        customers,
        like marketplaces or affiliate networks.
        """
        self.__merchant = merchant
        self.__payout = payout

    def get_token_by_facade(self, facade):
        """
        :param facade: Facades named collections of capabilities that can be granted,
         such as the ability to create invoices or grant refunds.
        """

        token = None

        if Facade.Merchant == facade:
            token = self.__merchant
        elif Facade.Payout == facade:
            token = self.__payout

        if token:
            return token

        raise Exception(
            "given facade does not exist or no token defined for the given facade"
        )

    def get_merchant_token(self):
        """
        Get method for the merchant
        :return: merchant
        """
        return self.__merchant

    def set_merchant_token(self, merchant):
        """
        Set method for the merchant
        :param merchant: merchant
        """
        self.__merchant = merchant

    def get_payout_token(self):
        """
        Get method for the payout
        :return: payout
        """
        return self.__payout

    def set_payout_token(self, payout):
        """
        Set method for the payout
        :param payout: payout
        """
        self.__payout = payout
