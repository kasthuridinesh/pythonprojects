# import re
# text = "The rain in Spain"
#
# # To find all the lower case characters in alphabetically between "a" and "m"
#
# x = re.findall ("[a -m]", text)
# print(x)
#
# #\d used to print the digit
# text1 = "that will be 599 dollers"
# x1= re.findall("\d{1}",text1)
# print(x1)
#
# #  " " double qoutes with space and start alphabet and end  will print the string
# text2="hello planet"
# x2=re.findall("h...o",text2)
# print(x2)
#
# txt = "hello planet"
# #Check if the string starts with 'hello':
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")
#
#
import re

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
value= re.findall("falls|stays", txt)
print(value)

if value:
  print("Yes, there is at least one match!")
else:
  print("No match")
