def findSqareRoot(number):
    low = 0.0 
    high = number
    epsilon = 0.01
    guess = (low + high) / 2
    
    while abs(number - guess*2) >epsilon:
        print "high" +