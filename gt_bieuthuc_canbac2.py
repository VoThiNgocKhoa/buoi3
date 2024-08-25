# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:19:42 2024

@author: 84372
"""

a = float(input("nhap vao so thuc a = "))
b = float(input("nhap vao so thuc b = "))
import math
tu_so1 = math.sqrt(a) - math.sqrt(b)
mau_so1 = math.pow(a, 0.25) - math.pow(b, 0.25)
phan_so1 = tu_so1 / mau_so1
tu_so2 = math.sqrt(a) + math.pow(a*b, 0.25)
mau_so2 = math.pow(a, 0.25) + math.pow(b, 0.25)
phan_so2 = tu_so2 / mau_so2
ket_qua = phan_so1 - phan_so2
print("gia tri cua bieu thuc la:", ket_qua)