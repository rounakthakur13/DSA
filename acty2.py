n = 9
for i in range(n):
    if n-i == n:
        for i in range(n):
            print("* ", end="")
    else:
        print("*", end="")
        for spaces in range((n-i)*2):
            if spaces >= 1:
                print(" ", end="")
    print("*")
print("*")
print()
