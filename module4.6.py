import random

total_random_points = int(input("How many random points do you want?: \n"))
counter = total_random_points
total_points_inside_circle = 0

while counter > 0:
    horizontal_point = random.randint(-1, 1)
    vertical_point = random.randint(-1, 1)
    if ((horizontal_point ** 2) + (vertical_point ** 2)) < 1:
        counter -= 1
        total_points_inside_circle += 1
    else:
        counter -= 1

value_of_pi = 4 * (total_points_inside_circle / total_random_points)
print(f"There are {total_points_inside_circle} points inside the circle.")
print(f"The value of pi is {value_of_pi}.")

