import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

fig, ax = plt.subplots()
plt.style.use("ggplot")
indexs = np.arange(4)
fig = plt.figure(figsize=(8,6))
width = 0.3

x = ["In Situ", "+5°C, oxic*", "+15°C, oxic", "+15°C, anoxic"]

y1 = [404000, 435000000, 4190000, 6280000]
y1error = [330000, 115000000, 2210000, 2780000]

y2 = [3020000, 860000000000, 5800000, 10500000]
y2error = [822000, 702000000000, 2670000, 5670000]

#plt.show()

colors = plt.cm.BuPu(np.linspace(0, 0.5, len(x)))
data = [y1, y2]
#print(data)
plt.bar(indexs, y1, label='DNA', width=width, color='orange')
plt.errorbar(indexs, y1, yerr=y1error, capsize=2, capthick=2, fmt='none', ecolor='black')

plt.bar(indexs+width, y2, label='cDNA', width=width, color='blue')
plt.errorbar(indexs+width, y2, yerr=y2error, capsize=2, capthick=2, fmt='none', ecolor='black')
plt.table(cellText=data,
          rowLabels=['DNA', 'cDNA'],
          rowColours=['orange', 'blue'],
          colLabels=x,
          loc='bottom',
          bbox=[0, -0.45, 1, 0.3])

fig.subplots_adjust(bottom=0.3)
plt.semilogy(10)
plt.title('Figure 3')
plt.xlabel('Conditions')
plt.ylabel('NosZ copies per g (WW lichen)')
plt.legend()
plt.xticks(indexs+width/2, x)
plt.show()
