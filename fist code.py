import math
#Tinh delta
print("Pt bậc 2 có dạng:ax^2+bx+c=0")
a=int(input("Nhập a: "))
b=int(input("nhập b: "))
c=int(input("nhập c: "))
delta=b**2-4*a*c
print("delta=",delta)
if delta < 0:
    print("phương trình vô nghiệm")
elif delta == 0:
    truonghop2=-b/(2*a)
    print("delta=0 ket qua la=",truonghop2) 
elif delta > 0:
    truonghop3=x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("truonghop3 x1=:",truonghop3)
    print("truong hop3 x2=",x2)