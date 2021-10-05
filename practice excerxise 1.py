class BankAccount:

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, money):
        self.money = money
        balance = self.balance - self.money
        print(balance)

    def deposit(self, money):
        balance = self.balance + money
        print(balance)

customer = BankAccount()

customer.set_details('Prakarti', 10000)
customer.display()
customer.withdraw(8000)
customer.deposit(50000)

