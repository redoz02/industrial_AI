# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:46:05 2022

@author: Hangyeol Kim
"""
# coding: utf-8
from and_gate import AND
from or_gate import OR
from xor_gate import XOR


def full_adder(a, b, c):
    p1 = XOR(a, b)
    p2 = AND(a, b)
    p3 = AND(p1, c)
    s = XOR(p1, c)
    c_out = OR(p3, p2)
    return c_out, s

#----print truth table
import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]), columns = ['a', 'b', 'c'])
df = pd.concat([df, pd.DataFrame(np.array([full_adder(row.a, row.b, row.c) for row in df.itertuples()]), columns=['c_out', 'sum'])], axis=1)

print(df)