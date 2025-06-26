##Class Inheritance

class BankAccount:
    """ A System to manage bank accounts. \n
    This System can create accounts, deposit, withdraw and check balance. \n
    Make sure you enter the account number correctly.
    """
    
    
    MAIN_BALANCE = 0
    INTEREST_RATE = 0.065
    YEARS = 0  
    def __init__(self, account_number, balance=0):
        if account_number < 10000 or account_number > 99999:
            raise ValueError("Account Number must be a 5 digit number. ")
        else:
            with open('BankAccount_Numbers.txt', "r") as file:
                x = file.read()
                account_numbers = [int(num.strip()) for num in x.split(",") if num.strip()]
                if account_number not in account_numbers:
                    raise ValueError("Account number does not exist.")
                self.account_number = account_number
                self.balance = balance
                BankAccount.YEARS = int(input("How many years you want to calculate interest for? \n >>> "))
                
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        BankAccount.MAIN_BALANCE += amount
        return f"Deposited {amount} TAKA.\n New balance: {self.balance:.2f} TAKA"
                     
class SavingsAccount(BankAccount):
    
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        
    def calculate_interest(self):
        BankAccount.MAIN_BALANCE = self.balance * BankAccount.INTEREST_RATE * BankAccount.YEARS
        return f"Interest earned in {BankAccount.YEARS} years: {BankAccount.MAIN_BALANCE:.2f} TAKA"
    def withdraw(self, amount):
        if amount < 500:
            raise ValueError("Minimum withdrawal amount is 500 TAKA.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        BankAccount.MAIN_BALANCE -= amount
        return f"Withdrawn {amount} TAKA.\n New balance: {self.balance:.2f} TAKA"
        
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        
raya = SavingsAccount(24772, 1000)
print(raya.deposit(500))












