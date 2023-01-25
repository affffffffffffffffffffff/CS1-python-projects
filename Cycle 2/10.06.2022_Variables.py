# Get the user's name
name = input("What is your name? ")

# Get the user's age
age = input("How old are you? ")

# Get the current year
year = input("What year was your last birthday? ")


# Print the user's name and age
print("Your name is",name,"and you are",age,"years old")

# Print the year the user was born
age = int(age)
year = int(year)
print("You were born in",(year - age))
