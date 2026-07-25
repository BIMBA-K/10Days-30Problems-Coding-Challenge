count = 0
total = 0
largest = 0

num = int(input("Enter number: "))

while num >= 0:
    count += 1
    total += num

    if num > largest:
        largest = num

    num = int(input("Enter number: "))

print("Total numbers =", count)
print("Sum =", total)
print("Largest =", largest)
