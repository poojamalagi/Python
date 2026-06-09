#Data type converter game
while True:
    print("select the option from the menu")
    print("\n1.list to tuple.\n2.tuple to list.\n3.list to set.\n4.list to dict")
    choice=int(input("enter your choice of data converter option from above="))
    if choice<1 or choice>4:
        print("invaild number,Please enter the number from givem option")
        continue
    n=int(input("enter the number size"))
    a=[]
    for i in range(n):
        valu=(input("enter the values"))
        
        if valu.isdigit():
            a.append(int(valu))
        else:
            a.append(valu)        
    if choice==1:
        tu=tuple(a)
        print("Tuple",tu)
    elif choice==2:
        num=tuple(a)
        print("list",list(num))
    elif choice==3:
        num=set(a)
        print("set=",num)
    elif choice==4:
        num=dict(enumerate(a))
        print(num)
    i=(input("Do you want to continue? (y/no):"))  
    if i.lower()=='no':
        print("program terminated")
        break

