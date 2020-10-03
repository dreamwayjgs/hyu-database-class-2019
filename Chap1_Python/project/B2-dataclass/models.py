from dataclasses import dataclass, field


@dataclass
class Bank:
    _bid: str
    _code: str
    name: str

    @property
    def bid(self):
        return int(self._bid)

    @property
    def code(self):
        return int(self._code)


@dataclass
class Customer:
    name: str
    phone: str
    local: str
    domain: str
    passwd: str = field(repr=False)
    _bankid: str
    accountnum: str
    _balance: str

    @property
    def bankid(self):
        return int(self._bankid)

    @property
    def balance(self):
        return int(self._balance)

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def email(self):
        return f"{self.local}@{self.domain}"

    def __repr__(self):
        return f"name: {self.name}, phone: {self.phone}, email: {self.email}, balance: {self.balance}"
