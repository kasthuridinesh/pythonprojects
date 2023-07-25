
def is_prime(number):
    if number < 2:
        return False
    for num in range(2, number):
        if number % num== 0:
            return False
    return True

for num in range(1, 12):
    if is_prime(num):
        print(num)



