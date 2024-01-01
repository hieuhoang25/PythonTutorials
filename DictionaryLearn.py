# Khai bao
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
mixed_dict = {'name': 'Bob', 'age': 30, 'is_student': True}
empty_dict = {}
# truy cap
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: 'Alice'
print(my_dict['age'])   # Output: 25
print(my_dict.get('city',"null")) # Output: 'New York'
# Thay doi gia tri
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict['age'] = 26      # Thay đổi giá trị của key 'age'
my_dict['job'] = 'Engineer'  # Thêm một cặp key-value mới
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
# Xoa phan tu
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
del my_dict['age']   # Xóa phần tử có key là 'age'
my_dict.clear()      # Xóa toàn bộ nội dung của Dictionary
# Kiem tra su ton tai cua key
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print('age' in my_dict)  # Output: True
print('job' in my_dict)  # Output: False
# Lấy danh sách các keys hoặc values từ Dictionary:
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])
