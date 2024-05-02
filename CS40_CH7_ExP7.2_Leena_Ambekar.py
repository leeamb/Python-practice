'''
CIS40_CH7_ExP7.2
Leena Ambekar

Discription:
This program accept input from a file and store data in output file ,proceed be line numbers.
'''
try:
    # ask user for input and output file names.
    inFile = input("Please enter input file name:")
    outFile = input("Please Enter output file Name:")

    # Open files
    inFile_handle = open(inFile , 'r')
    outFile_handle = open(outFile, 'w')

    #define a counter
    num = 1

    # start reading a input file
    for line in inFile_handle:
        #line = line.rstrip() # remove /n character from end of a line
        numline = "/* " + str(num) + " */ " + line
        outFile_handle.write(numline) # write in output file
        num = num + 1
    print("Done")

except:
    print("ERROR:",str(exception))
    
finally:
    inFile_handle.close()
    outFile_handle.close()
