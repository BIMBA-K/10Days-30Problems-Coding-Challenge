amount=int(input("enter the amount: "))
def delivery_fee(amount):
    if amount>=500:
        return 0
    else:
        return 50
x=delivery_fee(amount)
if x==0:
    print(f"wohoooo u have unlocked free delivery ")
    print(f"total bill is {amount+x}")
    
else:
    print(f"delivery fee is {x}")
    print(f"total bill is {amount+x}")
    print(f"shop above 500 to unlock free delivery")