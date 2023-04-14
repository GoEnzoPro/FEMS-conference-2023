import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

hour = np.array([1.5, 5.5, 26.86, 50.75, 75, 171.58, 337.4])

SP1 = [644.217388, 627.4819437, 626.4947274, 626.5262219, 623.2344247, 626.5110359, 630.8566168]
SP1error = [4.183507309, 3.273356389, 4.033755346, 4.367881569, 3.544066097, 5.100584027, 4.162017958]

model = make_interp_spline(hour, SP1)
hours = np.linspace(1, 337.4, 2)
blys = model(hours)

SP2 = [643.461759, 622.9250709, 626.4653316, 623.0081904, 624.7340734, 623.8860307, 629.3227582]
SP2error =[4.532240179, 5.255226982, 4.421527551, 3.730423482, 4.412896232, 2.742902632, 1.811222845]

SP3 =[642.4694209, 619.9407502, 624.9873944, 616.6096036, 623.4714901, 621.5602444, 622.5708824]
SP3error =[10.01233643, 10.09021913, 6.941896833, 8.590053142, 3.489523431, 7.878246162, 7.315612231]

SP4 =[640.6490299, 622.8907545, 621.4020407, 619.0126682, 619.0825045, 621.3101183, 625.952656]
SP4error =[5.934289679, 4.926828625, 6.03003547, 3.249372587, 3.275457657, 5.086086485, 3.135908812]



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
plt.title("Figure 17: N2O consumption wet samples", fontsize=18)
plt.xlabel("Incubation hours", fontsize=16)
plt.ylabel("ppb", fontsize=16)
plt.grid()
plt.legend(edgecolor="red", facecolor="whitesmoke", fontsize='12', loc="upper left", bbox_to_anchor=(-0.015, -0.07, 0, 0), ncol=2)
plt.tight_layout()

plt.show()