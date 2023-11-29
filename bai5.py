
diem = ['C','B','D','A','F','A','B','F','B','B','C','A','D','F','B']

# Số học sinh trong lớp
print('Số học sinh trong lớp là: ', len(diem))

# đếm số học sinh học lại
print("===================================")
hoclai = diem.count('F')
print('Số học sinh học lại là: ',hoclai)


# Số học sinh từ điểm B trở lên 
print("===================================")
hocsinhgioi = 0
for i in diem: 
    if(i == 'A' or i == 'B'):
        hocsinhgioi += 1
print('Có ', hocsinhgioi, ' Từ điểm B trở lên')


# Xóa học sinh đầu và học sinh cuối
print("===================================")
print('Bảng điểm mới:')
del diem[0]
del diem[-1]
print(diem)