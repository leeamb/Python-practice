#Chapter 2 . P2.2
#this program Computes and displays
#1. the perimeter of 8.5 by 11 inch paper sheet and
#2. length of its diagonal

import math

#assigne value of width and length in inches
width = 8.5
length = 11

# Calculate Perimeter
perimeter = round((width + length) * 2 ,2)

# Display value of perimeter
print("Perimeter of the sheet is: ", perimeter, "inches")

# calculate value of diagonal
diagonal_length = round(math.sqrt((width ** 2) + (length ** 2)) ,2)
print("diagonal lenght is : " , diagonal_length ,"inches")


##result
# Perimeter of the sheet is:  39.0 inches
# diagonal lenght is :  13.9 inches
