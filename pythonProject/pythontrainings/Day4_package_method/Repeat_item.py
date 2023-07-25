'''
Create a function that takes two arguments (item, times). The first argument (item) is the item that needs repeating while the second argument (times) is the number of times the item is to be repeated. Return the result in a list.

Examples:
repeat("edabit", 3) ➞ ["edabit", "edabit", "edabit"]
repeat(13, 5) ➞ [13, 13, 13, 13, 13]
repeat("7", 2) ➞ ["7", "7"]
repeat(0, 0) ➞ []

Notes:
item can be either a string or a number.
times will always be a number.
'''

####***********  Start of the program *************#
def repeat():
    try:
        item = input("Enter an item: ")
        times = int(input("Enter the number of times to repeat the item: "))
        if times < 0:
            raise ValueError("Times must be a non-negative number")
        return [item] * times
    except ValueError as ve:
        print(ve)
    except:
        print("Invalid input. Please enter a valid item and number of times.")


print(repeat())

#************** End of the program *************#
