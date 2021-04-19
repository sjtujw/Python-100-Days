def is_prime(num):
    for item in range(2, num):
        if num % item == 0:
            return False
    return True if num != 1 else False


list1 = [1, 287, 2984, 384, 46, 37, 29, 741]


for item in list1:
    print(is_prime(item))

