
chieucao = int(input("Nhập chiều cao(cm): "))
cannang = int(input("Nhập cân nặng(kg): "))

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