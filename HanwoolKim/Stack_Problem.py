def pair(str):
    st = []

    for s in str:
        if (s =='(' or s == '[' or s == '{'):
            st.append(s)
        else:
            if((st[-1] == '(' and s == ')') or ((st[-1] == '[' and s == ']')) or ((st[-1] == '{' and s == '}'))):
                st.pop()

    if (len(st) == 0):
        print(True)
    else:
        print(False)


pair("()(())")


