from numpy import arange 
import matplotlib.pyplot as plt 
import math


fx="(((5*x)**2)-(math.e**x))"
rango = arange(-10,10)
valores = []

for x in rango:
    y = eval(fx)
    valores.append(y)
    print "x = %s y = %s" %(x, y)

plt.plot(rango,valores)
plt.grid(axis='both')
plt.show()
