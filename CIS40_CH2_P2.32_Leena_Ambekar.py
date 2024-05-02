#CIS40_CH2_P2.32
# Leena Ambekar
# This program converts pseudocode . It shows how bookstore computes the price of an order from the total price and the number of the books that were ordered.

#### pseudocode:
# Read the total book price and the number of books
# Computes the tax (7.5 % of the total book prices)
# Compute the shipping charge ($2 /book)
# the price of the order is the sum of the total book price, the tax, and the shipping charge.
# Print the price of order.

#Create constant
shipping_charge = 2
# Read the total book price and the number of books
total_book_price = float(input("Enter total book price: "))
number_books = int(input("Enter number of books: "))

# Computes the tax (7.5 % of the total book prices)
tax =  round(total_book_price * 7.5 / 100, 2)

# Compute the shipping charge ($2 /book)
total_shipping_charge = round(number_books * shipping_charge , 2)

# Compute the price of order
price_of_order = round(total_book_price + tax + total_shipping_charge , 2)

print("Total Price of the order is : ", price_of_order)