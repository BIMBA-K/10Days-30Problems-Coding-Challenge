n=int(input("Enter the price: "))
t=n
while n!=0:
    n=int(input("Enter the price: "))
    t+=n
    continue
    if n==0:
        break
print(f"Total bill: {t}")
    