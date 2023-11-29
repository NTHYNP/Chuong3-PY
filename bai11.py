
n = int(input("Nhập số nguyên dương n: "))
check = True
if n <= 1:
    print(f"{n} không phải là số nguyên tố.")
    check = False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(f"{n} không phải là số nguyên tố.")
        check = False
if(check):
    print(f"{n} là số nguyên tố.")