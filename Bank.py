class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amt):
        if(amt > self.balance):
            print('Insufficient Funds')
        else:
            self.balance = self.balance - amt
            print('Successfully withdrawn ' + str(amt))    
            print('your balance is ' + str(self.balance))

    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Successfully deposited ' + str(amt))

    def __str__(self):
        return (self.name + ' ' + str(self.balance))

    def get_balance(self):
        return self.balance

account = BankAccount('Yash', 1000)
account.withdraw(500)
account.deposit(500)
print(account)
account.withdraw(5000)

  