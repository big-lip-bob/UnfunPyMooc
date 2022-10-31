from math import pi

eps, nmax = 1.0e-5, 50

def approx_arccos(x):
    term = 1
    acc = pi/2 - x
    for j in range(1, nmax-1):
        term *= (2*j-1) / (2*j)
        if abs(cn := term * (x ** (2*j+1)) / (2*j+1)) < eps: break
        acc += cn
    return acc
