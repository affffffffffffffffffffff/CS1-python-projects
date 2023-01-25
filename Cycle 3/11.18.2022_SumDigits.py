### Loop forever. Be mindful of indentation.
# Use a while loop construct. Everything else is inside this loop!
while True:
    # enter an integer
    num = int(input("Enter an integer :: "))            # see the sample output
    sum = 0
    #add another while loop
    while num != 0:
        #sum digit
        sum += num % 10
        #chop off right most digit of num
        num = (num-(num % 10))/10
    print(int(sum))