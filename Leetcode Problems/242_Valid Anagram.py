def isAnagram(s,t):
    dict_t= {}
    dict_s = {}
    if len(s)!= len(t):
        return False
    for i in range(len(s)):
        dict_s[s[i]] = s[i]
        dict_t[t[i]] = s[i]
    
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))