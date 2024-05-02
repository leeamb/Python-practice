try:
    infile= open("Num.txt",'r')

    for line in infile:
        line= line.rstrip()
        if line != 'NA':
            print(line)
    infile.close()
except:
    print("ERROR")
