from array_stack import ArrayStack
a = '((()(){([()])}))'
cd = '((({{}})))'
b= '()(()){([()])}'
c=')(()){([()])}'
d='(}'

S=ArrayStack()
list_a = []
for i in a:
    if i=='(' or i=='{' or i=='[':
        S.push(i)
        print("1",S.data)
    elif i==')' and S.top()=='(':
        S.pop()
        print("2",S.data)
    elif i=='}' and S.top()=='{':
        S.pop()
        print("3",S.data)
    elif i==']' and S.top()=='[':
        S.pop()
        print("4",S.data)



print(S.is_empty())
