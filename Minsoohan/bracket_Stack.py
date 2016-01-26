from stack import ArrayStack
a = '((()(()){([()])}))'
b= '()(()){([()])}'
c=')(()){([()])}'

S=ArrayStack()
for i in c:
    if i=='(' or i=='{' or i=='[':
        S.push(i)
    else :
        S.pop()


