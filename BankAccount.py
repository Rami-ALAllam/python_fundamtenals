class BankAccount:
		def __init__(self, int_rate=0.03, balance=0):
			self.int_rate = int_rate
			self.balance = balance
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
		

amjad= BankAccount()
Rami= BankAccount(0.05,500)

amjad.deposit(50).deposit(50).deposit(50).withdraw(20).yield_interest().display_account_info()

Rami.deposit(120).deposit(120).withdraw(40).withdraw(40).withdraw(40).withdraw(40).yield_interest().display_account_info()
