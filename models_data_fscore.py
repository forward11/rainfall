from matplotlib import rcParams
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

data = [20, 40, 60, 80, 100]
fscore_dl = [0.73, 0.79, 0.83, 0.84, 0.88]
fscore_svm = [0.80, 0.84, 0.85, 0.87, 0.88]
fscore_lgbm = [0.77, 0.84, 0.88, 0.90, 0.92]


rcParams['font.family'] = 'Times New Roman'
# rcParams['font.size'] = 24
rcParams['font.weight'] = 'bold'

axis_width = 1
major_tick_length = 6
minor_tick_length = 2.5
fig, ax = plt.subplots()
fig.set_figheight(3)
fig.set_figwidth(4)

ax.plot(data, fscore_lgbm, '*-', label='LightGBM')
ax.plot(data, fscore_svm, '.-', label='SVM')
ax.plot(data, fscore_dl, '^-', label='HYBRID')


# for x, y in zip(data, fscore):
#     label = '{}'.format(y)
#     ax.annotate(label, (x, y), textcoords='offset points', xytext=(0, 10), ha='center')
ax.set_xlabel('Data Size [%]', fontweight='bold')
ax.set_ylabel('F-Score', fontweight='bold')
x_major_locator = MultipleLocator(20)
x_minor_locator = MultipleLocator(4)
y_major_locator = MultipleLocator(0.05)
y_minor_locator = MultipleLocator(0.01)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
ax.xaxis.set_minor_locator(x_minor_locator)
ax.yaxis.set_minor_locator(y_minor_locator)
ax.tick_params(which='both', direction='in', width=axis_width)
ax.tick_params(which='major', length=major_tick_length)
ax.tick_params(which='minor', length=minor_tick_length)
ax.set_ylim([0.71, 0.95])
ax.set_xlim([10, 110])
ax.legend()
y_twin = ax.twinx()
x_twin = ax.twiny()
x_twin.set_xlim(ax.get_xlim())
y_twin.set_ylim(ax.get_ylim())
x_twin.xaxis.set_major_locator(x_major_locator)
y_twin.yaxis.set_major_locator(y_major_locator)
x_twin.xaxis.set_minor_locator(x_minor_locator)
y_twin.yaxis.set_minor_locator(y_minor_locator)
x_twin.tick_params(which='both', direction='in', width=axis_width)
y_twin.tick_params(which='both', direction='in', width=axis_width)
x_twin.tick_params(which='major', length=major_tick_length)
y_twin.tick_params(which='major', length=major_tick_length)
x_twin.tick_params(which='minor', length=minor_tick_length)
y_twin.tick_params(which='minor', length=minor_tick_length)
plt.setp(x_twin.get_xticklabels(), visible=False)
plt.setp(y_twin.get_yticklabels(), visible=False)
ax.spines['bottom'].set_linewidth(axis_width)
ax.spines['top'].set_linewidth(axis_width)
ax.spines['left'].set_linewidth(axis_width)
ax.spines['right'].set_linewidth(axis_width)
fig.tight_layout()
# plt.show()
plt.savefig('models_data_fscore.png', dpi=300)