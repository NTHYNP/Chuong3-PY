import datetime

# Xây dựng lớp Person với các giá trị thuộc tính là thông tin của bạn

class Person:
    def __init__(self, name="Nguyễn Tuấn Hưng", year=2002, height=170, weight=60):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def bmi(self):
        height_in_meter = self.height / 100  # Chuyển đổi chiều cao từ cm sang mét
        bmi_value = self.weight / (height_in_meter ** 2)
        print(f'Chỉ số BMI: {bmi_value}')

    def Getting(self):
        now = datetime.datetime.now().year
        age = now - self.year
        print('My name is: ', self.name)
        print(f"I am {age} years old. Nice to meet you!")
    


# Lớp Việt Nam kế thừa từ lớp person
class VietNam(Person):
    def __init__(self, name="Nguyễn Tuấn Hưng", year=2002, height=170, weight=60, nation='Kinh'):
        super().__init__(name, year, height, weight)
        self.nation = nation

    def Getting(self):
        print(f"Tôi tên là: {self.name} - Dân tộc: {self.nation}")
        print(f"Tôi sinh năm {self.year}. Rất vui được làm quen với bạn!")



# Tạo đối tượng và gọi phương thức

# p1 = Person('Nguyễn văn A',1990, 165, 70)
p1 = Person()
p1.Getting()
p1.bmi()

vn1 = VietNam('Thanh Huyền', 2000, 169, 52, 'Tày')
vn1.Getting()
vn1.bmi()