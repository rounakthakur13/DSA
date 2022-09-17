def longestPalindrome(s):
    def palicheck(l,r,s):
        while(l>=0) and (r<len(s)) and s[r] == s[l]:
            l-=1
            r+=1
        return s[l+1:r]
    str=s
    for i in range(len(s)):
        tempeven = palicheck(i,i,s)
        tempodd = palicheck(i,i+1,s)
        if len(tempeven) !=0 and len(tempodd)!=0:
          str= min(str,tempeven,tempodd,key=len)
        else:
            continue
    return str
s = "abba"
print(longestPalindrome(s))