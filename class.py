# -*- coding: utf-8 -*-
"""...
"""


class Account(object):
    num_of_accounts = 0

    def __init__(self, name:str, deposit:float):
        self.name = name
        self.balance = deposit
        Account.num_of_accounts += 1

    def __del__(self):
        Account.num_of_accounts -= 1
        pass

    def deposit(self, sum:float):
        self.balance += sum

    def withdraw(self, sum:float):
        self.balance -= sum

    def inquire(self):
        return self.balance


def main():
    a_1 = Account('Alex', 10)
    a_1.deposit(100)
    a_2 = Account('Alexander', 5)
    bal = a_1.inquire()
    del a_1
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')