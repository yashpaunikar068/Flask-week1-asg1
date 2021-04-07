class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amt):
        if(amt > self.balance):
            print('Insufficient Funds to complete the transaction')
        else:
            self.balance = self.balance - amt
            print('Successfully withdrawn ' + str(amt))    
            print('your balance is ' + str(self.balance))

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Successfully deposited ' + str(amt))
        print('your balance is ' + str(self.balance))

    def __str__(self):
        return ('This account is owned by ' + self.name + ' and has balance ' + str(self.balance))

    def get_balance(self):
        return self.balance

print()

account = BankAccount('Yash', 1000)
print(account)
account.withdraw(500)
account.deposit(500)
account.withdraw(5000)

print()

account1 = BankAccount('Flask', 10000)
print(account1)
account1.withdraw(5000)
account1.deposit(5000)
account1.withdraw(50000)

  