# Create a program that takes a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
#################   Start of the Program    #########################################
'''
# print all the divisor of a particular number
number = int(input("Enter the number which is divisor:"))

for index in range(1, number + 1):
    if number % index == 0:
        print(index)

######################### End of the program #########################################


'''
choice = 1
while choice == 1:
    i = 1
    num = int(input("Enter Test Number: "))
    while i < (num / 2 + 1):
        if num % i == 0:
            print(i)
        i = i + 1
    print(num)
'''
