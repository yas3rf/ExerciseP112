num1 = input("enter a number: ")
num2 = input("enter a number: ")
num3 = input("enter a number: ")
print(f"the entered numbers are : {num1} {num2} {num3}\n")
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is greatest. ")
    else:
        print(f"{num3} is greatest. ")
elif num2 > num3:
    print(f"{num2} is greatest. ")
else:
    print(f"{num3} is greatest. ")

