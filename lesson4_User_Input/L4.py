# input() = A function that prompts the user to ender data 
#           Returns the entered data as a STRING

name = input("What is your name?: ")
#age = input("How old are you?: ") this example is basic but it can be slight better
age = int(input("How old are you?: ")) #this makes it just one line and already converted into integer

#age = int(age) this example is only valid in the first User input for age
age = age + 1

print(f"Hello {name}")#do still note that the whole reason why we are using 'f' or "format" because we want to include a variable
print(f"Ohh so you are currently {age}")
