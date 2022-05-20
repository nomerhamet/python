from unicodedata import name


name = input("What is your name ?: ")
age = int(input("What is your age?: "))
height = float(input("What is your height?: "))

print('Hello ' +  name )
print('You are ' + str(age)+ ' byears old')
print('Your height is ' + str(height) + 'cm')