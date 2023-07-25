import os


# #Registraion for new user
# def register_user(username, password, mobile_number):
#     # Check if the user already exists in registered_users.txt
#     try:
#         if os.path.isfile("registered_users.txt"):
#             with open("registered_users.txt", "r") as register_file:
#                 registered_users = register_file.read()
#                 if f"{username},{password}\n" in registered_users:
#                     raise Exception("Error: User already exists.")
#
#                 else:
#          # Append the new user to registered_users.txt
#                     with open("registered_users.txt", "a") as new_user_file:
#                       new_user_file.write(f"{username},{password}\n")
#
#             # Create a new file for the user with their mobile number
#                     with open(f"{username}.txt", "w") as mobile_number_file:
#                      if len(str(mobile_number) > 10 < 5):
#                          raise Exception("Enter correct 10 digit mobile number")
#                      else:
#                       mobile_number = mobile_number_file.read()
#                       mobile_number_file.write(mobile_number)
#         else:
#             print("The given user_name or password is wrong")
#     except FileNotFoundError:
#         print("The file registered_user not exist")
#



# # printing mobile number while giving user_name and password
#
def show_mobile_number(username, password, mobile_number=None):
    try:
    # Check if the user exists in registered_users.txt
     if os.path.isfile("registered_users.txt"):
        with open("registered_users.txt", "r") as register_user_file:
            registered_users = register_user_file.read()
            if f"{username},{password}\n" not in registered_users:
                raise Exception("Error: Invalid username or password.")

    # Read the mobile number from the user's file
     with open(f"{username}.txt", "r") as mobile_number_file:
         if len((mobile_number)>10<5):
             raise Exception("Enter correct 10 digit mobile number")
         else:
           mobile_number = mobile_number_file.read()
           print(mobile_number)
    except FileNotFoundError:
        print("File not found")
show_mobile_number("kasthuri","kasthuri@26\5")
#

# updating mobile number
def update_mobile_number(username, password, new_mobile_number):
    # Check if the user exists in registered_users.txt
    if os.path.isfile("registered_users.txt"):
        with open("registered_users.txt", "r") as file:
            registered_users = file.read()
            if f"{username},{password}\n" not in registered_users:
                raise Exception("Error: Invalid username or password.")

    # Update the mobile number in the user's file
    with open(f"{username}.txt", "w") as file:
        file.write(new_mobile_number)
