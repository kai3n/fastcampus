print('*********** Multiplication Calculator*************')


Common = input("Enter a number: ")
Common_more = input("Enter another number: ")

converted_number = int(Common)
converted_another_number = int(Common_more)


def agree(one, two):

    return one * two

new = agree(converted_number,converted_another_number)

print(new)
print(type(new))