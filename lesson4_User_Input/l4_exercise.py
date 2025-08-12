# Exercise 1 Rectangle Area Calc

length = float(input("What is the length of this Rectangle?: "))
width  = float(input("What is the width of this Rectangle?: "))

area = length * width
print(f"Your Rectangle has an Area of {area}:")


# Exercise 2 Shopping Cart Program
item = input("What Item would you like to add?: ")#Notice that I didn't use str() because it is already set as default as string
price = float(input("How much is it per piece?: "))
quantity = int(input("How many do you have?: "))

total_amount = price * quantity
print(f"Your total amount for your item {item} is : {total_amount}")
