from .array_stack import ArrayStack, Empty

brackets = ")(()){([()])}"
S = ArrayStack()
bracket_num = 0

for i in range(len(brackets)):
    if brackets[i] == '(' or brackets[i] == ')':
        bracket_num = 1
    elif brackets[i] == '{' or brackets[i] == '}':
        bracket_num = 2
    elif brackets[i] == '[' or brackets[i] == ']':
        bracket_num = 3

    if S.is_empty():
        S.push(bracket_num)
        continue

    if S.top() == bracket_num:
        S.pop()
    else:
        S.push(bracket_num)

if S.is_empty():
    print("Correct")
else:
    print("Incorrect")


