import time

import globalVar


def mul(X, Y):
    result = [[0 for x in range(Y[0].__len__())] for y in range(X.__len__())]
    start_time = time.time()
    for i in range(len(X)):

        for j in range(len(Y[0])):

            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    index = str(X.__len__())
    globalVar.normMultTime[index] = time.time() - start_time
    globalVar.normMultTime[str(0)] = 0.0

    print("--- %s seconds ---" % globalVar.normMultTime)

    return result
