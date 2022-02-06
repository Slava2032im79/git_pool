# def is_prime (x):
#     b = True
#     for i in range(2, int(x ** 0)):
#         if x % i ==0:
#             b = False
#     return (b)
# a = int(input('введите число '))
# print((is_prime(a)))

a = int(input('введите сторону квадрата '))
def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k
