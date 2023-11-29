
diemso = [8.6, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
diemchu = []
diemhe4 = []
for i in diemso:
    if(i < 4):
        diemchu.append('F')
        diemhe4.append(0)
    elif(i < 5):
        diemchu.append('D')
        diemhe4.append(1)
    elif(i < 5.5):
        diemchu.append('D+')
        diemhe4.append(1.5)
    elif(i < 6.5):
        diemhe4.append(2)
        diemchu.append('C')
    elif(i < 7):
        diemhe4.append(2.5)
        diemchu.append('C+')
    elif(i < 8):
        diemchu.append('B')
        diemhe4.append(3)
    elif(i < 8.5):
        diemchu.append('B+')
        diemhe4.append(3.5)
    elif(i < 9):
        diemchu.append('A')
        diemhe4.append(3.7)
    else:
        diemchu.append('A')
        diemhe4.append(4)
print('Điểm hệ 10: ', diemso)
print('Điểm hệ chữ tương ứng: ',diemchu)
print('-------------Điểm Trung Bình--------------')
print('Tổng số môn học: ', len(diemso))
print('ĐTB hệ 10: ', sum(diemso)/len(diemso))
print('ĐTB hệ 4: ', sum(diemhe4)/len(diemhe4))
