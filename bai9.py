
while True:
        number = int(input("Nhập số từ 1 đến 10: "))
        if 1 <= number <= 10:
            for i in range(1, 11):
                result = number * i
                print(f"{number} x {i} = {result}")
            break  
        else:
            print("Vui lòng nhập số từ 1 đến 10.")
