from HanwoolKim import linked_binarytree as lb

def postfix(str):

    result = []
    st = []
    priority_operator = {'+': 0, '-' : 0, '*' : 1, '/' : 1}
    operator = ['+', '-', '*', '/']

    for char in str:
        if ( 48 <= ord(char) and ord(char) <= 57):
            result.append(char)
        elif(char == '('):
            st.append(char)
        elif(char in operator):
            if(len(st) == 0):
                st.append(char)
            else:
                if(st[-1] in operator and priority_operator[st[-1]] >= priority_operator[char]):
                    result.append(st.pop())
                st.append(char)
        elif(char == ')'):
            while(st[-1] != '('):
                result.append(st.pop())
            st.pop()

    if(len(st) != 0):
        result.append(st[-1])
    return result

def cal(str):

    st = []
    operator = ['+', '-', '*', '/']

    for char in str:
        if ( 48 <= ord(char) and ord(char) <= 57):
            st.append(char)
        elif(char in operator):
            num1 = st.pop()
            num2 = st.pop()
            result = 0
            if(char == '*'):
                result = int(num2) * int(num1)
            elif(char == '/'):
                result = int(int(num2) / int(num1))
            elif(char == '+'):
                result = int(num2) + int(num1)
            else:
                result = int(num2) - int(num1)
            st.append(result)
    print(st)



post = postfix("((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))")
print(post)
cal(post)



