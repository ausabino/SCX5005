
# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import random

#Define function distribution: (p ** k) * ((1-p) ** (1-k))
def bernoulli( p ):
  y = []
  for i in range(10000):
    x = random.random()
    if x <= p:
      y.append(1)
    else:
      y.append(0)
  return y

exp = bernoulli(0.7)

#Create the plot
plt.hist( exp, bins=(1000), histtype = 'bar', edgecolor='r', label='p = 0.7')

# Add a title
plt.title('Distribuição de Bernoulli')

# Add X and y Label
plt.xlabel('Evento')
plt.ylabel('Frequência')

# Add a grid
plt.grid(alpha=.4,linestyle='-.')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
