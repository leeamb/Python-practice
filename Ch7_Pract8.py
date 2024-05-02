try:
    inputFile = open("new.txt", 'r')
    outputFile = open("outFile", 'w')

    for line in inputFile:
        line = line.rstrip()
        item = line.split()
        salary = float(item[0])
        name = item[1]
        outputFile.write("Name: ", name)
        outputFile.write("Salary:", salary)
    inputFile.close()
    outputFile.close()

except:
    print("ERROR::")