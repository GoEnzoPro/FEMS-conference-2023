import matplotlib.pyplot as plt
import numpy as np

y = ("lichen 510 ml N2O/CH4 gas", [-0.003066463095, 0.00190308, 0.001668123])

y2 = ("lichen 510 ml local air", [-0.004127, -0.00033859, -0.000296787])

y3 = ("control 510 ml N2O/CH4 gas", [0,000000, -0.002313985, -0.002028298])

y4 = ("control 510 ml local air", [0.000000, -0.002079346, -0.001822627])

X1 = np.random.normal(0, 1, 10000)
plt.boxplot(X1)
plt.show()