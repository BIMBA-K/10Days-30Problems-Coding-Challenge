c=0
d=0
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        c+=1
    else:
        d+=1
print(f"Even numbers={c}")
print(f"Odd numbers={d}")