def factorial(num):
    sum = 1
    while num >=1:
        sum *= num
        num -= 1
    return sum

def factorial_iter(num):
    if num is 0:
        return 1
    else:
        return num*factorial_iter(num-1)


print(factorial(5))

print(factorial_iter(5))