# Chapter2 P2.3
# This program reads number and displays squar, cube and fourth power.

# Get a number from user
# type cast the user input to interger
number = float(input("Please enter a number: "))

# Calculate square of the number
square_num = (number * number)
print("Square of ",number , "is: ", square_num)

# Calculate Cube of the number
cube_num = (number * number * number)
print("Cube of ", number, "is: ", cube_num)

# Calculate fourth power
fourth_power_num = (number ** 4)
print("fourth power of ", number, "is: ",fourth_power_num)


##Result
# Please enter a number: 23
# Square of  23.0 is:  529.0
# Cube of  23.0 is:  12167.0
# fourth power of  23.0 is:  279841.0
