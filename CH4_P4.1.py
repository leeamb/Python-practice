# CIS40_CH4_P4.9
# This programs reads a word and prints it in reverse order

myword = input("Please enter a word :")
print("Entered word is:", myword)
reverse_word = ""

for i in myword:
    reverse_word = i + reverse_word
print("Reversed word is: ",reverse_word)
