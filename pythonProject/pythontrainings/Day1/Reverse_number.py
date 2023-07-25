# Write a code that takes a number between 11 to 99, reverse the number,
# and print the reversed number. for example,
# if the input number is 54, the code will reverse the number to 45 and print it.
##################      Start of the program ########################################################
# Reversing of a number
number = input("Enter the number:")

num = int(number)
if 11 < num < 100:
    rev = 0
    while num > 0:
        reminder = num % 10
        rev = rev * 10 + reminder
        num = num // 10
    print(rev)
else:
    print("enter the valid number")

############################# End of the Program #############################################
