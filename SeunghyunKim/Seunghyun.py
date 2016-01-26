def factorial(num):
    result = 1
    if num <= 1:
        return 1
    else:
        for x in range(num, 0, -1):
            result *= x
    return result


print(factorial(0))    #1
print(factorial(1))    #1
print(factorial(5))    #120
print(factorial(3))    #6