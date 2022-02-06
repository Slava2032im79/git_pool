def is_prime (x):
    b = True
    for i in range(2, int(x ** 0)):
        if x % i ==0:
            b = False
    return (b)
a = int(input('введите число '))
print((is_prime(a)))

a = int(input('введите сторону квадрата '))
def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k


def arithmetic(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else:
        return ("Invalid operation")


print(arithmetic(2, 6, '+'))
print(arithmetic(2, 5, '*'))
print(arithmetic(4, 4, '-'))
print(arithmetic(4, 9, '/'))
print(arithmetic(4, 7, 0))


a = input('Введите слово: ')
def is_Palindrome(a):
    s = a.lower()
    if s == s[::-1]:
        print('Является палиндромом')
    else:
        print('Не является палиндромом')