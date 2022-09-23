currency = [20, 10, 5, 2, 1]
def rendre_monnaie(money, *pennies):
    if len(pennies) != 5: raise ValueError
    change = sum(x * y for x, y in zip(currency, pennies)) - money
    if change < 0: return (None, None, None, None, None) # pourquoi pas un seul bof

    charge = []
    for amount in currency:
        count = change // amount
        charge.append(count)
        change -= count * amount

    return tuple(charge)