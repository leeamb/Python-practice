# Chapter 2 P2.5

# This program accepts two intergers from user and
# prints folloing in indented format-
# The Sum, The difference, the product,The average, The distance, The maximum and minimum

# Accepts two numbers from user
num1 = int(input("Please enter a interger number: "))
num2 = int(input("Please enter 2nd interger number: "))

#display the Sum
print("Sum is: %17d" %(num1 + num2))

#display the difference
difference= max(num1, num2) - min(num1,num2)
print("Difference is: %10d" %(difference))

#display product
print("Product is: %13d"  %(num1 * num2))

# display average
print("average is: %13d" %((num1 +num2)/2))

#Display the distance (absolute value of the difference
print("distance is: %12d" %(abs(difference)))

# Display Maximum
print("Muximum number is: %6d"  %(max(num1, num2)))

#Display Minimum
print("Minimum number is: %6d" %(min(num1 , num2)))


## Result
# Please enter a interger number: 50
# Please enter 2nd interger number: 40
# Sum is:                90
# Difference is:         10
# Product is:          2000
# average is:            45
# distance is:           10
# Muximum number is:     50
# Minimum number is:     40
