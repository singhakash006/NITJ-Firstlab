# print("{:*^20}".format("BILL"))

quantity = float(input("Enter the quantity of item: "))
price_per_item = float(input("Enter the price of items: "))
amount = quantity * price_per_item
discount = float(input("Enter discount :"))
discount_total = amount - ((discount*100)/amount)
tax = float(input("Enter tax amount: "))
tax_total = discount_total - ((discount_total*tax)/100)

print(format("BILL", "*^54"))
print("*************************BILL*************************")
print("Quantity Sold  :", format(quantity, ">36"))
print("Price_Per_Item :", format(price_per_item, ">36"))
print()
print("Amount :", format(amount, ">44"))
print("Discount: ", format(discount_total, ">43"))
print("Tax: ", format(tax_total, ">48"))