from YongseokSoh import ArrayStack

string = "((()(()){([()])}))"

S = ArrayStack.ArrayStack()

for i in string:
    if S.is_empty() is True:
        if i is ')' or i is '}' or i is ']':
            raise Exception("Invalid Parenthesis - 1")
        else:
            S.push(i)

    elif i is '(' or i is '{' or i is '[':
        S.push(i)

    elif i is ')' or i is '}' or i is ']':
        if i is ')' and S.top() is '(':
            S.pop()
        elif i is '}' and S.top() is '{':
            S.pop()
        elif i is ']' and S.top() is '[':
            S.pop()
        else:
            raise Exception("Invalid Parenthesis - 2")
    else:
        print("Unexpected input", i)

if S.is_empty() is False:
    raise Exception("Invalid Parenthesis - Went through string but is not empty")
else:
    print("Valid Parenthesis Expression")

