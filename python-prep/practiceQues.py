# Write a Python function that takes two three-dimensional numeric data sets and adds them componentwise. 
# def add_3d_datasets(data1, data2):
#     result = []
#     for i in range(len(data1)):
#         layer = []
#         for j in range(len(data1[i])):
#             row = []
#             for k in range(len(data1[i][j])):
#                 row.append(data1[i][j][k] + data2[i][j][k])
#             layer.append(row)
#         result.append(layer)
#     return result



# Write a Python program for a matrix class that can add and multiply two dimensional arrays of numbers, assuming the dimensions agree appropriately for the operation.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return result

    def multiply(self, other):
        result = [[0] * len(other.matrix[0]) for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result
