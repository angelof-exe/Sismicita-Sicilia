from module.most_dangerous1e2 import province, number
from module.font import font_title, font_labels, font_ticks
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(12, 9), dpi= 70)

plt.bar(province, number)


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.2, y[i], ha='center', fontdict=font_ticks)


addlabels(province, number)
plt.xlabel('Province', fontdict=font_labels, labelpad=20)
plt.ylabel('Number of municipalities', fontdict=font_labels, labelpad=20)
plt.xticks(size=20)
plt.yticks(size=15)
plt.tick_params(axis='x', pad=10)
plt.title('Number of municipalities present in\n every province with Level 1 & 2 of seismicity', pad=20,
          fontdict=font_title)

plt.show()
