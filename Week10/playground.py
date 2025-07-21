import numpy as np

array = np.array([[1, 2],
                  [4, 5],
                  [7, 8]])
# 2 columns, 3 rows each, so we will have 2 stds
result = array.std(axis=0) # 3 stds, but they are in the shape of 2 rows and 1 col
# print("result", result)
result = array.std(axis=0).reshape(1, -1) # the question tells us to have an array of 1 by 2 instead
# print(result)
print(array.reshape(6,1))