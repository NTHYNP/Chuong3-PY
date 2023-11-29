def kiem_tra_so_nguyen_to(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))

print(f"Các số nguyên tố từ 2 đến {n} là:")
for i in range(2, n + 1):
    if kiem_tra_so_nguyen_to(i):
        print(i, end=" ")