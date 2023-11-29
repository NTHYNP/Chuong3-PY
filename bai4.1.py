text = "Nước Việt Nam là một, dân tộc Việt Nam là một, Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 - 1969)"
text1 = "hồ chí minh"
text2 = "non sông"

# Số ký của đoạn văn
print("Số ký tự có trong đoạn văn trên là: ", len(text))

# kiểm tra chuỗi có năm trong đoạn văn
print("===================================")
if(text1.lower() in text.lower()):
    print("Chuỗi: ", text1, " nằm trong chuỗi đã cho")
else: 
    print("Chuỗi: ", text1, " không nằm trong chuỗi đã cho")
if(text2.lower() in text.lower()): 
    print("Chuỗi: ", text2, " nằm trong chuỗi đã cho")
else: 
    print("Chuỗi: ", text2, " không nằm trong chuỗi đã cho")

# Tách đoạn văn thành mảng đoạn văn nhỏ
print("===================================")
array = text.split(',')
print(array)

# Kiểm tra đoạn văn có chứa ký tự không
print("===================================")
kiemtra = any(not char.isalnum() for char in text)

if kiemtra:
    print("Đoạn văn có chứa ký tự không phải chữ hoặc số")
else:
    print("Đoạn văn chỉ chứa chữ và số.")

# Thay thế từ "Việt nam" thành "VIỆT NAM"
print("===================================")
newText = text.replace('Việt Nam', 'VIỆT NAM') 
print(newText)