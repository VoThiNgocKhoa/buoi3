# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:40:31 2024

@author: 84372
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM "
cach1 = chuoi.split(", ")
print(cach1)
print("tách thành các chuỗi sub-string (yêu cầu 1):")
for i in cach1:
    print(i)
cach2 = chuoi.replace("P. ","").replace("Q. ","").replace("Tp. ","").split(", ")
print(cach2)
print("tách thành các chuỗi sub-string (yeu cau 2):")
for j in cach2:
    print(j)
    