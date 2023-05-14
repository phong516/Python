"""
Nhập chiều cao cm và cân nặng kg (kiểu float)
Xuất BMI, thông tin đánh giá
"""
from math import *
def isfloat(n: str):
     try:
         float(n)
         return True
     except ValueError:
         return False
cm=input("Nhập chiều cao (cm): ")
while isfloat(cm)==False or ("-" in cm):
    cm=input("Nhập sai chiều cao!!! Mời nhập lại: ")

kg=input("Nhập cân nặng (kg): ")
while isfloat(kg)==False or ("-" in kg):
    cm=input("Nhập sai cân nặng!!! Mời nhập lại: ")

cm=float(cm)
kg=float(kg)

bmi=kg/(cm/100)**2

print("Chỉ số BMI của bạn là:",round(bmi,1),end=" ")
if bmi<18.5:
    print("-->Gầy")
elif bmi>=18.5 and bmi<25:
    print("-->Bình thường")
elif bmi>=25 and bmi<30:
    print("-->Thừa cân")
else: print("-->Béo phì")