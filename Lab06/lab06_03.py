# CS344 Exercise 6.3
# @author: Won Seok Park
# Note: help received from Ian Park for keras installation

from keras.datasets import boston_housing

(train_examples, train_labels), (test_examples, test_labels) = boston_housing.load_data()

print("Number of training examples ", len(train_examples))
print("Number of testing examples ", len(test_examples))

print("\tRank: ", test_labels.ndim) # Rank: 1
print("\tShape: ", test_labels.shape) # Shape: (102,) - confirms rank above
print("\tType: ", test_labels.dtype) # Type: float64