from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account: int, balance: float = 0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    @abstractmethod
    def withdraw(self, value: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'(Deposit {value})')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'Your current balance is: {self.balance:.2f} -- {msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance})'
        return f'{class_name}{attrs}'


class SavingsAccount(Account):
    def withdraw(self, value: float) -> float:
        balance_after_withdraw = self.balance - value

        if balance_after_withdraw >= 0:
            self.balance -= value
            self.details(f'(Cash Withdrawal: {value})')
            return self.balance
        print('Unable to withdraw money!')
        self.details('\n~Withdrawal denied!~')
        return self.balance


class CheckingAccount(Account):
    def __init__(self, agency: int, account: int,
                 balance: float = 0, limit: int = 0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, value: float) -> float:
        balance_after_withdraw = self.balance - value
        max_limit = -self.limit

        if balance_after_withdraw >= max_limit:
            self.balance -= value
            self.details(f'(Cash Withdrawal: {value})')
            return self.balance
        print('Unable to withdraw money!')
        print(f'Your account limit is: {-self.limit:.2f}')
        self.details('Withdrawal denied!')
        return self.balance

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account!r}, {self.balance}, '\
            f'{self.limit})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    saving_a1 = SavingsAccount(1123, 222)
    saving_a1.withdraw(1)
    saving_a1.deposit(1)
    saving_a1.withdraw(1)
    print('~' * 20)
    checking_a1 = CheckingAccount(1123, 222, 0, 100)
    checking_a1.withdraw(1)
    checking_a1.deposit(1)
    checking_a1.withdraw(1)
    checking_a1.withdraw(98)
    checking_a1.withdraw(1)
    checking_a1.withdraw(2)
