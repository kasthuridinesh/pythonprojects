'''
 Write a code that takes a list of dictionaries and returns the sum of people's budgets.

Examples:
 [
{ "name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve",  "age": 32, "budget": 40000 },
{ "name": "Martin",  "age": 16, "budget": 2700 }
] ➞ 65700

[
{ "name": "John",  "age": 21, "budget": 29000 },
{ "name": "Steve",  "age": 32, "budget": 32000 },
{ "name": "Martin",  "age": 16, "budget": 1600 }
] ➞ 62600

'''
# *********************************   Start of the program *****************#
def sum_budgets(people_list):

    for person in people_list:
        if person["age"] ==16:
            person.clear()
    #print(people1)
   # print(people2)

def sum_budget(people_list):
    total_budget = 0
    for person in people_list:
        total_budget += person["budget"]
        return total_budget


# list of dictionary
people1 = [
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]

people2 = [
    {"name": "John", "age": 21, "budget": 29000},
    {"name": "Steve", "age": 32, "budget": 32000},
    {"name": "Martin", "age": 16, "budget": 1600}
]


print("Total budget of peopel list 1:", sum_budget(people1))
print("Total budget of peopel list 1:", sum_budgets(people1))
print("Total budget of peopel list 1:", sum_budgets(people2))
print("Total budget of peopel list 1:", sum_budget(people2))

# ************** End of the program ************************
