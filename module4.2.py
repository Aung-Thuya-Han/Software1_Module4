#1 inch is equal to 2.54 cm
user_input = float(input("Enter your input in inches: "))
while user_input >= 0:
    if user_input < 0:
        break
    inch_to_cm = user_input * 2.54
    print(f"{user_input} inches is {inch_to_cm} in cm.")
    user_input = float(input("Enter your input in inches: "))
