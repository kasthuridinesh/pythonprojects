from Bank import Constant_variable


class CloseAccount:
    def __init__(self, account_number, password):
        self.account_number = str(account_number)
        self.password = password

    def __close_account(self):
        try:
            int(self.account_number)
            if len(self.account_number) == 12 and self.password == "Advith@25":
                print(f"The account {self.account_number} is closed")
            else:
                print(f"The given account number or password is invalid !!!")
        except ValueError:
            print(f"The account {self.account_number} is not valid")


    def call_private_method(self):
        obj = CloseAccount(Constant_variable.account_number, Constant_variable.password)
        obj.__close_account()


obj = CloseAccount(Constant_variable.account_number, Constant_variable.password)
obj.call_private_method()
