class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Type:", self.acc_type)
        print("Balance:", self.balance)


# Test
acc = BankAccount(101, "Fathima", "Savings", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()
