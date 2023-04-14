import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np


hour = np.array([1, 20, 46, 70])
fiveSox = [251.108618489, 243.057680626, 187.078388148, 237.878140845]
fiveSoxError = [6.079456126, 7.674382259, 5.257587541, 1.548401467]

model = make_interp_spline(hour, fiveSox)
hours = np.linspace(1, 70, 2)
blys = model(hours)

fiveDox = [246.339376927, 236.927993561, 238.749631110, 237.159446061]
fiveDoxError =[2.368198335, 5.385950713, 9.199222866, 5.462420392]

quinSox =[247.572523348, 238.015655469, 235.821004546, 239.661915887]
quinSoxError =[2.701759706, 4.922359556, 6.922864437, 7.071136816]

quinDox =[247.741764393, 235.031165047, 234.702812368, 238.592872414]
quinDoxError =[0.991855231, 2.205657724, 10.651628047, 5.121445808]

quinSan = [145.759987235, 143.814778742, 141.482878348, 145.962210295]
quinSanError =[1.262498945, 1.646883350, 7.099764671, 2.102190009]

quinDan= [137.131508280, 135.153610226, 143.879375317, 138.028446010]
quinDanError = [5.174890076, 5.152534438, 5.506351519, 5.826181510]

plt.figure(figsize=(14, 10), dpi=300)
plt.plot(hours, fiveDox, 'brown', linewidth=3, label="lichen sample 510ml + N2O/CH4 gas")
plt.errorbar(hour, bl, yerr=blerror, capsize=3, capthick=3, fmt='brown', ecolor='brown')

plt.plot(hour, be, 'green', linewidth=3, label="lichen sample 510ml + local air")
plt.errorbar(hour, be, yerr=beerror, capsize=3, capthick=3, fmt='green', ecolor='green')

plt.plot(hour, sl, 'red', linewidth=3, label="lichen sample 135ml + N2O/CH4 gas")
plt.errorbar(hour, sl, yerr=slerror, capsize=3, capthick=3, fmt='red', ecolor='red')

plt.plot(hour, se, 'b', linewidth=3, label="lichen sample 135ml + local air")
plt.errorbar(hour, se, yerr=seerror, capsize=3, capthick=3, fmt='b', ecolor='b')

plt.plot(hour, cbl, 'magenta', linewidth=3, label="control sample 510ml + N2O/CH4 gas")
plt.errorbar(hour, cbl, yerr=cblerror, capsize=3, capthick=3, fmt='magenta', ecolor='magenta')

plt.plot(hour, cbe, 'aqua', linewidth=3, label="control sample 510ml + local air")
plt.errorbar(hour, cbe, yerr=cbeerror, capsize=3, capthick=3, fmt='aqua', ecolor='aqua')

plt.plot(hour, csl, 'black', linewidth=3, label="control sample 135ml + N2O/CH4 gas")
plt.errorbar(hour, csl, yerr=cslerror, capsize=3, capthick=3, fmt='black', ecolor='black')

plt.plot(hour, cse, 'orange', linewidth=3, label="control sample 135ml + local air")
plt.errorbar(hour, cse, yerr=cseerror, capsize=3, capthick=3, fmt='orange', ecolor='orange')
plt.xlim(0, 300)
plt.ylim(0, 100)
plt.title("Figure 18: N2O consumption", fontsize=20)
plt.xlabel("Incubation hours", fontsize=16)
plt.ylabel("ng N2O-C/g", fontsize=16)
plt.grid()
plt.legend(edgecolor="red", facecolor="whitesmoke", fontsize='16', loc="upper left", bbox_to_anchor=(-0.015, -0.07, 0, 0), ncol=2)
plt.tight_layout()

plt.show()