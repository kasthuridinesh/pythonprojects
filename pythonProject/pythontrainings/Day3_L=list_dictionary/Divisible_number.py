'''
Write a code that takes three parameters where:
 x is the start of the range (inclusive).
y is the end of the range (inclusive).
n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n. Return an empty list if there are no numbers that are divisible by n.
 Examples:
1, 10, 3 ➞ [3, 6, 9]
7, 9, 2 ➞ [8]
15, 20, 7 ➞ []
'''


# ******************** Start of the program *******
def divisible_numbers(start, end, divisor):
    result = []
    try:
        for number in range(start, end + 1):
            if number % divisor == 0:
                result.append(number)
    except:
        raise Exception("divisor must be an integer")
    return result


print(divisible_numbers(-6, 10, 2))
print(divisible_numbers(7, 9, 2))
print(divisible_numbers(15, 20, 7))
# ***** end of the program ****
