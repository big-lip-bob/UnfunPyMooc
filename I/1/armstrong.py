def est_armstrong(n):
    sta, acc = "", 0
    stn = str(n)
    stl = len(stn)
    for c in stn: # J'aurais préféré utiliser n%10 et n/=10 mais bon...
       sta += f"+{c}^{stl}"
       acc += int(c) ** stl
    return f"{n} {'=' if acc == n else '!='} {sta[1:]}"