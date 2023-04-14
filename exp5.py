import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

hour = np.array([1, 20, 46, 70])

fiveSox = [251.108618489, 243.057680626, 187.078388148, 237.878140845]
fiveSoxError = [6.079456126, 7.674382259, 5.257587541, 1.548401467]

model = make_interp_spline(hour, fiveSox)
hours = np.linspace(1, 80, 2)
blys = model(hours)

fiveDox = [246.339376927, 236.927993561, 238.749631110, 237.159446061]
fiveDoxError =[2.368198335, 5.385950713, 9.199222866, 5.462420392]

quinSox = [247.572523348, 238.015655469, 235.821004546, 239.661915887]
quinSoxError = [2.701759706, 4.922359556, 6.922864437, 7.071136816]

quinDox = [247.741764393, 235.031165047, 234.702812368, 238.592872414]
quinDoxError =[0.991855231, 2.205657724, 10.651628047, 5.121445808]

quinSan = [145.759987235, 143.814778742, 141.482878348, 145.962210295]
quinSanError =[1.262498945, 1.646883350, 7.099764671, 2.102190009]

quinDan= [137.131508280, 135.153610226, 143.879375317, 138.028446010]
quinDanError = [5.174890076, 5.152534438, 5.506351519, 5.826181510]


plt.figure(figsize=(18, 12), dpi=400)
plt.plot(hour, fiveSox, 'y', linewidth=3, label="P.glauca 5°C O2 + snow")
plt.errorbar(hour, fiveSox, yerr=fiveSoxError, capsize=5, capthick=5, fmt='y', ecolor='y')

plt.plot(hour, fiveDox, 'green', linewidth=3, label="P.glauca 5°C O2 dry")
plt.errorbar(hour, fiveDox, yerr=fiveDoxError, capsize=5, capthick=5, fmt='green', ecolor='green')

plt.plot(hour, quinSox, 'red', linewidth=3, label="P.glauca 15°C O2 + snow")
plt.errorbar(hour, quinSox, yerr=quinSoxError, capsize=5, capthick=5, fmt='red', ecolor='red')

plt.plot(hour, quinDox, 'black', linewidth=3, label="P.glauca 15°C O2 dry")
plt.errorbar(hour, quinDox, yerr=quinDoxError, capsize=5, capthick=5, fmt='black', ecolor='black')

plt.plot(hour, quinSan, 'orange', linewidth=3, label="P.glauca 15°C He + snow")
plt.errorbar(hour, quinSan, yerr=quinSanError, capsize=5, capthick=5, fmt='orange', ecolor='orange')

plt.plot(hour, quinDan, 'blue', linewidth=3, label="P.glauca 15°C He dry")
plt.errorbar(hour, quinDan, yerr=quinDanError, capsize=5, capthick=5, fmt='blue', ecolor='blue')

plt.xlim(0, 80)
plt.ylim(120, 270)

plt.xlabel("Incubation hours", fontsize=16)
plt.ylabel("ng N2O-C/g", fontsize=16)
plt.grid()
plt.legend(edgecolor="red", facecolor="whitesmoke", fontsize=21, loc="upper left", bbox_to_anchor=(-0.015, -0.07, 0, 0), ncol=3)
plt.tight_layout()

plt.show()