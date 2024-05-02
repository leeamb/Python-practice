from csv import reader, writer
try:
    infile = open("movies.csv")
    csvReader = reader(infile)
        
    outfile = open("1990movies.csv",'w')
    csvwriter = writer(outfile)
    csvwriter.writerow(["Name","Year","Actors"])
    csvwriter.writerow([])
        
    for row in csvReader:
        print(row)
            
        if row[1] == "1990":
            newrow = [row[0],row[1],row[4]]


            csvwriter.writerow(newrow)           

except:
        print("ERROR")

finally:
    infile.close()
    outfile.close()
    
