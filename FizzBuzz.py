def FizzBuzz():
    '''FizzBuzz is if 3 is divisibal by 3 it turns in Fizz and if it is divisibal by 5 it turn in to Buzz and if it is divisibal by 3 and 5 it turns in to FizzBuzz'''
    for numbers in range(1, 101):
        if numbers %15==0:
            print "FizzBuzz"
        elif numbers %3==0:
            print "Fizz"
        elif numbers %5==0:
            print "Buzz"
        else:
            print numbers        