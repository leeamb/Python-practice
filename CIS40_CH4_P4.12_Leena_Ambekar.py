# CIS40_CH4_P4.12
# Leena Ambekar
#This program reads a word and prints all substrings , sorted by length

mystr= input("Please enter a string:")

length= len(mystr)

for i in range(1, length +1):
    for pos in range(0, length - i +1):
        print(mystr[pos:pos+i])

