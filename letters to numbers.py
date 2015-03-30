def namegame():
    '''The namegame changes the letters in the name to numbers then divids them by how meny letters are in the name'''
    name = raw_input('Write Text: ')
    name = name.lower()
    output =[]
    for character in name:
        number = ord(character) - 96
        output.append(number)
    answer = (sum(output)/ float(len(output)))
    print answer  