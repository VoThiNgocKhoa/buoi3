# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:13:11 2024

@author: 84372
"""

chuoi = "i'm a cat"
chuoi_tua_de = chuoi[0].upper() + chuoi[1:4] + chuoi[4:].title()
print(chuoi_tua_de)
chuoi_in_hoa = chuoi.upper()
print(chuoi_in_hoa)
chuoi_ngau_nhien = chuoi[0] + chuoi[1:4].upper() + chuoi[4:7].lower() + chuoi[7:].upper() 
print(chuoi_ngau_nhien)
chuoi_hoa_thuong = chuoi.capitalize()
print(chuoi_hoa_thuong)
