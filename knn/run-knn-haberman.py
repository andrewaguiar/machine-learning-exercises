# Performing KNN algorithm using Haberman dataset
#
# http://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival

from knn import KNN

if __name__ == "__main__":
  haberman_dataset_file = open('haberman.data', 'r')

  data = []

  for line in haberman_dataset_file.readlines():
    attributes = line.replace('\n', '').split(',')
    data.append([int(attributes[0]),
                 int(attributes[1]),
                 int(attributes[2]),
                 int(attributes[3])])

  knn = KNN(data, 250)

  print(knn.info())

  print(knn.perform_all_testing_data(5))
