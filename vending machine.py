def drinklist(choice,money):
    Drinks = ["coke","sprite","water", "mountain-dew","DR.Pepper"]
    if money == 1.50:
        if choice in Drinks:
            return choice
    
    if money > 1.50:
        return (choice, money - 1.50)
    if money < 1.50:
        return "Not enough money"    
    