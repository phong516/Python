#Xay dung class
class SV:
    nganh_hoc='CDT'
    khoa_hoc='2020'
    def Add(self,MS,ten):
        self.id=MS
        self.name=ten
    def in_thong_tin(self):
        print("Ho ten: ",self.name)
        print("MSSV: ",self.id)
        print("Nganh hoc: ",self.nganh_hoc)
        print("Khoa hoc: ",self.khoa_hoc)
A=SV()
A.Add(20146516,'Nguyen Le Phong')
A.in_thong_tin()
print('-----------------------')
#VD init
class SV1:
    nganh_hoc='CDT'
    khoa_hoc='2020'
    def __init__(self,MS=0,ten=''):
        self.id=MS
        self.name=ten
    def in_thong_tin(self):
        print("Ho ten: ",self.name)
        print("MSSV: ",self.id)
        print("Nganh hoc: ",self.nganh_hoc)
        print("Khoa hoc: ",self.khoa_hoc)
B=SV1(20146516,'Nguyen Le Phong')
B.in_thong_tin()

#Ví dụ 3
class SV3:
    major='CĐT'
    year=2020
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def nhap_diem(self,midterm,final):
        self.midterm=midterm
        self.final=final
    @classmethod
    def change(cls,major1,year1):
        cls.major=major1
        cls.year=year1
SV3.change('Zalo',2022)
print(SV3.major)