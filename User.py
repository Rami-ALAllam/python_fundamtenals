class User:
    def __init__(self,name1,email1):
        self.name=name1
        self.email=email1
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("Username:",self.name,",and User email:",self.email,",and he has a balance of:",self.account_balance) 
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
    

Rami = User("Rami","Rami@gmail.com")        
amjad = User("Amjad","Amjad@gmail.com")       
yousef = User("yousef","yousef@gmail.com")       

Rami.make_deposit(100)
Rami.make_deposit(200)
Rami.make_deposit(50)
Rami.make_withdrawal(150)
Rami.display_user_balance()

amjad.make_deposit(200)
amjad.make_deposit(100)
amjad.make_withdrawal(150)
amjad.make_withdrawal(120)
amjad.display_user_balance()

yousef.make_deposit(450)
yousef.make_withdrawal(50)
yousef.make_withdrawal(50)
yousef.make_withdrawal(50)
yousef.display_user_balance()

Rami.transfer_money(amjad,50)
Rami.display_user_balance()
amjad.display_user_balance()