'''CIS40_Ch7_Ex1
Leena Ambekar
Description:
This program -
1. Ask the user to enter the backend error log file name ("ErrorLog.txt")
2. Read the file (ErrorLog.txtPreview the document)
3. Count the lines in the file
4. Count how many words "error", "Error" and "ERROR" are in the log file.
5. Print the lines which have a word "error", "Error" and "ERROR"
6. Write items 3, 4 and 5 in a report file (name the report file "reportError.txt")
'''

inFile = "ErrorLog.txt"
outFile = "ReportLog.txt"

count = 0
err_count = 0

try:
    infile_handle = open(inFile, 'r')
    outfile_handle = open(outFile, 'w')

    for line in infile_handle:
        line = line.rstrip()
        count = count +1
        if 'error' in line.lower():
            print(line)
            err_count = err_count + 1
            print(line, file=outfile_handle)
    print("Number of line in the file: ", count, file=outfile_handle)

    print("number of time error word occurred is: ", err_count, file=outfile_handle)

except:
    print("ERROR: ")
finally:
    infile_handle.close()
    outfile_handle.close()


    
'''Result:
/Users/leena/PycharmProjects/Ch7/venv/bin/python /Users/leena/Python/Chapter7/CIS40_CH7_EX1_Leena_Ambekar.py
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A

Process finished with exit code 0'''
