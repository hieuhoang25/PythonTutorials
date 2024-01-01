# Khai bao
myTuple = (1,2,3,4,5,6,7,8,9,10,11,12,13)
mixedTuple =  (1, 'hello', True, 3.14)
simpleElement = (42,)  # Khi khai báo Tuple chứa 1 phần tử, cần có dấu phẩy ở cuối
emptyList = ()
# Truy cap phan tu
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1]) # Output: 5 (chỉ số âm đếm từ cuối về đầu)
# Không thay đổi giá trị của Tuple:
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Lỗi! Tuple không thể thay đổi giá trị của phần tử
# Sử dụng Tuple để gán giá trị đồng thời:
point = (10, 20)
x, y = point
print(x)  # Output: 10
print(y)  # Output: 20

#Sử dụng Tuple trong hàm:
def get_info():
    name = "Alice"
    age = 30
    return name, age

info = get_info()
print(info)       # Output: ('Alice', 30)
name, age = info
print(name)       # Output: Alice
print(age)        # Output: 30
