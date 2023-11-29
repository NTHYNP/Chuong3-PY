
thangsinh = int(input("Nhập tháng sinh của bạn: "))

if(thangsinh < 1 or thangsinh > 12):
    print('Tháng sinh không hợp lệ!')
elif(thangsinh <= 3):
    print('Bạn sinh vào Mùa xuân!')
elif(thangsinh <= 6):
    print('Bạn sinh vào Mùa hạ')
elif(thangsinh <= 9):
    print('Bạn sinh vào Mùa thu')
else:
    print('Bạn sinh vào Mùa đông')