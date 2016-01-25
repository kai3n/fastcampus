def chk_correct(e):

    chk_dict = {'(': ')', '[': ']', '{': '}'}
    match_stack = []

    if len(e) <= 0:
       return e + " ====> 입력값이 없습니다"
    # e의 len이 홀수이면 100% 쌍이 맞지 않는다,첫 값이 values이면 100% 쌍이 맞지 않는다
    elif len(e) % 2 == 1 or e[0] in chk_dict.values():
       return e + " ====>XX Incorrect XX"

    for i in range(0, len(e)):
       if len(match_stack) == 0:
           match_stack.extend(e[i])
       elif match_stack[len(match_stack) - 1] != e[i]:  # 스택에 넣은 마지막 인덱스가 e[i]와 같지 않을 경우..매치 될 가능성이 있음
           if chk_dict.get(match_stack[-1]) == e[i]:  # 키값을 넣어 얻은 value값이 e[i]와 일치하면 pop
               match_stack.pop()
           else:
               match_stack.extend(e[i])
       else:
           match_stack.extend(e[i])

    if len(match_stack) == 0:
       return e + " --->OO Correct OO"
    else:
       return e + " --->XX Incorrect XX"


print(chk_correct('())[]{'))
print(chk_correct('()(()){([()])}'))
print(chk_correct('((()(()){([()])}))'))
print(chk_correct(')(()){([()])}'))
print(chk_correct('('))











###========================
# class match_test:
#     def __init__(self):
#         self.data =[]
#
#     def chk_correct(self, e):
#         chk_dict = {'(':')','[':']','{':'}'}
#         match_stack = []
#
#         if len(e) <= 0:
#             return e+" ====> 입력값이 없습니다"
#         #e의 len이 홀수이면 100% 쌍이 맞지 않는다,첫 값이 values이면 100% 쌍이 맞지 않는다
#         elif len(e)%2 == 1 or e[0] in chk_dict.values():
#             return e+" ====>XX Incorrect XX"
#
#         for i in range(0, len(e)):
#             if len(match_stack)==0:
#                 match_stack.extend(e[i])
#             elif match_stack[len(match_stack)-1] != e[i]: #스택에 넣은 마지막 인덱스가 e[i]와 같지 않을 경우..매치 될 가능성이 있음
#                 if chk_dict.get(match_stack[len(match_stack)-1]) == e[i]:#키값을 넣어 얻은 value값이 e[i]와 일치하면
#                     del match_stack[len(match_stack)-1] #
#                 else:
#                     match_stack.extend(e[i])
#             else:
#                 match_stack.extend(e[i])
#
#         if len(match_stack) == 0:
#             return e+" --->OO Correct OO"
#         else:
#             return e+" --->XX Incorrect XX"
#
#
#
# M = match_test()
# print(M.chk_correct('())[]{'))
# print(M.chk_correct('()(()){([()])}'))
# print(M.chk_correct('((()(()){([()])}))'))
# print(M.chk_correct(')(()){([()])}'))
# print(M.chk_correct('('))

