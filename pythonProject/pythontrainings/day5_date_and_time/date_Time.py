from datetime import datetime


# def convert():
#     date_string = "18 january 2023"
#     print("date_string =", date_string)
#     date_object = datetime.strptime(date_string, "%d %B, %Y")
#     print("date_object =", date_object)
#
# convert()


def converting():
    date_string = "18 january, 2023"
    print("date_string =", date_string)
    print("type of date_string =", type(date_string))
    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)
    print("type of date_object =", type(date_object))
converting()