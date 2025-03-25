price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount of the item: "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent = price * discount_percent / 100
        print("discounted price is: ",round(price * discount_percent/100, 2))
    else:
        print("original price is: ", price)
    
calculate_discount(price, discount_percent)