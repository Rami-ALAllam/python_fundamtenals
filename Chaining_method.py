class User:
    def __init__(self,name1,email1):
        self.name=name1
        self.email=email1
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("Username:",self.name,",and User email:",self.email,",and he has a balance of:",self.account_balance) 
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    

Rami = User("Rami","Rami@gmail.com")        
amjad = User("Amjad","Amjad@gmail.com")       
yousef = User("yousef","yousef@gmail.com")       

Rami.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(150).display_user_balance()

amjad.make_deposit(200).make_deposit(200).make_withdrawal(150).make_withdrawal(150).display_user_balance()

yousef.make_deposit(450).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

Rami.transfer_money(amjad,50)
Rami.display_user_balance()
amjad.display_user_balance()