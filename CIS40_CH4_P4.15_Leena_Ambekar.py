# CIS40_CH4_P4.15
# Leena Ambekar
# This program accepts a interger number n from user and
# displays nth Fibonacci number.

try:
    n = int(input("Enter a number: "))
    fold1 = 1
    fold2 = 1
    if n >= 3:
        for num in range(3, n+1):
            fnew = fold1 + fold2
            print(num, "-",fnew)
            fold2 = fold1
            fold1 = fnew
        print(n,"th Fibonacci number is: ", fnew)


except:
    print("ERROR: Please enter integer only.")
