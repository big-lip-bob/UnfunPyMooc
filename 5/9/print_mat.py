def print_mat(m):
    if not m: return print()
    for r in m:
        for e in r:
            print(e, end = ' ')
        print()

ma_matrice = eval(input())
print_mat(ma_matrice)