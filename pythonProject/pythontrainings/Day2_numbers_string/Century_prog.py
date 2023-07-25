'''
Exercise 1: Write a code that takes in a year and returns the correct century.
 1756 ➞ "18th century"
1555 ➞ "16th century"
1000 ➞ "10th century"
1001 ➞ "11th century"
2005 ➞ "21st century"
Notes:
 All years will be between 1000 and 2010.
The 11th century is between 1001 and 1100.
The 18th century is between 1701-1800.

'''
#### ******************* Start of the program *******************
enter_the_year=int(input("Enter the year:"))
century = (enter_the_year//100)+1
print("year belongs to century of :",century)
##########*********** End of the program **************************