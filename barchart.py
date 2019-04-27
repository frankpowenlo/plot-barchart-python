import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 8

means_women = (90.74,93.31,83.59,87.12,77.83,82.59,72.36,75.66)
std_men = (5.18,3.98,2.74,5.99,4.60,2.84,5.86,3.00,12.67,7.60)

means_men = (94.25,95.61,96.49,96.14,91.18,95.27,94.91,93.32)
std_women = (5.08,4.10,2.91,2.80,4.26,3.25,2.85,4.66,12.78,8.52)


fig, ax = plt.subplots(figsize=(20,10))
index = np.arange(n_groups)
bar_width = 0.3
opacity = 0.7

error_config = {'ecolor': '0.3'}



rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='xkcd:red',
                label='A',capsize=3)

rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='xkcd:blue',
                label='B',capsize=3)


ax.set_ylabel('Caption ($\%$)',fontsize=20)
ax.set_ylim((0, 100))
ax.tick_params(labelsize=20)
ax.grid(linestyle="--", linewidth=0.8, color='.25', zorder=-10,)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9','10'),fontsize=20, rotation=0)
ax.legend(bbox_to_anchor=(1.01, 1.2),fontsize=21)

fig.tight_layout()
plt.show()

