import numpy as np


def f(x, s):
    return x-s

def y(x):
    a, b = 0, 1
    n = 1000
    h = (b-a)/n


    w = np.zeros(n+1)
    for i in range(n+1):
        if i == 0 or i == n:
            w[i] = 1
        elif i % 2 == 1:
            w[i] = 4
        else:
            w[i] = 2


    I = 0
    for i in range(n+1):
        s = a + i*h
        I += w[i]*f(x, s)
    I *= h/3

    return 3 - 2*x + I


x = np.linspace(0, 1, 101)
for xi in x:
    print(f"y({xi:.2f}) = {y(xi):.6f}")