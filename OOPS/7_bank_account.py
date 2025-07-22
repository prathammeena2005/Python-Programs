class BankAccount:
    def __init__(self, name, account_no, balance):
        self.account_no=account_no
        self.name=name
        self.balance=balance

    def deposite(self, amount):
        self.balance+=amount
        print("Deposited Rs. :", amount, ", New balance =", self.balance)
    
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
            print("Withdrawn Rs. :", amount,"New balance =", self.balance)
        else:
            print("Invalid amount!")
    
    def get_balance(self):
        return self.balance
    
acc1=BankAccount("Rohan Sharma", 142575, 10000)
print("Account holder name =",acc1.name)
print("Account no. =", acc1.account_no)
print("Initial balance =", acc1.balance)
acc1.deposite(12000)
acc1.withdraw(5000)