'''  CIS40_MidTerm
     Leena Ambekar
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
    Total price after tax '''
# constants:

option1 = "De Anza Burger"
option2 = "Bacon Cheese" 
option3 = "Mushroom Swiss"
option4 = "Western Burger" 
option5 = "Don Cali Burger" 
price_option1 = 5.25
price_option2 = 5.75
price_option3 = 5.95
price_option4 = 5.95
price_option5 = 5.95

percentTax = 0.09
quantity = 0
# main function calls all other functions.
def main():    
    displayMenu()
    print("")
    getOrder()
    print("")



# ===============================================================================================


# displayMenu function shows the 5 food menu options to user.
# this function gives call to functions for menu options which gives details of that menu option.
def displayMenu():
    try:
        print(10 * "*"+"Burger Club" + 10 * "*")
        print("")
        deAnzaBurger()
        print("")
        baconCheese()
        print("")
        mushroomSwiss()
        print("")
        westernBurger()
        print("")
        donCaliBurger()
        print("")
    except:
        print("displayMenu ERROR:")
# ==============================================================================================
   
def deAnzaBurger():
    print("-- 1. ",option1, " --")
    print("Ingredients: Charbroiled Beef Patty, Green Leaf, Tomato, white Cheddar on toasted Bun, Red Onion ")
    print("Price:$", price_option1)
   
def baconCheese():
    print("-- 2. ",option2, " --")
    print("Ingredients: Charbroiled Beef Patty, smoked Bacon, Caramelized Onion & American Cheese on oasted Bun.")
    print("Price:$", price_option2)

def mushroomSwiss():
    print("-- 3. ",option3, " --")
    print("Ingredients: Beef Patty, Mushrooms & Swiss Cheese, Garlic Mayo, Green Leaf Lettuce, &Tomato on toasted Bun.")
    print("Price:$", price_option3)

def westernBurger():
    print("-- 4. ",option4, " --")
    print("Ingredients: Charbroiled Beef Patty, Beer Battered Onion Rings, Sriracha BBQ Sauce& American Cheese on Toasted Bun.")
    print("Price:$", price_option4)

def donCaliBurger():
    print("-- 5. ",option5, " --")
    print("Ingredients: Charbroiled Beef Patty, Spring Mix Lettuce, Tomato, Red Onion, Avocado, smoked Gouda & Bacon on Toasted Bun")
    print("Price:$", price_option5)

# ====================================================================================

# This function asks user to enter their order.
def getOrder():
    total_before_tax = 0.0
    total_tax = 0.0
    total_pay = 0.0

    try:
        print("Are you placing order for Student or Staff?")
        status=int(input("Please enter 0 for a Student or 1 for a Staff:"))
        if status ==0 or status == 1:
            print("")
            print("Please Enter menu option (1-5) of your choice.")
            order = True
            totalpay = 0.0
            while order :
                option = int(input("Menu Option:"))
                quantity = int(input("Quantity:"))
                if option > 5:
                    print("Please Enter Menu option 1-5 only..")
                else:
                    before_tax, tax, pay = calculateOrder(status,option,quantity)

                    total_before_tax = round(total_before_tax + before_tax, 2)
                    total_tax = round(total_tax + tax,2)
                    total_pay = round(total_pay + pay, 2)

                    endOrder = input("Do you want to order more:(yes/ no)")
                    if endOrder == 'no':
                        displayBill(total_before_tax , total_tax , total_pay)
                        order = False
            return option, quantity, total_before_tax , total_tax , total_pay
        else:
            print("Please enter 0 or 1 only")    
    except:
        print("getOrderERROR: Invalid Input :: Please enter values in digits only.")
    

# ======================================================================================

# This Function Calculates the order
def calculateOrder(status,option,quantity):
    try:
        tax = 0.0
        if option == 1:
            price = price_option1
            print(option1, "   $", price_option1, "   ", quantity)
        elif option == 2:
            price = price_option2
            print(option2, "   $", price_option2, "   ",quantity)

        elif option == 3:
            price = price_option3
            print(option3, "   $", price_option3, "   ", quantity)
        elif option == 4:
            price = price_option4
            print(option4, "   $", price_option4, "   ", quantity)
        elif option == 5:
            price = price_option5
            print(option5, "   $", price_option5, "   ", quantity)
        if status == 1:
            tax = round(price * quantity * percentTax, 2)

        before_tax = round(price * quantity,2)

        pay = round(price * quantity + tax , 2)

        return before_tax, tax, pay

    except:
        print("calculateorder ERROR: Invalid input.")


# ==================================================================================================

# This function displays output
def displayBill( total_before_tax , total_tax , total_pay):
    print("The total before Tax:$",total_before_tax)
    print("Tax amount:$", total_tax)
    print("Total price after tax:$", total_pay)
    
#===================================================================================================

    
# Call main function.
main()
