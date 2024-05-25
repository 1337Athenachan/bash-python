#!/usr/bin/python3

# greeting
print("welcome to my item discount helper, simply type in the items price and the percentage discount.")
print("-" * 74 )
# input sale amount
price = float(input("Enter Item Price: "))
amt = float(input("Enter Sale Amount: "))

# checking conditions and calculating discount
total = price - price * amt / 100
print(f"The price of the item is now {total}")
print("\n")
print("Thank you for using my program.")

