def iterSqRt(number):
    for counter in range(1, number):
        if counter**2 == number:
            return"sqare root of " + str(number) + "is" + str(counter)
    return " FAILED sqare root" + str(number) + "isnt" + str(counter)