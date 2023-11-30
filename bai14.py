import datetime

# 1 Viết hàm getting() trả về câu chào tương tự bài 2
def getting():
    ten=input("Nhập tên: ")
    namsinh=int(input("Nhập năm sinh: "))
    nam = datetime.datetime.now().year
    tuoi = nam - namsinh
    print(ten ,tuoi, "Tuổi" )

# 2 Viết hàm rabbit_count tính số thỏ tưởng tư bài 3
def rabbit_count(n):
    sotho = 2
    for i in range(n):
         sotho = sotho * 2
    print("Sau ", n ," tháng thì số thỏ là: ", sotho)


# 3 viết hàm count_mark trả về số sinh viên và số sinh viên học lại theo bài 5
def count_mark(n):
    # Số học sinh trong lớp
    print('Số học sinh trong lớp là: ', len(n))
    # đếm số học sinh học lại
    hoclai = n.count('F')
    print('Số học sinh học lại là: ',hoclai)


# 4 Viết hàm bmi_show trả về nhận xét dựa vào chiều cao và cân nặng theo bài 7 
def bmi_show(chieucao, cannang):
    bmi = cannang / ((chieucao/100)*(chieucao/100))
    print(bmi)
    if(bmi < 18.5):
        print('Underweight')
    elif(bmi < 25):
        print('Normal Weight')
    elif(bmi < 30):
        print('OverWeight')
    else:
        print('Obese')


# 5 Viết hàm cal_point trả về diểm trung bình hệ 10 và hệ 4 của 1 học sinh theo bài 10
def cal_point(diemso):
    diemhe4 = []
    for i in diemso:
        if(i < 4):
            diemhe4.append(0)
        elif(i < 5):
            diemhe4.append(1)
        elif(i < 5.5):
            diemhe4.append(1.5)
        elif(i < 6.5):
            diemhe4.append(2)
        elif(i < 7):
            diemhe4.append(2.5)
        elif(i < 8):
            diemhe4.append(3)
        elif(i < 8.5):
            diemhe4.append(3.5)
        elif(i < 9):
            diemhe4.append(3.7)
        else:
            diemhe4.append(4)
    print('-------------Điểm Trung Bình--------------')
    print('Tổng số môn học: ', len(diemso))
    print('ĐTB hệ 10: ', sum(diemso)/len(diemso))
    print('ĐTB hệ 4: ', sum(diemhe4)/len(diemhe4))

# 5 Viết hàm list_prime trả danh sách các số nguyên tố khoảng từ 1 đến n theo bài 12

def list_prome(n):
    def kiem_tra_so_nguyen_to(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    print(f"Các số nguyên tố từ 1 đến {n} là:")
    for i in range(2, n + 1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=" ")




# Test các hàm đã viết

getting()
rabbit_count(3)
count_mark(['C','B','D','A','F','A','B','F','B','B','C','A','D','F','B'])
bmi_show(167,70)
cal_point([8.6, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1])
list_prome(9)

