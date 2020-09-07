# a class that save pin number and accounts of a customer

class Customer:

	def __init__(self, pin_number):

		self.pin = pin_number

		self.accounts = {}

		self.n_accounts = 0

	def validateCustomer(self):

		pin_number = int(input("Please enter your PIN number: "))

		return True if (pin_number == self.pin) else False

	def addAccount(self, account):

		self.n_accounts += 1

		self.accounts[self.n_accounts] = account



# a class that save an account info of a customer and can operate withdraw/balance/deposit action on the account

class Account:

	def __init__(self):

		self.balance = 0

	def deposit(self):

		value = float(input("Enter the value you want to deposit to your account: "))

		self.balance += value

		print("\nDeposite is Completed.")



	def withdraw(self):

		value = float(input("Enter the value you want to withdraw from your account: "))

		if self.balance >= value:

			self.balance -= value

			print("\nWithdraw is completed.")

		else:

			print("\nYou donot have enough balance in your account.")

	def display(self):

		print("\nAvailable balance in your account is ", self.balance)



pin_number = int(input("Please enter a number to create your pin?"))

# create a customer object

customer = Customer(pin_number)



# check the validity of the customer

card_inserted = input("Have you inserted your card? True or False?")

if card_inserted == "True":

	if (customer.validateCustomer()):

		account_number = int(input("Please type your account number? "))

		if customer.n_accounts == 0:

			customer.addAccount(Account())

		while customer.n_accounts < account_number:

			account_number = int(input("Wrong account number.\nPlease type your account number? "))

		account = customer.accounts[account_number]

		

		select_action = 1

		while (select_action > 0):

			select_action = int(input("\nPlease select your operation from these options\n 0:Terminate 1: Balance 2: Withdraw 3: Deposit ?"))

			if select_action == 1:

				account.display()

			elif select_action == 2:

				account.withdraw()

			elif select_action == 3:

				account.deposit()



	

