#Chapter 2 P2.6
#This Program accepts user input in meters and convert it into miles , feet and inches

#Accepts input from user.
measurement_meter = float(input("Please enter measurement value in meters:"))

#Convert meters into miles
_mi = 0.00062137  #Creating constant
measurement_miles = round(measurement_meter * _mi, 5)
print(measurement_meter ,"meters = ",measurement_miles, "miles")

#Convert meters into feet
_ft = 3.28084 #creating constant
measurement_feet = round(measurement_meter * _ft, 5)
print(measurement_meter ,"meters = ",measurement_feet, "feet")

#Convert meters into inches
_in = 39.37007874 #Creating constant
measurement_inches = round(measurement_meter * _in, 5)
print(measurement_meter ,"meters = ",measurement_inches, "inches")


##Result
# Please enter measurement value in meters:30
# 30.0 meters =  0.01864 miles
# 30.0 meters =  98.4252 feet
# 30.0 meters =  1181.10236 inches
