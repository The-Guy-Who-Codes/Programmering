import pylab as py
import numpy as np
from matplotlib import pyplot as plt

dato = 25
måned = 11
gutt = True

dx = 1E-4
xmin = -10
xmax = 10
antall_punkter = 100

# definer koeffisientene

a = 1
b = dato // 10 + dato % 10
c = måned // 10 + måned % 10
d = b + c

x_val = py.linspace(xmin, xmax, antall_punkter)

if gutt:
    b = -b
    d = -d
else:
    a = -a
    c = -c
    
# definisjon av funksjonnene

f = lambda x: a*x**3 + b*x**2 + c*x + d


df = lambda x: 3*a*x**2 + 2*b*x + c


fwd = lambda x: (f(x + dx) - f(x)) / dx

sym = lambda x: (f(x + dx) - f(x - dx)) / (2 * dx)

# mulig verdier av h
h = [10, 10**-1, 10**-4, 10**-7, 10**-15, 10**-19]

# gj. snitt feil på vær metode for vær h
err_fwd = []
err_sym = []

for z in h:
    
    dx = z
    
    # lage y verdiene
    df_Y_Val = df(x_val)
    
    fwd_Y_Val = fwd(x_val)
    
    sym_Y_Val = sym(x_val)
    
    # plotte grafene
    plt.title("h = " + str(z))
    plt.plot(x_val, df_Y_Val, label='df')
    plt.plot(x_val, fwd_Y_Val, label='fwd')
    plt.plot(x_val, sym_Y_Val, label='sym')
    plt.legend()
    plt.show()
    
    # finn gj. snitt forsjell mellom kvotient og analytisk metoden
    diff_Sym = []
    diff_Fwd = []
    
    for i in df_Y_Val:
        diff_Sym.append(abs(i - sym_Y_Val[np.where(df_Y_Val == i)]))
        diff_Fwd.append(abs(i - fwd_Y_Val[np.where(df_Y_Val == i)]))
        
    err_fwd.append(np.average(diff_Fwd))
    err_sym.append(np.average(diff_Sym))

# print h verdien med best tilnærming til analytiske metoden    

t = np.where(err_fwd == np.amin(err_fwd))
print("Beste verdi av h i frammover kvotient: \n\t", h[t[0][0]])
t = np.where(err_sym == np.amin(err_sym))
print("Beste verdi av h i symetriske kvotient: \n\t", h[t[0][0]])
