# Get an integer for x from the user
x = int(input("Enter an integer for x: "))

# Get an integer for y from the user
y = int(input("Enter an integer for y: "))

# Get a decimal for z from the user
z = float(input("Enter a decimal for z: "))


# Print the product of x and y
print("Product of x and y is",x*y)

# Print the product of x, y, and z
print("Product of x, y, and z is",x*y*z)

# Print the remainder of x divided by 2
# Remember to use modulus (%) to get the remainder
print(x,"mod 2 is",x%2)

# Print the remainder of y divided by 2
print(y,"mod 2 is",y%2)

# Print the remainder of z divided by 2
print(z,"mod 2 is",round(z%2,1))