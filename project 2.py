#asking you to build a small KBC (Kaun Banega Crorepati) quiz game using Python lists.
question=[["what is indian capital name?", "Delhi"],["who is our PM?","modi"]]
money=0
for i in question:
    print(i[0])
    ans=input("enter your ans")
    if ans.lower()==i[1].lower():
        print("ans correct")
        money+=100
    else:
        print("wrong")
        break
print("won",money)