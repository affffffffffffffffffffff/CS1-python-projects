while ( True ):
    # Get the numerator
    year = int(input("Enter a year :: "))
    # check to see if it is a leap year
    # a leap year is divisible by 4 and / or 400
    if(year % 4 == 0):
        # print not a leap year if it is NOT a leap year
        if((year % 100 == 0) & (year % 400 != 0)):
            print("not a leap year")
        # print leap year if it is a leap year
        else:
            print("leap year")
    # print not a leap year if it is NOT a leap year
    else:
        print("not a leap year")
