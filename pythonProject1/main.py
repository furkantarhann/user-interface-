print("******************************************")
print("              X   COMPANY                 ")
print("******************************************")

answer= input("Sign in(Y) or Sign up(N)?")
if answer=="Y" or answer=="y":
    with open("userinformation.txt", "r") as f:
        content1 = f.readline()
        content2 = f.readline()
    x=1
    while content1!=x:
        x = input("Username: ")
        if x == content1.strip():
            y=1
            while content2!=y:
                y = input("Password: ")
                if y == content2.strip():
                    print("Sign in succesfully completed")
                    x=content1
                    y=content2
                else:
                    print("Wrong password.Try Again!")

        else:
            print("Wrong username.Try Again!")
elif answer=="N" or answer=="n":
    content3=input("New username: ")
    content4=input("New password: ")
    with open("userinformation.txt", "w") as f:
        f.write(content3)
        f.write("\n")
        f.write(content4)
    print("Sign un succesfully completed")
else:
    print("Only use 'Y' or 'N' .Try again!")