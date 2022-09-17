path = "/a/./b/../../c/"
path = path.split("/")
stack = []
for i in range (len(path)):
    if(len(path[i])==0) or (path[i]=="."):
        continue
    if path[i] == (".."):
        if len(stack)!=0:
            stack.pop()
        else:
            continue
    else:
        stack.append(path[i])
final_str = "/"+"/".join(stack)
print(final_str)