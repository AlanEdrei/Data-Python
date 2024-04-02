def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def fact_I (n):
    if n == 0:
        return 1
    total = n
    i=n-1
    while i > 0:
        total = total*i
        i = i-1
    return total

print(fact_I(0))
