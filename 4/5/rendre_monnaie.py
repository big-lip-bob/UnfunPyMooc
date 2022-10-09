currency = [20, 10, 5, 2, 1]
def rendre_monnaie(money, x20, x10, x5, x2, x1): # *pennies): # triste de ne pas pouvoir *pennies
    pennies = [x20, x10, x5, x2, x1]
    change = sum(x * y for x, y in zip(currency, pennies)) - money
    if change < 0: return (None, None, None, None, None) # pourquoi pas un seul, bof
    charge = []
    for amount in currency:
        count = change // amount
        charge.append(count)
        change -= count * amount
        # assert 0 <= change

    return tuple(charge)