from dataclasses import dataclass
from typing import Optional


class InsufficientBalanceError(Exception):
    pass


class AccountHolderNotFound(Exception):
    pass


@dataclass
class BankAccount:
    owner: str
    balance: int

    def deposit(self, amount: int) -> None:
        """
        It adds the amount to your balance
        """

        if amount < 500:
            raise ValueError("Minimum 500 required for deposit")

        if amount < 0:
            raise ValueError("Amount should be in positive")

        self.balance += amount
        print("Deposit Successful")

    def withdraw(self, amount: int) -> None:
        """
        It withdraw amount from your back account
        """

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Your balance is lesser than required amount"
            )

        if amount <= 0:
            raise ValueError("Amount should be in positive")

        self.balance -= amount
        print(f"Withdraw Sucessfull : Your balance is {self.balance}")

    def transfer(self, other_account: str, amount: int) -> None:
        """
        It Transfers money from one account to another
        """

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Your balance is lesser than required amount"
            )
        if amount < 0:
            raise InsufficientBalanceError("Balance must be in positive")
        if not other_account:
            raise AccountHolderNotFound("Mentioned account is not found")

        self.balance -= amount
        other_account.balance += amount
        print(f"Tranfer completed to the Account : {other_account.owner}")


class Service:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    def create_account(self, name: str, balance: int):
        """
        It creates a new Account by the name and amount
        """

        if any(account.owner == name for account in self.accounts):
            raise ValueError(f"Account already exists in the name : {name}")

        if balance < 0:
            raise ValueError("Balance should be in positive")

        account = BankAccount(name, balance)
        self.accounts.append(account)

    def find_account(self, name):
        """
        It finds the Account that already exists in database
        """

        for account in self.accounts:
            if account.owner == name:
                return account
        raise AccountHolderNotFound("Account not found")


service = Service()

service.create_account("Kishore", 5000)
service.create_account("Luffy", 2000)

acc1 = service.find_account("Kishore")
acc2 = service.find_account("Luffy")

acc1.transfer(acc2, 1000)

print(acc1.balance)

acc1.deposit(1000)

print(acc1.balance)
print(acc2.balance)
