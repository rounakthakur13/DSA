def longestPalindrome(s):
    def palicheck(l,r,s):
        while(l>=0) and (r<len(s)) and s[r] == s[l]:
            l-=1
            r+=1
        return s[l+1:r]
    str=""
    for i in range(len(s)):
        tempeven = palicheck(i,i,s)
        tempodd = palicheck(i,i+1,s)
        str= max(str,tempeven,tempodd,key=len)
    return str
s = "babad"
print(longestPalindrome(s))