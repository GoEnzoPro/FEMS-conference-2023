import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

hour = np.array([1.5, 5.5, 26.86, 50.75, 75, 171.58, 337.4])

SP1 = [644.0791234, 626.0998085, 625.3552919, 624.6643653, 620.5422569, 621.3719481, 627.7696256]
SP1error = [14.45688491, 11.65747396, 19.36387365, 18.53173328, 16.41936253, 16.37681228, 15.09221202]

model = make_interp_spline(hour, SP1)
hours = np.linspace(1, 337.4, 2)
blys = model(hours)

SP2 = [639.7371858, 621.8107768, 620.3117982, 620.3471138, 620.3651605, 625.0470614, 625.2025014]
SP2error =[4.143687486, 3.098935187, 4.714693862, 5.103727339, 4.378172781, 2.068908225, 3.543733845]

SP3 =[639.5257981, 617.1336871, 620.2445783, 619.8341072, 617.8867037, 623.1966452, 624.6596739]
SP3error =[2.473163834, 5.727589236, 1.836942653, 3.100419941, 1.971430408, 2.042743238, 2.879786021]

SP4 =[639.7404646, 621.5388438, 620.6221545, 617.6901683, 616.933208, 622.9593414, 624.8450163]
SP4error =[1.505157622, 2.817548561, 3.111296785, 3.93474255, 3.13922064, 2.603780867, 3.955647188]



plt.figure(figsize=(14, 6), dpi=400)
plt.plot(hour, SP1, 'y', linewidth=3, label="Bryoria fuscescens")
plt.errorbar(hour, SP1, yerr=SP1error, capsize=5, capthick=5, fmt='y', ecolor='y')

plt.plot(hour, SP2, 'green', linewidth=3, label="Hypogymnia physodes")
plt.errorbar(hour, SP2, yerr=SP2error, capsize=5, capthick=5, fmt='green', ecolor='green')

plt.plot(hour, SP3, 'red', linewidth=3, label="Platismatia glauca")
plt.errorbar(hour, SP3, yerr=SP3error, capsize=5, capthick=5, fmt='red', ecolor='red')

plt.plot(hour, SP4, 'blue', linewidth=3, label="Pseudevernia furfuracea")
plt.errorbar(hour, SP4, yerr=SP4error, capsize=5, capthick=5, fmt='blue', ecolor='blue')


plt.xlim(0, 340)
plt.ylim(600, 660)
plt.title("Figure 16: N2O consumption dry samples", fontsize=18)
plt.xlabel("Incubation hours", fontsize=16)
plt.ylabel("ppb", fontsize=16)
plt.grid()
plt.legend(edgecolor="red", facecolor="whitesmoke", fontsize='12', loc="upper left", bbox_to_anchor=(-0.015, -0.07, 0, 0), ncol=2)
plt.tight_layout()

plt.show()