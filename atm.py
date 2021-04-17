class Atm(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin

    def cashWithdrawal(self,cash):
        self.cash=input('enter amount to withdraw')
        print('cash withdrawn sucessfully')

sbi=Atm(123456789,1230)
print(sbi.cardNumber)
print(sbi.pin)

sbi.cashWithdrawal(50000000000)