# Khai bao
myList = [1,2,3,4]
mixedList = [1,'hello', True, 3.14, {1,2,4}, [1,2,3],(1,2,3)]
emptyList = []
# Truy cap element
print(mixedList)
print(myList[3])
# Cac phuong thuc lists
#1. append Thêm một phần tử vào cuối List.
myList.append(5)
print(myList)
# 2. insert(): Chèn một phần tử vào vị trí chỉ định trong List.
myList.insert(2,'hello')
print(myList)
# remove(): Xóa phần tử đầu tiên có giá trị cụ thể từ List.
myList.remove(2)
print(myList)
# pop(): Loại bỏ và trả về phần tử ở vị trí chỉ định (mặc định là phần tử cuối cùng).
print(myList.pop(1))
# len(): Lấy độ dài của List.
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4
