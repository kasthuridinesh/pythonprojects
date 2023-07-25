# A number sequence is as follows:
# 5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, …
# Given that 5 is at position 1, Write a code that returns the number found at position N in the sequence.
# Examples:
# N = 4 ➞ 200
# N = 5 ➞ 7
# N = 28 ➞ 819200
# Notes: You can expect to be only given valid inputs.

####################################################################################################################
#                                         Start of the program                                                     #
###################################################################################################################
"""
Author name : Kasthuri kandavelu
"""

position = int(input("Enter the position:"))
# checking that the number position is even or not and stored in the list
if position % 2 == 0:
    num = int(100 * (2 ** (position / 2 - 1)))
    print(num)
else:
    print(position // 2 + 5)
#####################################################################################################################
#                                End of the program                                                                 #
#####################################################################################################################
