# -*- coding: utf-8 -*-
"""杨辉三角算法"""


def yanghui():
    """杨辉三角算法实现"""
    llist = [1]
    while True:
        yield llist
        llist = [1] + [llist[i - 1] + llist[i] for i in range(len(llist))if i > 0] + [1]


n = 0
for t in yanghui():
    print(t)
    n = n + 1
    if n == 10:
        break
