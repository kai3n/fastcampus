


def num_generator(n):

    print("Function Start")
    while n < 6:
        yield n
        n += 1
    print("Function End")


for i in num_generator(2):
    print (i)

