n=int(input("Nhập số kẹo: "))
m=int(input("Nhập số học sinh: "))
sokeo = n // m
du = n % m
if(n < m):
    print("Thiếu số kẹo là", m - n)
else:
    print("Mỗi học sinh được số kẹo là: ", sokeo)
    print("Cô còn lại số kẹo là: ", du)
