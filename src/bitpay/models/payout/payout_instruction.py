"""
PayoutInstruction
"""
from ...exceptions.bitpay_exception import BitPayException
from .recipient_reference_method import RecipientReferenceMethod
from .payout_instruction_btc_summary import PayoutInstructionBtcSummary
from .payout_instruction_transaction import PayoutInstructionTransaction
from ...exceptions.payout_creation_exception import PayoutCreationException
from ...utils.key_utils import change_camel_case_to_snake_case


class PayoutInstruction:
    """
    PayoutInstruction
    """

    __amount = None
    __email = None
    __recipient_id = None
    __shopper_id = None
    __label = ""
    __wallet_provider = None
    __id = None

    __btc = PayoutInstructionBtcSummary()
    __transactions = []
    __status = None
    __address = None
    __payout_id = None

    __method = None
    __method_value = None

    def __init__(self, amount, method, method_value, **kwargs):
        self.set_amount(amount)

        for key, value in kwargs.items():
            try:
                if key in ["btc", "transactions"]:
                    klass = (
                        PayoutInstructionTransaction
                        if key == "transactions"
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

        try:
            if method:
                if RecipientReferenceMethod.EMAIL == method:
                    self.__email = method_value
                elif RecipientReferenceMethod.RECIPIENT_ID == method:
                    self.__recipient_id = method_value
                elif RecipientReferenceMethod.SHOPPER_ID == method:
                    self.__shopper_id = method_value
            else:
                raise PayoutCreationException(
                    "method code must be a type " "of RecipientReferenceMethod"
                )
        except Exception as exe:
            raise BitPayException(exe)

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
        if amount < 5:
            raise BitPayException("Instruction amount should be 5 or higher.")
        self.__amount = amount

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

    def get_payout_id(self):
        """
        Get method for to payout_id
        :return: payout_id
        """
        return self.__email

    def set_payout_id(self, payout_id):
        """
        Set method for to payout_id
        :param payout_id: payout_id
        """
        self.__payout_id = payout_id

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

    def get_wallet_provider(self):
        """
        Get method for to wallet_provider
        :return: wallet_provider
        """
        return self.__wallet_provider

    def set_wallet_provider(self, wallet_provider):
        """
        Set method for to wallet_provider
        :param wallet_provider: wallet_provider
        """
        self.__wallet_provider = wallet_provider

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

    def get_address(self):
        """
        Get method for to address
        :return: address
        """
        return self.__address

    def set_address(self, address):
        """
        Set method for to address
        :param address: address
        """
        self.__address = address

    def get_btc(self):
        """
        Get method for to btc
        :return: btc
        """
        return self.__btc

    def set_btc(self, btc: PayoutInstructionBtcSummary):
        """
        Set method for to btc
        :param btc: btc
        """
        self.__btc = btc

    def get_transactions(self):
        """
        Get method for to transactions
        :return: transactions
        """
        return self.__transactions

    def set_transactions(self, transactions: [PayoutInstructionTransaction]):
        """
        Set method for to transactions
        :param transactions: transactions
        """
        self.__transactions = transactions

    def to_json(self):
        """
        :return: data in json
        """
        transactions = []
        for data in self.get_transactions():
            transactions.append(data.to_json())
        data = {
            "amount": self.get_amount(),
            "email": self.get_email(),
            "recipientId": self.get_recipient_id(),
            "shopperId": self.get_shopper_id(),
            "label": self.get_label(),
            "id": self.get_id(),
            "btc": self.get_btc().to_json(),
            "transactions": transactions,
            "status": self.get_status(),
            "payoutId": self.get_payout_id(),
        }
        data = {key: value for key, value in data.items() if value}
        return data
