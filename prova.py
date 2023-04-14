import numpy as np
import pandas as pd
m = np.array([[1, 2, 3], [4, 5, 6], [9, 6, 3]])

pd.pivot_table(m, index = 'casa')
