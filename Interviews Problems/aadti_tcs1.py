# HW = str(input())
# N = int(input())
# B = str(input())
HW= "alice bob"
N =3
B = "lic bob"
str.lower(B)
str.lower(HW)
HW = HW.replace(" ", "")
B= B.replace(" ","")
print(HW,B)
if B in HW:
    print("Yes")
else:
    print("No")