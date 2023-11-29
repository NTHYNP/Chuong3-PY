import datetime


ten=input("Nhập tên: ")
namsinh=int(input("Nhập năm sinh: "))
nam = datetime.datetime.now().year
tuoi = nam - namsinh
print(ten," " ,tuoi, "Tuổi" )