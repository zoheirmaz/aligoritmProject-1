import time
from pprint import pprint

import globalVar


def mul(X, Y):
    result = [[0 for x in range(Y[0].__len__())] for y in range(X.__len__())]
    start_time = time.time()
    ln1 = len(X)
    ln2 = len(Y[0])
    ln3 = len(Y)
    for i in range(ln1):

        for j in range(ln2):

            for k in range(ln3):
                result[i][j] += X[i][k] * Y[k][j]

    index = str(X.__len__())
    globalVar.normMultTime[index] = time.time() - start_time
    globalVar.normMultTime[str(0)] = 0.0

    print("--- %s seconds ---" % globalVar.normMultTime)

    return result
