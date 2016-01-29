import re



exp = "((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))"

def inorder_to_postorder(exp):
    operator = "+-*/()"                     # 연산자들을 선언
    result = list()                     # 후위 표기법으로 결과가 저장되는 리스트
    stack = list()                      # list를 스택으로 사용함.
    for symbol in exp:
        if symbol not in operator:          # 숫자일 경우 바로 결과리스트에 넣는다.
            result.append(symbol)
        else:
            if symbol in "+-*/":        # 더하기, 빼기, 곱하기, 나누기 연산자일 경우
                stack.append(symbol)    # 후위 표기법으로 변환하기 위하여 우선 별도 스택에 임시로 저장.
            elif symbol == ")":         # 닫는 괄호 ) 일 경우 저장해 연산자 하나를 결과리스트에 추가한다.
                result.append(stack.pop())      # 이 때 pop()을 통해 스택을 하나 비운다.
    while len(stack) != 0:              # 스택에 남아 있는 연산자들을 pop()으로 하나씩 결과리스트에 붙여주면
        result.append(stack.pop())      # 중위 표기법에서 후위 표기법으로 변환 완료!
    return ''.join(result)


def sum_func(s):
    if s[2] is '+':
        return int(s[0])+int(s[1])
    elif s[2] is '-':
        return int(s[0])-int(s[1])
    elif s[2] is '*':
        return int(s[0])*int(s[1])
    else:
        return int(s[0])/int(s[1])

post_exp = inorder_to_postorder(exp)

print(post_exp)

def calc(exp):
    operator = "+-*/()"                     # 연산자들을 선언
    result = list()                     # 후위 표기법으로 결과가 저장되는 리스트
    stack = list()                      # list를 스택으로 사용함.
    for symbol in exp:
        if symbol not in operator:          # 숫자일 경우 바로 결과리스트에 넣는다.
            result.append(symbol)
        else:
            if symbol in "+-*/":        # 더하기, 빼기, 곱하기, 나누기 연산자일 경우
                stack.append(symbol)    # 후위 표기법으로 변환하기 위하여 우선 별도 스택에 임시로 저장.
            elif symbol == ")":         # 닫는 괄호 ) 일 경우 저장해 연산자 하나를 결과리스트에 추가한다.
                result.append(stack.pop())      # 이 때 pop()을 통해 스택을 하나 비운다.
    while len(stack) != 0:              # 스택에 남아 있는 연산자들을 pop()으로 하나씩 결과리스트에 붙여주면
        result.append(stack.pop())      # 중위 표기법에서 후위 표기법으로 변환 완료!
    return ''.join(result)






# import re
# s = "Example String"
# replaced = re.sub('[ES]', 'a', s)
#
#
# print(re.findall("\d\d[+*/-]", post_exp))
#
#
# while re.findall("\d\d[+*/-]", post_exp):
#     ans = list()
#     a = re.findall("\d\d[+*/-]", post_exp)
#     ans.append(sum_func(a[0]))
#     print(ans)


