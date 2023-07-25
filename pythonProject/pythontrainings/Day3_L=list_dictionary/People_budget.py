# def sum_budgets(people):
#     total_budget = 0
#     for person in people:
#         try:
#             total_budget += person["budget"]
#         except KeyError:
#             pass
#     return total_budget
# people = [
#     { "name": "John", "age": 21, "budget":80000 },
#     { "name": "Steve",  "age": 32, "budget":30000 },
#     { "name": "Martin",  "age": 16, "budget":70000 }
# ]
# print(sum_budgets(people))

def sum_budgets(people_list):
    total_budget = 0
    people_list = [person for person in people_list
                   if person['age'] != 16]
    print(people_list)
    for person in people_list:
        total_budget += person['budget']
    return total_budget

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


print("Total budget of peopel list 1:", sum_budgets(people1))
#print(peo)

print("Total budget of peopel list 1:", sum_budgets(people2))
