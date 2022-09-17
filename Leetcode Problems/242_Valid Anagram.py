def isAnagram(s,t):
    dict_t= {}
    dict_s = {}
    if len(s)!= len(t):
        return False
    for i in range(len(s)):
        dict_s[s[i]] = s[i]
        dict_t[t[i]] = t[i]
    dict_t= set(dict_t)
    dict_s= set(dict_s)
    print(dict_s,dict_t)
    if dict_s == dict_t:
        return True
    else:
        return False
s = "aacc"
t = "cacc"
print(isAnagram(s,t))