from collections import OrderedDict
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random

haberman_dataset_file = open('haberman.data', 'r')

data = []

colors = { 1: 'green', 2: 'red' }
label_names = { 1: 'survived', 2: 'died' }

for line in haberman_dataset_file.readlines():
  attributes = line.replace('\n', '').split(',')
  data.append([int(attributes[0]),
                int(attributes[1]),
                int(attributes[2]),
                int(attributes[3])])

fig = pylab.figure()
ax = Axes3D(fig)

for sample in data:
  ax.scatter(sample[0], sample[1] + 1900, sample[2], color=colors[sample[3]], label=label_names[sample[3]])

pyplot.show()
