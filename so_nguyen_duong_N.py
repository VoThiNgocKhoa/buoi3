# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:47:18 2024

@author: 84372
"""

N=int(input("nhap vao so nguyen duong co 2 chu so="))
if 9<N<100:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong_cac_so_N = hang_chuc + hang_don_vi
    print(f"tong cac chu so cua N la:{ tong_cac_so_N}") 
else:
    print("phep tinh khong hop le")
