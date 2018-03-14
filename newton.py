from numpy import *
import matplotlib.pyplot as plt


def f(x):
    y = x**2 - 25
    return y


def newton(a,b,e):
    n = 1
    y = []
    x1 = random.random()
    x2 = random.random()
    x1 = -5*x1 + 5
    x2 = -5*x2 + 5
    y.append(x1)
    y.append(x2)
    while(abs(f(y[n]))>= e):
        pochodna = ((f(y[n]) - f(y[n - 1])) / (y[n] - y[n - 1]))
        y.append(y[n] - f(y[n])/pochodna)
        n+=1
    x = arange(x1 - 2, y[-1] + 2, e)
    print(y)
    plt.plot(x, f(x), y[-1], 0, 'o')
    plt.plot(x1,f(x1), 'ro')
    plt.show()
a = -6
b = 6
e = 0.0001
newton(a,b,e)

