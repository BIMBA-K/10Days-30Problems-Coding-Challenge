pin = int(input("Enter your PIN: "))

def check_pin(pin):
    count = 0
    temp = pin

    while temp > 0:
        count += 1
        temp = temp // 10

    if count == 4:
        return "Valid PIN"
    else:
        return "Invalid PIN"

print(check_pin(pin))