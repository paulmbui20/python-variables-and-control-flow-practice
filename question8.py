# Ask the user to enter a number between 1 and 7
day_number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))

# Determine the corresponding day
if day_number == 1:
    print("It's Monday")
elif day_number == 2:
    print("It's Tuesday")
elif day_number == 3:
    print("It's Wednesday")
elif day_number == 4:
    print("It's Thursday")
elif day_number == 5:
    print("It's Friday")
elif day_number == 6:
    print("It's Saturday")
elif day_number == 7:
    print("It's Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")