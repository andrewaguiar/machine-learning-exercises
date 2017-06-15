from collections import OrderedDict
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

data = np.genfromtxt('data.txt', delimiter=',', dtype=None, skiprows=1)

colors = { 'armadillo': 'red', 'pangolim': 'blue', 'racoon': 'green' }

for animal_data in data:
  plt.scatter(animal_data[1], animal_data[2], color=colors[animal_data[3]], label=animal_data[3])

handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.xlabel('weight')
plt.ylabel('height')

plt.show()
