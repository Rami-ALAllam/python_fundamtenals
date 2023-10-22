class User:
    def __init__(self,name1,email1):
        self.name=name1
        self.email=email1
        self.account= BankAccount(int_rate=0.03, balance=0, name= "checking_account")
        self.account2= BankAccount(int_rate=0.1, balance=100, name= "saving_account")


    def make_deposit(self,amount,x):
        if x == 1:
            self.account.deposit(amount)
        else:
            self.account2.deposit(amount)
			
    def make_withdrawal(self, amount,x):
        if x == 1:
            self.account.withdraw(amount)
        else:
            self.account2.withdraw(amount)
		
    def display_user_balance(self,x):
        if x == 1:
            print("Username:",self.name,",and User email:",self.email,",and his",self.account.name,"has a balance of:",self.account.balance)
        else:
            print("Username:",self.name,",and User email:",self.email,",and his",self.account2.name,"has a balance of:",self.account2.balance)
		
    def transfer_money(self, other_user, amount, x):
        if x==1:
            self.account.transfer_money(other_user,amount)
        else:
            self.account2.transfer_money(other_user,amount)
    def yield_interest(self,x):
        if x==1:
            self.account.yield_interest()
        else:
            self.account2.yield_interest()


class BankAccount:
		def __init__(self, int_rate, balance, name):
			self.int_rate = int_rate
			self.balance = balance
			self.name = name

		def deposit(self,amount):
			self.balance += amount
			return self
		
		def withdraw(self, amount):
			if self.balance >= amount:
				self.balance -= amount
			else:
				self.balance -= 5
				print("Insufficient funds: Charging a $5 fee")
			return self
		
		def yield_interest(self):
			if self.balance > 0:
				self.balance = (self.balance * self.int_rate)+self.balance
			return self
		
		def display_account_info(self):
			print("balance:",self.balance,"int_rate:",self.int_rate)
			return self
		
		def transfer_money(self, other_user, amount):
			self.balance -= amount
			other_user.account.balance += amount

		
Rami = User("Rami","Rami@gmail.com")
amjad = User("amjad","amjad@gmail.com")

Rami.make_deposit(100,2)
Rami.make_deposit(50,1)
Rami.make_withdrawal(20,1)
Rami.make_withdrawal(30,2)
Rami.transfer_money(amjad,40,1)
Rami.yield_interest(1)
Rami.display_user_balance(2)
Rami.display_user_balance(1)
amjad.yield_interest(2)
amjad.display_user_balance(2)

