class bank_account:
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0
        self.overdraft_limit=-2000
        self.transactions=[]

    def print(self):
        '''print account details'''
        print(f'name:{self.name}\n'
              f'account number:{self.account_number}\n'
              f'balance:{self.balance}\n'
              f'transactions:{self.transactions}')

    def withdraw(self,amount):
        if self.balance-amount>=self.overdraft_limit:
            self.balance-=amount
            print(f'the amount after withdraw is:{self.balance}')
            self.transactions.append(-amount)
        else:print(f'חרגת מהמסגרת אבאלה')

    def deposit(self,amount):
        self.balance+=amount
        print(f'the amount after deposit is:{self.balance}')
        self.transactions.append(amount)

    def is_overdraft(self):
        if self.balance<0:
            return True
        else:
            return False

my_account=bank_account('idan',12)
my_account.deposit(2000)
my_account.print()
my_account.withdraw(900)
my_account.print()
my_account.deposit(500)
my_account.print()
my_account.withdraw(450)
my_account.print()
my_account.withdraw(5000)
my_account.print()

if my_account.is_overdraft():
    print('your account is overdraft')
else:
    print('your account is not overdraft')

