strs = ["flower","flow","flight"]
count = 0
ccount = 0

for i in range(len(strs[0])):
    # if strs[0] == "":
    #     break
    bully = True
    for s in strs:
        if i>=len(s):
            bully = False
            break
        if strs[0][i] != s[i]:
            bully = False
            break
    
    if bully == False:
        break
    ccount +=1
print(strs[0][:ccount])