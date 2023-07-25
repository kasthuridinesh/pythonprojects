from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def getBalance(self):
        pass


class BankA(Bank):
    def getBalance(self):
        return 100


class BankB(Bank):
    def getBalance(self):
        return 150


class BankC(Bank):
    def getBalance(self):
        return 200



