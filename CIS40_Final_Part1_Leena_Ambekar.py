'''
## CIS40_Final_Part1
# Leena Ambekar
 This is a menu driven program which shows:
1. Display the food menu to a user (Just show the 5 options - No need to show the Combos!)
2. Ask the user what he/she wants and how many of it.
3. Keep asking the user until he/she chooses the end order option.
4. Calculate the price.
5. Ask the user whether he/she is a student or a staff.
There is no tax for students and 9% tax for staffs.
Add the tax price to the total price.
6. Display the bill to the user. The bill includes:
    The food items
    The quantities
    The cost of them
    The total before tax
    Tax amount
    Total price after tax
7. It prints bill on the screen and also in a file.
8. output file format is "yyyy-mm-dd h-m-sec.txt"
9. it uses dictonary as a data structure 
'''

import datetime;

# Create a class :
class DeAnzaBurger():
    
    percentTax = 0.09
    quantity = 0
    # create a constructor
    def __init__(self):
        
        # constants:
        self.option1 = "De Anza Burger"
        self.option2 = "Bacon Cheese" 
        self.option3 = "Mushroom Swiss"
        self.option4 = "Western Burger" 
        self.option5 = "Don Cali Burger" 
        self.price_option1 = 5.25
        self.price_option2 = 5.75
        self.price_option3 = 5.95
        self.price_option4 = 5.95
        self.price_option5 = 5.95
        
        # Create a dictionary having menu items as key and its price as value
        self.priceDict = {self.option1:self.price_option1,self.option2:self.price_option2,self.option3:self.price_option3,self.option4:self.price_option4,self.option5:self.price_option5}

        # create TimeStamp
        self.orderTimeStamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        
        self.orderDict = {}
        self.priceBeforeTax = 0
        self.priceAfterTax = 0
        self.percentTax = 0.09
        self.totalTax = 0.00

# ==============================================================================================
    # give call to other methods/ functions from main()   
    def main(self):

        # Display the menu option on the screen
        self.displayMenu()

        # asks user input and stores data in dictionary
        self.orderDict = self.getInput()
        print("")

        #Calculates bill
        self.calculateOrder()
        print("")

        # create output File in Timestamp format and stores billing data in it.
        self.createTimeStampFile()

        print("***** Thank You for your order *****")
        
# ==============================================================================================

# displayMenu function shows the 5 food menu options to user.
# this function gives call to functions for menu options which gives details of that menu option.
    def displayMenu(self):
        try:
            print(10 * "*"+"Burger Club" + 10 * "*")
            print("")
            self.deAnzaBurger()
            print("")
            self.baconCheese()
            print("")
            self.mushroomSwiss()
            print("")
            self.westernBurger()
            print("")
            self.donCaliBurger()
            print("")
        except Exception as exceptObj:
            print("displayMenu ERROR:")
            self.errorLog("\nProblem in displayMenu():" + str(Exptobj))

# ==============================================================================================
   ## These methods gives detailed discription of menu options.
    def deAnzaBurger(self):
        print("-- 1. ",self.option1, " --")
        print("Ingredients: Charbroiled Beef Patty, Green Leaf, Tomato, white Cheddar on toasted Bun, Red Onion ")
        print("Price:$", self.price_option1)
       
    def baconCheese(self):
        print("-- 2. ",self.option2, " --")
        print("Ingredients: Charbroiled Beef Patty, smoked Bacon, Caramelized Onion & American Cheese on oasted Bun.")
        print("Price:$", self.price_option2)

    def mushroomSwiss(self):
        print("-- 3. ",self.option3, " --")
        print("Ingredients: Beef Patty, Mushrooms & Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, &Tomato on toasted Bun.")
        print("Price:$", self.price_option3)

    def westernBurger(self):
        print("-- 4. ",self.option4, " --")
        print("Ingredients: Charbroiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce& American Cheese on Toasted Bun.")
        print("Price:$", self.price_option4)

    def donCaliBurger(self):
        print("-- 5. ",self.option5, " --")
        print("Ingredients: Charbroiled Beef Patty, Spring Mix Lettuce, Tomato, Red Onion, Avocado, smoked Gouda & Bacon on Toasted Bun")
        print("Price:$", self.price_option5)

# ====================================================================================

# Accept order input from user.
    def getInput(self):
        try:
            print("\nAre you placing order for Student or Staff?")
            self.status=int(input("Please enter 0 for a Student or 1 for a Staff:"))
            if self.status == 0 or self.status == 1:
                print("\nPlease enter Menu Option 1-5 of your choice:")
                self.order = True

                while self.order:
                    self.menuOption = int(input("Menu Option:"))
                    self.quantity = int(input("Quantity:"))

                    if self.menuOption < 6:
                        self.userInput = self.chooseOption(self.menuOption)

                        self.orderDict[self.userInput] = self.quantity
                    else:
                        print("Please enter menu option 1-5 only....\n")
                            
                    self.moreOrder=input("\nDo you want to place more order: y/n:")
                    if self.moreOrder == 'n':
                        self.order = False
                 
            else:
                print("Please enter 0 or 1 only.\n")
                
            return self.orderDict

        except ValueError:
            print("**Error**:Could not convert entered data to an integer.")
            self.errorLog("Problem in getInput():Could not convert data to an integer.")

        except Exception as exceptObj:
            print("**ERROR**")
            self.errorLog("Problem in getInput():" + str(Exptobj))


# ==============================================================================================

    def chooseOption(self,menuOption):
        if self.menuOption == 1:
            self.userInput = self.option1
        elif self.menuOption == 2:
            self.userInput = self.option2
        elif self.menuOption == 3:
            self.userInput = self.option3
        elif self.menuOption == 4:
            self.userInput = self.option4
        elif self.menuOption == 5:
            self.userInput = self.option5
        return self.userInput

# ==============================================================================================

    def calculateOrder(self):
        try:
            for entry in self.orderDict:
                price = self.orderDict[entry]
                quantity = self.priceDict[entry]
            
                beforeTax = round(price * quantity,2)
                self.priceBeforeTax = self.priceBeforeTax + beforeTax
                
                if self.status == 1:
                    tax = round(price * quantity * self.percentTax,2)
                                      
                elif self.status == 0:
                    tax = 0.00
                    
                self.totalTax = self.totalTax + tax
                afterTax =round(price * quantity + tax,2)
                self.priceAfterTax = self.priceAfterTax + afterTax  
                
        except Exception as Exptobj:
            print("**ERROR**")
            self.errorLog("Problem in calculateOrder():" + str(Exptobj))

# ==============================================================================================

    def createTimeStampFile(self):
        try:
            
            outputFile = self.orderTimeStamp + ".txt"

            # open the file to write the bill
            fileHandleToSaveTheBill = open(outputFile,'w')

            # write the Bill in file..
            fileHandleToSaveTheBill.write("Your Order is:\n")

            for items in self.orderDict:
                line = str(self.orderDict[items]) + "\t" + items
                fileHandleToSaveTheBill.write("\n"+line+ "\t $ %0.2f" % self.priceDict[items])
                

            # Price before tax
            fileHandleToSaveTheBill.write("\nPrice Before tax is :$% 0.2f" % self.priceBeforeTax )
            fileHandleToSaveTheBill.write("\nTotal tax is :$% 0.2f " %  self.totalTax)
            fileHandleToSaveTheBill.write("\nTotal Bill Price is:$% 0.2f " % self.priceAfterTax )

        except Exception as Exptobj:
            print("**ERROR**")
            self.errorLog("Problem in createTimeStampFile():" + str(Exptobj))

        finally:
            fileHandleToSaveTheBill.close()

# ==============================================================================================

    def errorLog(self,msg):
        try:            
            errorLogFile = open("ErrorLog.txt",'a')
            errorLogFile.write("\n"+self.orderTimeStamp + ":" + msg)
         
        except Exception as ExceptObj:
            print("Error in loging error..." + str(ExceptObj))
        finally:
            errorLogFile.close()

# ==============================================================================================

# Create an object of a class        
theOrder = DeAnzaBurger()

# access main() method
theOrder.main()

##END###
# ==============================================================================================

### RESULT#####

''''====== RESTART: /Users/leena/Python/CIS40_Final_Part1_Leena_Ambekar.py ======
**********Burger Club**********

-- 1.  De Anza Burger  --
Ingredients: Charbroiled Beef Patty, Green Leaf, Tomato, white Cheddar on toasted Bun, Red Onion 
Price:$ 5.25

-- 2.  Bacon Cheese  --
Ingredients: Charbroiled Beef Patty, smoked Bacon, Caramelized Onion & American Cheese on oasted Bun.
Price:$ 5.75

-- 3.  Mushroom Swiss  --
Ingredients: Beef Patty, Mushrooms & Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, &Tomato on toasted Bun.
Price:$ 5.95

-- 4.  Western Burger  --
Ingredients: Charbroiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce& American Cheese on Toasted Bun.
Price:$ 5.95

-- 5.  Don Cali Burger  --
Ingredients: Charbroiled Beef Patty, Spring Mix Lettuce, Tomato, Red Onion, Avocado, smoked Gouda & Bacon on Toasted Bun
Price:$ 5.95


Are you placing order for Student or Staff?
Please enter 0 for a Student or 1 for a Staff:1

Please enter Menu Option 1-5 of your choice:
Menu Option:2
Quantity:30

Do you want to place more order: y/n:y
Menu Option:4
Quantity:21

Do you want to place more order: y/n:n


***** Thank You for your order *****
>>> 
'''
##RESULT####
'''====== RESTART: /Users/leena/Python/CIS40_Final_Part1_Leena_Ambekar.py ======
**********Burger Club**********

-- 1.  De Anza Burger  --
Ingredients: Charbroiled Beef Patty, Green Leaf, Tomato, white Cheddar on toasted Bun, Red Onion 
Price:$ 5.25

-- 2.  Bacon Cheese  --
Ingredients: Charbroiled Beef Patty, smoked Bacon, Caramelized Onion & American Cheese on oasted Bun.
Price:$ 5.75

-- 3.  Mushroom Swiss  --
Ingredients: Beef Patty, Mushrooms & Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, &Tomato on toasted Bun.
Price:$ 5.95

-- 4.  Western Burger  --
Ingredients: Charbroiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce& American Cheese on Toasted Bun.
Price:$ 5.95

-- 5.  Don Cali Burger  --
Ingredients: Charbroiled Beef Patty, Spring Mix Lettuce, Tomato, Red Onion, Avocado, smoked Gouda & Bacon on Toasted Bun
Price:$ 5.95


Are you placing order for Student or Staff?
Please enter 0 for a Student or 1 for a Staff:saa
**Error**:Could not convert entered data to an integer.

**ERROR**

**ERROR**
***** Thank You for your order *****
>>> '''
