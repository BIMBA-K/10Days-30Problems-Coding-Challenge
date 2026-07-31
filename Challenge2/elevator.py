c_floor = int(input("Enter current floor: "))
r_floor = int(input("Enter required floor: "))
def move_lift(c_floor,r_floor):
    if r_floor>10 or r_floor<0:
        return "Invalid floor number"
    elif c_floor==r_floor:
        return "Lift is on the same floor"
    else:
        return abs(r_floor-c_floor)
print(move_lift(c_floor,r_floor))