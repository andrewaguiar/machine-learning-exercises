import math
from collections import Counter

class KNN:
  """
  Implementing Knn using plain python code

  https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
  """

  def __init__(self, data, training_data_size):
    self.data = data
    self.training_data = self.data[:training_data_size]
    self.testing_data = self.data[training_data_size:]

  def info(self):
    return "data: %d rows, %d training, %d testing" % (len(self.data), len(self.training_data), len(self.testing_data))

  def perform(self, tested_sample, k):
    distance_dict = {}

    # Perform euclidian distance against each training sample
    for index in range(len(self.training_data)):
      distance = self.__euclidian_distance(self.training_data[index], tested_sample)
      distance_dict[index] = distance

    k_nearest = sorted(distance_dict, key=distance_dict.get)[:k]

    results = map(lambda index : self.training_data[index][-1], k_nearest)

    result, _counting = Counter(results).most_common(1)[0]

    return result

  def perform_all_testing_data(self, k):
    results = { 'ok': 0, 'fail': 0 }

    for sample in self.testing_data:
      result = self.perform(sample, k)

      if result == sample[-1]:
        results['ok'] += 1
      else:
        results['fail'] += 1

    return results

  def __euclidian_distance(self, sample_1, sample_2):
    """
    Euclidian distance is the Square Root of Sum of all distances powered by 2

    Example:
      Given 2 coordinates x,y,z: c1 (4,7,3) and (3,9,7) the euclidian distance will be

      result = Sqrt(((4 - 3) ** 2) + ((7 - 9) ** 2) + ((3 - 7) ** 2))
      result = Sqrt((1 ** 2) + (-2 ** 2) + (-4 ** 2))
      result = Sqrt((1) + (4) + (16))
      result = Sqrt(21)
      result = 4.58257569495584
    """

    total_sum = 0
    samples_len = len(sample_1)

    for index in range(samples_len - 1):
      total_sum += math.pow(sample_1[index] - sample_2[index], 2)

    return math.sqrt(total_sum)
