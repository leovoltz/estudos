import accounts
import person


class Bank:
    def __init__(
        self,
        agencys: list[int] | None = None,
        clients: list[person.Client] | None = None,
        accounts: list[accounts.Account] | None = None,
    ):
        self.agencys = agencys or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_agency(self, account):
        if account.agency in self.agencys:
            return True
        return False

    def _check_client(self, client):
        if client in self.clients:
            return True
        return False

    def _check_account(self, account):
        if account in self.accounts:
            return True
        return False

    def _check_if_is_clients_account(self, client, account):
        if account is client.account:
            return True
        return False

    def auth(self, client: person.Client, account: accounts.Account):
        return self._check_agency(account) and \
            self._check_client(client) and \
            self._check_account(account) and \
            self._check_if_is_clients_account(client, account)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencys!r}, {self.clients!r}, {self.accounts})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = person.Client('Leonardo', 20)
    ca1 = accounts.CheckingAccount(111, 222, 0, 0)
    c1.account = ca1
    c2 = person.Client('Yasmin', 19)
    sa1 = accounts.SavingsAccount(112, 223, 100)
    c2.account = sa1
    bank = Bank()
    bank.clients.extend([c1, c2])
    bank.accounts.extend([ca1, sa1])
    bank.agencys.extend([111, 112])

    if bank.auth(c1, ca1):
        ca1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)
