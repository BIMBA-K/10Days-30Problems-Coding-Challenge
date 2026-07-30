age=int(input("Enter your age: "))
def cinema_ticket(age):
    if age<5:
        return "Free"
    elif age>=5 and age<=17:
        return 150
    else:
        return 250
ticket_price=cinema_ticket(age)
if ticket_price=="Free":
    print("You can watch the movie for free here Baby.")
    print("Enjoy the movie Baby and Grab ur popcorn")
else:
    print(f"please pay {ticket_price*0.18+ticket_price} for your movie ticket.")
    print("Enjoy the movie my dear lady or gentleman and Grab ur popcorn")
