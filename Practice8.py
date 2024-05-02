try:
    inputfile= open("new.txt", 'r')
    outputfile = open("outFile.txt", 'w')

    for line in inputfile:
        line = line.rstrip()
        print(line)
        items = line.split()
        print(items)
        salary = float(items[0])
        print(salary)
        name = items[1]
        print(name)

        outputfile.write(name)
        outputfile.write("%10.2f" % salary)
except:
    print("ERROR:")
finally:
    inputfile.close()
    outputfile.close()
    
    
        
