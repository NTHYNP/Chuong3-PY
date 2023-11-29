n = int(input("Nhập số nguyên dương n (> 0): "))

if n > 0:
    binary = bin(n)[2:]  # Sử dụng hàm bin() và bỏ đi hai ký tự đầu ('0b') trong chuỗi kết quả
    print(f"Số nhị phân của {n} là: {binary}")
else:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")