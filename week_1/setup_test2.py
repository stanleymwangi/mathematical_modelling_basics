"""
Python program to test whether numpy and matplotlib have been installed correctly.
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

a = -1
b = 1
N = 101
x = np.linspace(a,b,N)
y = x**2
print(x[range(0,N,10)])
# If there is a problem: use print(x[list(range(0,N,10))]) instead.
print("\n\nDo see a list of values? \
Numpy has been installed correctly!")


input("\n\nPress ENTER to continue...")
# In Python 2.7, use raw_input("\n\nPress ENTER to continue...")

print("\n\nDo you see the graph of two functions?\n")
# Don't you see it? Sometimes (when you are not using Spyder),
# the graph is hidden behind a document or minimized.
# In the last case you need to have a look at your taskbar.
# Close the plot, when you want to continue.

plt.figure(1)
plt.plot(x,y,color = "violet", label = "$f(x)=x^2$")
plt.plot(x,-y,color = "red", label = "$g(x)=-x^2$")
plt.xlim([-1,1])
plt.axis("equal")
plt.xlabel("$x$-values")
plt.ylabel("$y$-values")
plt.title("Plot of two graphs")
plt.legend(loc = "upper right", shadow = True)
plt.show()
print("\n\nMatplotlib has been installed correctly!")