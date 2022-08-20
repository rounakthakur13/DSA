def longestPalindrome(s):
    mid = len(s)//2
    p= mid - 1
    q = mid + 2
    for i in range(len(s)):
        if s[p] == s[q]:
            p+=1
            q-=1
        else:
            return False
    return True
s = "baaab"
print(longestPalindrome(s))