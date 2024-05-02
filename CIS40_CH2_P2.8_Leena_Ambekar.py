#Chapter2 P2.8
# This program asks user for the lengths of the sides of rectangle
# and Calculates area and perimeter of rectangle
# Calculates length of the diagonal

import math

# ask user for the length of the sides of rectangle
height = float(input("Please enter height of the rectangle :"))
width = float(input("Please enter width of the rectangle :"))

# calculate area of the rectangle
are_rect = round((height * width),2)

# calculate perimeter of the rectangle
perimeter_rect = round(((height + width) * 2), 2)

# print the area and perimeter of rectangle
print("Area of the rectangle =", are_rect , "\nperimeter of the rectangle =",perimeter_rect)

# Calculate length of the diagonal
len_diagonal = round(math.sqrt((height ** 2) + (width ** 2)), 2)

# Print length of the diagonal
print("Length of the diagonal =", len_diagonal)


## Result
# Please enter height of the rectangle :5.5
# Please enter width of the rectangle :6.5
# Area of the rectangle = 35.75 
# perimeter of the rectangle = 24.0
# Length of the diagonal = 8.51
