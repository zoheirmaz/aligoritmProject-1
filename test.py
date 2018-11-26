from pprint import pprint

import matplotlib.pyplot as plt


def f(t):
    return 2 * t


def Plot(stra, norm):
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    # plt.ylabel('some numbers')
    # plt.show()

    listK1, listI1, listK2, listI2 = [], [], [], []

    list1 = list(stra.items())
    list2 = list(norm.items())

    pprint(list1)
    pprint(list2)

    while list1.__len__() != 0:
        a = list1.pop()
        listK1.append(a[0])
        listI1.append(a[1])

    while list2.__len__() != 0:
        a = list2.pop()
        listK2.append(a[0])
        listI2.append(a[1])

    # pprint(lists)
    # pprint(lists2)

    # x, y = zip(*lists)  # unpack a list of pairs into two tuples
    # s, p = zip(*lists2)

    # n = [0, 1]
    # m = [0, 1]
    # v = [0, 1]
    # w = [0, 2]

    # plt.subplot(2, 1, 1)
    # lines = plt.plot(x, y, s, p, 'o-')
    # lines = plt.plot(n, m, v, w, 'o-')


    # plt.setp(lines[0], linewidth=4)
    # plt.setp(lines[1], linewidth=2)

    # plt.subplot(2, 1, 1)
    # plt.plot(s, p, '.-')
    listK1.reverse()
    listI1.reverse()
    # listK2.reverse()
    # listI2.reverse()

    listK1 = [int(i) for i in listK1]
    listK2 = [int(i) for i in listK2]

    lines = plt.plot(listK1, listI1, 'o-', listK2, listI2)

    plt.setp(lines[0], linewidth=2)
    plt.setp(lines[1], linewidth=2, linestyle='--')

    plt.title('Strasen Mult VS Regular Mult')
    plt.ylabel('Execution Time')

    plt.legend(('Strasen Mult', 'Regular Mult'),
               loc='upper left')

    plt.grid(True)

    plt.show()
    print(stra)
