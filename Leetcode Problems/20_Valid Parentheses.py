input="]"
stack = []
for i in range(len(input)):
    if len(stack)==0:
        print(False)
    if input[i] == "(":
        stack.append(")")
    elif input[i] == "{":
        stack.append("}")
    elif input[i] == "[":
        stack.append("]")
    else:
        if input[i] == ")" and stack[-1] == ")":
            stack.pop()
        elif input[i] == "]" and stack[-1] == "]":
            stack.pop()          
        elif input[i] == "}" and stack[-1] == "}":
            stack.pop()
        else:
            print(False)
if len(stack)==0:
    print(True)
else:
        print(False)