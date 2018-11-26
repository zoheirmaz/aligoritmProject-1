import random
from pprint import pprint

from exceptions.Error import MatrixMultipltionException
from globalVar import time_dict, normMultTime
from matrix.matrix import Matrix
from test import Plot
from usualMultiple import multiple as ml


# start_time = time.time()



def New2DList(row, column):
    return [[0 for x in range(column)] for y in range(row)]


def CheckPoweredBy2(num):
    ch = True
    while ch is True and num >= 2:
        if num % 2 == 0:
            num /= 2
        else:
            ch = False
    return ch


def FixMatrix(matrix1, matrix2):
    tmp = [matrix1.row, matrix1.column, matrix2.row, matrix2.column]

    print(max(tmp))

    tmp = max(tmp)

    while not CheckPoweredBy2(tmp):
        tmp += 1

    matrix1.row, matrix1.column, matrix2.column, matrix2.row = tmp, tmp, tmp, tmp

    count = tmp - matrix1.matrix[0].__len__()
    for i in range(count):
        for x in range(matrix1.matrix.__len__()):
            matrix1.matrix[x].append(0)
            # pprint(matrix1.matrix)

    count = tmp - matrix2.matrix[0].__len__()
    for i in range(count):
        for x in range(matrix2.matrix.__len__()):
            matrix2.matrix[x].append(0)
            # pprint(matrix2.matrix)

    count = tmp - matrix1.matrix.__len__()
    for i in range(count):
        matrix1.matrix.append([0 for x in range(tmp)])
    # pprint(matrix1.matrix)

    count = tmp - matrix2.matrix.__len__()
    for i in range(count):
        matrix2.matrix.append([0 for x in range(tmp)])
    # pprint(matrix1.matrix)

    return [matrix1, matrix2]


# ------------------ main --------------------


cont = True
while cont:
    row1 = int(input('Enter row number of 1st matrix: '))
    col1 = int(input('Enter column number of 1st matrix: '))
    row2 = int(input('Enter row number of 2nd matrix: '))
    col2 = int(input('Enter column number of 2nd matrix: '))
    try:
        if col1 != row2:
            raise MatrixMultipltionException
        else:
            cont = False
    except MatrixMultipltionException as e:
        print(e.message)
        cont = True

a = [[random.randint(0, 10) for x in range(col1)] for y in range(row1)]
b = [[random.randint(0, 10) for x in range(col2)] for y in range(row2)]

a = Matrix(a)
b = Matrix(b)

pprint(ml.mul(a.matrix, b.matrix))

ls = FixMatrix(a, b)
a = ls[0]
b = ls[1]

pprint((a * b).matrix)
print()
pprint(time_dict)

# print("--- %s seconds ---" % (time.time() - start_time))
Plot(time_dict, normMultTime)
