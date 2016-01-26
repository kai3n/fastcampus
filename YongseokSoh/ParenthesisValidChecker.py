from YongseokSoh import ArrayStack



string = "((()(()){([()])}))"

S = ArrayStack.ArrayStack()

for i in range(len(string)):
    if S.is_empty() is True:
        if string[i] is ')' or string[i] is '}' or string[i] is ']':
            raise Exception("Invalid Parenthesis - 1")
        else:
            S.push(string[i])

    elif string[i] is '(' or string[i] is '{' or string[i] is '[':
        S.push(string[i])

    elif string[i] is ')' or string[i] is '}' or string[i] is ']':
        if string[i] is ')' and S.top() is '(':
            S.pop()
        elif string[i] is '}' and S.top() is '{':
            S.pop()
        elif string[i] is ']' and S.top() is '[':
            S.pop()
        else:
            raise Exception("Invalid Parenthesis - 2")
    else:
        print("Unexpected input", string[i])

if S.is_empty() is False:
    raise Exception("Invalid Parenthesis - Went through string but is not empty")
else:
    print("Valid Parenthesis Expression")



    # elif string[0] is '(':
    #     S.push('(')
    # elif string[0] is '{':
    #     S.push('{')
    # elif string[0] is '[':
    #     S.push('[')
    #
    #
    # elif string[0] is ')':
    #     if S.top() is '(':
    #         S.pop()
    #     else:
    #         raise Exception("Invalid Parenthesis: Expecting )")
    #
    # elif string[0] is '}':
    #     S.push('{')
    # elif string[0] is ']':
    #     S.push('[')
    #
    #
    #
    # elif element is ')':
    #     if S.pop() is not element:
    #         raise Exception("Invalid Parenthesis")
    # elif element is '}':
    #     if S.pop() is not element:
    #         raise Exception("Invalid Parenthesis")
    # elif element is ']':
    #     if S.pop() is not element:
    #         raise Exception("Invalid Parenthesis")



