def est_adn(str):
    if str == '': return False
    for c in str:
        if not ['A', 'T', 'C', 'G'].__contains__(c):
            return False
    return True