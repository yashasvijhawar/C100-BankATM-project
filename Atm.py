class Atm(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def CashWithdrawal(self):
        print("A cash withdrawal requires converting the holdings of an account, plan, pension, or trust into cash, usually through a sal")

    def BalanceEnquiry(self):
        print("The Balance Inquiry process is associated with customer accounts and is used to check the amount remaining on a customer's store credit voucher, gift card, or gift certificate.")


card = Atm(3547826484,756)
card.CashWithdrawal()
card.BalanceEnquiry()