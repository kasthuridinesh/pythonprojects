no_row=int(input("Enter the number of row:"))
for row in range(no_row):
    for col in range(row+1):
        print(col+1,end=" ")
    print()

no_row=int(input("Enter the number of row:"))
for row in range(no_row):
    for col in range(row,-1,-1):
        print(col+1,end=" ")
    print()

no_row=int(input("Enter the number of row:"))
for row in range(no_row):
    for j in range(row,-1,-1):
        print(col+1,end=" ")
    print()

no_row=int(input("Enter the number of row:"))
for row in range(no_row):
    for col in range(row,-1,-1):
        print(no_row-row,end=" ")
    print()

