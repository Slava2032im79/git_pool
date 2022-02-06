def is_prime (x):
    b = True
    for i in range(2, int(x ** 0)):
        if x % i ==0:
            b = False
    return (b)
a = int(input('введите число '))
print((is_prime(a)))

