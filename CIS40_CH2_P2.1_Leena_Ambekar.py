# This program displays the diamention of (8.5 * 11 inch) sheet of paper in milimeter

width = 8.5 #in inches
length = 11 #in inches

# define a constanst
mm_per_inch = 25.4

# inch to milimeter converstion
new_width = round(width * mm_per_inch ,2) #result rounded to 2 decimal points
new_length = round(length * mm_per_inch,2)

print("Diamentions of sheet in inches: ", width , " * ", length)
print("Diamentions of sheet in milimeter: ", new_width , " * ", new_length)


## Result
#Diamentions of sheet in inches:  8.5  *  11
#Diamentions of sheet in milimeter:  215.9  *  279.4
