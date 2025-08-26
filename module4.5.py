correct_username = 'python'
correct_password = 'rules'
user_input_name = input("Enter your username: ")
user_input_password = input("Enter your password: ")
try_count = 1

while user_input_name != correct_username or user_input_password != correct_password:

    if try_count < 5:
        print("Wrong username or password.")
        user_input_name = input("Enter your username: ")
        user_input_password = input("Enter your password: ")
        try_count += 1
    else:
        print("Access denied.")
        break

else:
    print("Welcome.")