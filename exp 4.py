import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

hour = np.array([3, 24, 65, 87, 110, 140, 154])

snow = [2.474, 2.040, 2.058, 2.154, 2.503, 2.906, 3.100]

model = make_interp_spline(hour, snow)
hours = np.linspace(1, 154, 2)
blys = model(hours)

milliq = [2.058, 2.154, 1.404, 2.256, 1.616, 1.663, 1.348]

dry =[1.404, 2.256, 2.040, 2.097, 2.225, 2.950, 2.371]

plt.figure(figsize=(14, 6), dpi=400)
plt.plot(hour, snow, 'red', linewidth=3, label=" P. glauca Snow sample")

plt.plot(hour, milliq, 'orange', linewidth=3, label="P. glauca MilliQ sample")

plt.plot(hour, dry, 'green', linewidth=3, label="P. glauca Dry sample")


plt.xlim(0, 160)
plt.ylim(1.000, 3.500)
plt.title("Figure 22: Variation of N2O samples  in anoxic condition", fontsize=18)
plt.xlabel("Incubation hours", fontsize=16)
plt.ylabel("ng N2O-C/g", fontsize=16)
plt.grid()
plt.legend(edgecolor="red", facecolor="whitesmoke", fontsize='12', loc="upper left", bbox_to_anchor=(-0.015, -0.07, 0, 0), ncol=2)
plt.tight_layout()

plt.show()