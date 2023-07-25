import random

from Bank import Constant_variable

class AccountDetails:

    def __init__(self, account_name, pan_card, age):
        self.account_name = account_name
        self.pan_card = pan_card
        self.age = age

    def create_account(self):
        if self.account_name != "" and len(self.pan_card) == 10 and self.age > 18 and \
                (all(char.isalpha() or char.isspace() for char in self.account_name)):
            account_number = random.randint(100000000000, 999999999999)
            Constant_variable.account_number = account_number
            print(f"The account is created for {self.account_name} and account number is {account_number}")

        elif self.age < 18:
            print("The account cannot be created because age is less than 18")

        elif self.account_name == "":
            print("The account name is null")

        elif len(self.pan_card) != 10:
            print("The PAN Card is invalid")
        else:
            print("The account name is invalid")

#obj= AccountDetails(Constant_variable.account_name, Constant_variable.pan_card, Constant_variable.age,)
#obj.create_account()
