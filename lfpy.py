# -*- coding: utf-8 -*-
"""列出列表里所有字符串小写数据"""


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ch.lower() for ch in L1 if isinstance(ch, str)]


print(L2)
