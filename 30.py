# ask the marks and print the grade
# 90-100  A
#80-89    B
#70-79    C
#60-69    D
#Below 60  Fail

print("enter the marks")
eg=int(input("enter the english sub mark"))
math=int(input("enter the Math sub mark"))
sci=int(input("enter the Sci sub mark"))
total=eg+math+sci
m=(total*100)/300
print("Total Mark=",total)
if m<60:
    print("fail")
elif(m<=69):
    print("D")
elif(m<=79):
    print("c")
elif m<=89:
    print("B")
elif m<=100:
    print("A")
else:
    print("Invaild Number")
