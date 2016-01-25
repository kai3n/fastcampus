import array_stack
S = array_stack.ArrayStack()

def judge(bracket):
    if bracket[0] == ')' or bracket[0] == '}' or bracket[0] == ']':
        return 'Incorrect'
    for c in bracket:
        if c == '(' or c == '{' or c == '[':
            S.push(c)
        elif c == ')' and S.top() == '(':
            S.pop()
        elif c == '}' and S.top() == '{':
            S.pop()
        elif c == ']' and S.top() == '[':
            S.pop()
        else:
            return 'Incorrect'
    for i in S.data:
        if i == '(' or '{' or '[':
            return 'Incorrect'
        else:
            continue
    return 'Correct'

c1 = '('
print(judge(c1))