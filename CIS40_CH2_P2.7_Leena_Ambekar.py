#Chapter 2 P2.7
#This program takes radius and prints -
# - the area and circumference of the circle with that radius
# - the volume and surface area of the sphere with that radius

#Define a constant
_PI = 3.14

# Accept radius value from user
radius = float(input("Please Enter radius :"))

# Calculate area of circle
area_circle = round(_PI * (radius ** 2), 2)

#Calculate circumference of circle
circumference_circle = round(2 * _PI * radius , 2)

#print value of area and circumference of the circle
print("Area of Circle =",area_circle ,"\nCircumference of circle =", circumference_circle)


# Calculate volume of the Sphere
volume_sphere = round(4/3 * _PI * (radius ** 3) , 2)

# Calculate Surface area of the Sphere
surface_area_sphere = round(4 * _PI * (radius ** 2))

#print volume and Surfacce area of the sphere
print("Volume of the Sphere = ", volume_sphere, "\nSurface area of the Sphere = ",surface_area_sphere)


## Result
# Please Enter radius :5
# Area of Circle = 78.5 
# Circumference of circle = 31.4
# volume of the Sphere =  523.33 
# Surface area of the Sphere =  314
