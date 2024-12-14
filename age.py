try:
    Age = int(input("Enter your age"))

    if Age%2==0:
        print("Your age is a even number")
    elif Age%2==1:
        print("your Age is a odd number")

except ValueError:
    print("Enter valid number")