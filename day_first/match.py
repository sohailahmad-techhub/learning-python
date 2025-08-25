day = int(input("Enter day (1-31): "))
match day:
    case 1:
        print("It's the 1st day of the month.")
    case 2:
        print("It's the 2nd day of the month.")
    case 3:
        print("It's the 3rd day of the month.")
    case _:
        print("It's some other day of the month.")
