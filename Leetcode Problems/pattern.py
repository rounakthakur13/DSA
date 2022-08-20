def pattern30():
    n = 5
    
    for row in range(1,n+1):        
        for space in range(n-row): #space
            print(" ",end=" ")
        for col1 in range(row,1,-1): #left half  
            print(col1,end=" ")
            # count+=1
        for col2 in range(0,row): #right half
            print(col2+1,end=" ")
        print("\t")

def pattern48():
    n = 4
    colinrow = n
    for row in range(1,n*2):
        if row>n:
            colinrow = 2*n - row
        else:
            colinrow = row
        noofspaces = n - colinrow
        for space in range(0,noofspaces):
            print(" ",end="")
        for col in range(0,colinrow):
            print("* ",end="")
        print("\r")
    return " "
print(pattern30())