def MaxYueshu(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def MinBeishu(x, y):
    return x * y // MaxYueshu(x, y)


a = MaxYueshu(18, 24)
b = MinBeishu(18, 24)
print(a)
print(b)
