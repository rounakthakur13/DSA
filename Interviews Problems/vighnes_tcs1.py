N1 = 3
N2 = 3
a = [3,9]
b = [1, 2, 3]
c = a
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
c.sort()
if len(c) % 2 == 0:
    d = c[len(c)//2] + c[(len(c)//2)-1]
    print(d/2)
else:
    print(c[len(c)//2])