# -*- coding: utf-8 -*-
"""This script parse the content of a xml file"""


def hannoi(nhan, xhan, yhan, zhan):
    """This script parse the content of a xml file"""
    if nhan == 1:
        print(xhan, '-->', zhan)
    else:
        hannoi(nhan - 1, xhan, zhan, yhan)
        hannoi(1, xhan, yhan, zhan)
        hannoi(nhan - 1, yhan, xhan, zhan)


print("汉诺塔示例开始：")
hannoi(5, 'A', 'B', 'C')
