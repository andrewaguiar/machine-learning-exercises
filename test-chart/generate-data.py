import os
import numpy as np
import random

print('generating data file')

types = {
  'racoon': { 'weight': np.arange(6.5, 10.5, 0.1), 'height': np.arange(23, 30, 0.1) },
  'pangolim': { 'weight': np.arange(5.8, 7.3, 0.1), 'height': np.arange(33, 35, 0.1) },
  'armadillo': { 'weight': np.arange(4.5, 6.5, 0.1), 'height': np.arange(15, 20, 0.1) }
}

sample_id = 0

lines = []

for animal in ['racoon', 'pangolim', 'armadillo']:
  for _i in range(1, 200):
    sample_id += 1

    datas = types[animal]
    random.shuffle(datas['weight'])
    random.shuffle(datas['height'])

    weight = datas['weight'][0]
    height = datas['height'][0]

    if bool(random.getrandbits(1)):
      weight += random.randint(-2, 2)
      height += random.randint(-2, 2)

    if bool(random.getrandbits(1)) and bool(random.getrandbits(1)):
      weight += random.randint(-2, 2)
      height += random.randint(-2, 2)

    if bool(random.getrandbits(1)) and bool(random.getrandbits(1)) and bool(random.getrandbits(1)):
      weight += random.randint(-2, 2)
      height += random.randint(-2, 2)

    lines.append('%s,%0.2f,%0.2f,%s\n' % (sample_id, weight, height, animal))

os.remove('data.txt')

data_file = open('data.txt', 'w')

random.shuffle(lines)

data_file.write("id,weight,height,animal\n")

for l in lines:
  data_file.write(l)

data_file.close()
