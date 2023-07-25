'''
 Exercise 3: Consider the following string variables in your code:
chocolatePrice = '₹35'
lemonPrice = '₹20'
And, write a code to print the sum of the above two variables.
'''
# ***************** Start of the program ***********
chocolatePrice = "₹35"
lemonPrice = "₹20"
price1 = int(chocolatePrice[1:])
price2 = int(lemonPrice[1:])
sum = price1 + price2
print("Printing sum of two string: ₹",sum)

# ***************** End of the program **************
