from Bank import Constant_variable
from Bank.Create_account import AccountDetails
from Bank.Transfer_account import  TransferMoney

# creating bank account
Create_account = AccountDetails(Constant_variable.account_name, Constant_variable.pan_card, Constant_variable.age)
Create_account.create_account()
# Transfering money
Transfer_account = TransferMoney()
Transfer_account.tranfer_money()
