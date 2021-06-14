import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from set_plt import config_lps

wind = pd.read_excel('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\lps\\WG006_8_30.xlsx', index_col=0)

ax = WindroseAxes.from_ax()
wd = wind['WD'].values.tolist()
wv = wind['WV'].values.tolist()
ax.bar(wd, wv, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.savefig('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\lps\\wind\\8-30.png',dpi=300)
plt.close()
