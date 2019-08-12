
# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import random

#Define function distribution
def binomial( n, p ):
  y = []
  for i in range(10000):
    cont = 0
    for j in range(n):
      x = random.random()
      if x <= p:
        cont += 1
    y.append(cont)
  return y

exp = binomial( 10, 0.7)

#Create the plot
plt.hist( exp, bins=(1000), histtype = 'bar', edgecolor='r')

# Add a title
plt.title('Distribuição Binomial ~Bi( 10, 0.7)')

# Add X and y Label
plt.xlabel('Evento')
plt.ylabel('Frequência')

# Add a grid
plt.grid(alpha=.4,linestyle='-.')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
