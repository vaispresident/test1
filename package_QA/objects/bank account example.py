class bank_account:
    def __init__(self,name,acc_number,balance):
        self.name=name
        self.acc_number=acc_number
        self.balance=balance

    def statememt(self):
        '''print account details'''
        print(f'name:{self.name} '
              f'account number:{self.acc_number} '
              f'balance:{self.balance}')

    def withdraw(self,amount):
        self.balance-=amount


my_account=bank_account('idan',2000,500)
# my_account.name='idan'
# my_account.acc_number=2000
# my_account.balance=1000000
my_account.withdraw(1)
my_account.statememt()



# your_account=bank_account()
# your_account.name=ben
# your_account.acc_number=100
# your_account.balance=5
# your_account.statememt()

