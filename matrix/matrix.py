import time

from globalVar import time_dict
from exceptions.Error import MatrixSummationException


class Matrix:
    matrix = None
    row = 0
    column = 0

    def __init__(self, matrix=None, row=None, column=None):
        if matrix is not None:
            self.matrix = matrix
            self.row = int(str(matrix.__len__()))
            self.column = int(str(matrix[0].__len__()))
        else:
            if (row is not None) and (column is not None):
                if row == 1:
                    self.matrix = [0 for x in range(column)]
                else:
                    self.row = row
                    self.column = column
                    self.matrix = [[0 for x in range(column)] for y in range(row)]

    def __add__(self, otherMatrix):
        finalMatrix = New2DList(self.row, self.column)

        try:
            if (self.row != otherMatrix.row) or (self.column != otherMatrix.column):
                raise MatrixSummationException
            else:
                for x in range(self.row):
                    for y in range(self.column):
                        # print(str(x) + str(y))
                        finalMatrix[x][y] = self.matrix[x][y] + otherMatrix.matrix[x][y]
        except MatrixSummationException as e:
            print(e.message)

        return Matrix(finalMatrix)

    def __sub__(self, otherMatrix):
        finalMatrix = New2DList(self.row, self.column)

        try:
            if (self.row != otherMatrix.row) or (self.column != otherMatrix.column):
                raise MatrixSummationException
            else:
                for x in range(self.row):
                    for y in range(self.column):
                        # print(str(x) + str(y))
                        finalMatrix[x][y] = self.matrix[x][y] - otherMatrix.matrix[x][y]
        except MatrixSummationException as e:
            print(e.message)

        return Matrix(finalMatrix)

    # --------------------------------------------------------    

    def __mul__(self, other):

        if self.row <= 1024:

            result = [[0 for x in range(other.matrix[0].__len__())] for y in range(self.matrix.__len__())]
            start_time = time.time()
            for i in range(len(self.matrix)):

                for j in range(len(other.matrix[0])):

                    for k in range(len(other.matrix)):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]

            time_dict[str(self.row)] = (time.time() - start_time)

            # print("--- %s seconds ---" % time_dict)

            # if 3 in self.matrix[0]:
            #     print(True)

            finalMatrix = Matrix(result)

        else:
            index=str(self.row)

            self = devide(self)
            other = devide(other)

            M = Matrix(row=1, column=8)

            finalMatrix = Matrix(row=self.row, column=self.column)

            start_time = time.time()

            M.matrix[1] = (self.matrix[0][0] + self.matrix[1][1]) * (other.matrix[0][0] + other.matrix[1][1])
            M.matrix[2] = (self.matrix[1][0] + self.matrix[1][1]) * other.matrix[0][0]
            M.matrix[3] = self.matrix[0][0] * (other.matrix[0][1] - other.matrix[1][1])
            M.matrix[4] = self.matrix[1][1] * (other.matrix[1][0] - other.matrix[0][0])
            M.matrix[5] = (self.matrix[0][0] + self.matrix[0][1]) * other.matrix[1][1]
            M.matrix[6] = (self.matrix[1][0] - self.matrix[0][0]) * (other.matrix[0][0] + other.matrix[0][1])
            M.matrix[7] = (self.matrix[0][1] - self.matrix[1][1]) * (other.matrix[1][0] + other.matrix[1][1])

            finalMatrix.matrix[0][0] = M.matrix[1] + M.matrix[4] - M.matrix[5] + M.matrix[7]
            finalMatrix.matrix[0][1] = M.matrix[3] + M.matrix[5]
            finalMatrix.matrix[1][0] = M.matrix[2] + M.matrix[4]
            finalMatrix.matrix[1][1] = M.matrix[1] + M.matrix[3] - M.matrix[2] + M.matrix[6]

            time_dict[index] = (time.time() - start_time)

            # print("--- %s seconds ---" % time_dict[str(self.row)])

            finalMatrix = mergeMatrix(finalMatrix)

        return finalMatrix


# -------------------------------------------------------------------------------

def mergeMatrix(matrix):
    row = matrix.matrix[0][0].row
    column = matrix.matrix[0][0].column

    finalMatrix = Matrix(row=row * 2, column=column * 2)

    for x in range(2):
        for y in range(2):

            for p in range(row):
                for q in range(column):
                    finalMatrix.matrix[(row * x) + p][(column * y) + q] = (matrix.matrix[x][y]).matrix[p][q]

    return finalMatrix


def devide(matrix):
    finalMatrix = New2DList(2, 2)

    for ro in range(2):
        for col in range(2):

            row = matrix.row

            temp = New2DList(row // 2, row // 2)

            if (ro == 0) and (col == 0):

                p = 0
                for x in range(row // 2):
                    q = 0
                    for y in range(row // 2):
                        temp[p][q] = matrix.matrix[x][y]
                        q += 1
                    p += 1

            elif (ro == 0) and (col == 1):

                p = 0
                for x in range(row // 2):
                    q = 0
                    for y in range(row // 2, row):
                        temp[p][q] = matrix.matrix[x][y]
                        q += 1
                    p += 1

            elif (ro == 1) and (col == 0):

                p = 0
                for x in range(row // 2, row):
                    q = 0
                    for y in range(row // 2):
                        temp[p][q] = matrix.matrix[x][y]
                        q += 1
                    p += 1

            elif (ro == 1) and (col == 1):

                p = 0
                for x in range(row // 2, row):
                    q = 0
                    for y in range(row // 2, row):
                        temp[p][q] = matrix.matrix[x][y]
                        q += 1
                    p += 1

            finalMatrix[ro][col] = Matrix(temp)

    return Matrix(finalMatrix)


def New2DList(row, column):
    return [[0 for x in range(column)] for y in range(row)]
