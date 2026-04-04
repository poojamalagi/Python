# 5. Password attempts
# Ask the user to enter a password.
# If the password is "python123", print "Access Granted" and stop
# Otherwise, keep asking (max 3 attempts)
# 👉 Use break

for i in range(1,4):
    pwd=input("enter your password=")
    if(pwd=="python123"):
        print("Acess Granted")
        break
    elif(i==3):
        print("you have excessed 3 attempts")
    else:
     print("Try Again")