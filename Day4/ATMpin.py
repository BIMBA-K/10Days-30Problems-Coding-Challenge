n=input("Enter your ATM pin: ")
c=0
while n!="1234":
    print("Incorrect pin. Please try again.")
    c+=1
    n=input("Enter the correct pin: ")
    if c==3:
        print("You have entered the wrong pin 3 times. Your account is locked.")
        break
print("Welcome to Canara Bank ATM.")
m=int(input("Enter the amount: "))

