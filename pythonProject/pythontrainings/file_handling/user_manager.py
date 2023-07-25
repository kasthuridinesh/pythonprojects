def register_user(username, password, mobile_number):
    with open("registered_users.txt", "r") as read_registered_file:
        try:
            read_user = read_registered_file.read()
            if f"{username},{password}\n" in read_user:
                print("User already exists")
            elif len(username) == 0:
                print("please enter a valid username")
            elif len(username) <= 3 and password <= 6:
                print("Please enter valid username and password")
            elif len(mobile_number) != 10 and mobile_number.isdigit():
                print("Please provide valid mobile number")

            else:
                with open('registered_users.txt', 'a') as register_user_and_password:
                    register_user_and_password.write(f"{username},{password}\n")
                    print(f"User {username} has been registered with password {password}.")
                    print("Username and password are registered successfully!!")
                    with open(f"{username}.txt", "w") as register_mobile_number:
                        register_mobile_number.write(mobile_number)

        except FileNotFoundError:
            print("File is not present")


# register_user("sfghhn ", "kasthuri@26", "7293022280")


def show_mobile_number(username, password):
    try:
        with open("registered_users.txt", "r") as read_file:
            check_user = read_file.read()
            if f"{username},{password}\n" not in check_user:
                print("Username doesn't exists")
            elif password not in check_user:
                print("password doesn't exist")
            elif len(username) == 0:
                print("Enter the valid username")
            elif len(password) >= 5:
                print("Password must be more than 8 characters")
            elif len(username) <= 3:
                print("enter the valid user name")

            else:
                with open(f"{username}.txt", "r") as mobile_number:
                    display_mobile_number = mobile_number.read()
                    print(f"The mobile number of the given username '{display_mobile_number}'")
    except FileNotFoundError:
        print("File doesn't exist")


# show_mobile_number("Netra","Netra@123")


def update_mobile_number(username, password, new_mobile_number):
    try:
        with open("registered_users.txt", "r") as read_file:
            registered_file = read_file.read()
            if f"{username},{password}\n" not in registered_file:
                print("Username  doesn't exist in the file")
            elif len(new_mobile_number) != 10 and new_mobile_number.isdigit():
                print("Enter proper mobile_number")
            else:
                with open(f"{username}.txt", "w") as write_file:
                    updated_mobile_number = write_file.write(new_mobile_number)
                with open(f"{username}.txt", "r") as read_file:
                    new_mobile_number = read_file.read(updated_mobile_number)
                    print("The mobile_number of the given user", new_mobile_number)

    except FileNotFoundError:
        print("OOPS,File doesn't exist")

# update_mobile_number("Netra","Netra@123", "9876564597")
