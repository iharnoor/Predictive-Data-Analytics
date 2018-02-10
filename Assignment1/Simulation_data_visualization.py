import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# with i.i.d. random variables N(137; 100) (simulating weight).
# Mean =137, Standard Deviation=100

matrix = [[0 for x in range(100)] for y in range(4)]

std1 = 25
std2 = 100
mean1 = 165
mean2 = 137
heights = std1 * np.random.randn(1, 100) + mean1
weights = std2 * np.random.randn(1, 100) + mean2

# 2.5 * np.random.randn(2, 4) + 3
matrix[0] = weights
matrix[1] = heights
# print(matrix)

# for row in range(len(matrix)):
#     for column in range(len(matrix[row])):
#         print(matrix[row][column], end="")
#     print()

# plt.scatter(heights, weights, color='red')
# # plt.plot(X, , color='blue')
# plt.title('Truth or Bluff (SVR)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

# plt.hist(matrix, bins=100, normed=True)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
