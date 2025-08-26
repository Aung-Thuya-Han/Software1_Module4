user_number = input("Enter your number: ")
saved_number = []

while user_number != '':
    saved_number.append(float(user_number))
    user_number = input("Enter your number: ")

smallest_num = min(saved_number)
largest_num = max(saved_number)
print(f"The smallest number is: {smallest_num}")
print(f"The largest number is: {largest_num}")
