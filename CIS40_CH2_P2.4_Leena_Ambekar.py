# Chapter 2 P2.4

# This program accepts two intergers from user and
# prints - The Sum, The difference, the product,The average, The distance, The maximum and minimum

# Accepts two numbers from user
num1 = int(input("Please enter a interger number: "))
num2 = int(input("Please enter 2nd interger number: "))

#display the Sum
print("Sum is: ", num1 + num2)

#display the difference
difference= max(num1, num2) - min(num1,num2)
print("Difference is :", difference)

#display product
print("Product is: ",num1 * num2)

# display average
print("average is: ", (num1 +num2)/2)

#Display the distance (absolute value of the difference
print("distance is: ",abs(difference))

# Display Maximum
print("Muximum number is: " , max(num1, num2))

#Display Minimum
print("Minimum number is: ", min(num1 , num2))



## Result:
# Please enter a interger number: 34
# Please enter 2nd interger number: 45
# Sum is:  79
# Difference is : 11
# Product is:  1530
# average is:  39.5
# distance is:  11
# Muximum number is:  45
# Minimum number is:  34
