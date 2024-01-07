# Python
## 1. Define a variable
```python
tenBien =  giaTri
```
- `tenBien` là tên của biến. Tên biến này không được bắt đầu bằng số hay các ký tự đặc biệt, mà chỉ được bằng chữ cái hoặc _ và nó phân biệt hoa thường
- `giaTri` là giá trị mà bạn muốn gán
## 2. Các kiểu dữ liệu 
1. Number types:
- int : integer type: x = 10
- float : float type: x = 3.14
- complex : complex type: x = 2 + 3j
2. String types:
- str : string type: x = "Hello, world!"
3. Array types:
- list : save a list, it can be changed (mutable): myList = [1, 2, 3]
4. Tuples 
- tuple : like list but can not  be changed (immutable) : myTuple = (1, 2, 3)
5. Dictionary types
- dict : save key-value pairs: myDictionary = {'name': 'Alice', 'value':'123'}
6. Set types
-  set :  Lưu trữ tập hợp các giá trị duy nhất, không có thứ tự : myset = {1,2,3}
7. boolean types
- bool : is_valid  = True (False)
8. None types
- None: Được sử dụng để biểu diễn giá trị không tồn tại hoặc không có giá trị, ví dụ: x = None
## 3. Check type of a variable
To check the type of a variable:
```python
type(data)
```
## 4. Cast a variable
- float(data) : to float
- int(data,base) : chuyển đổi sang kiểu số, trong đó base là kiểu hệ số mà các bạn muốn chuyển đổi sang (tham số này có thể bỏ trống).
- str(data): to string
- complex(data):chuyển đổi sang kiểu phức hợp.
- tuple(data):chuyển đổi sang kiểu phức hợp.
- dict(data) chuyển đổi sang kiểu Dictionary.
- hex(data) chuyển đổi sang hệ 16.
- oct(data) chuyển đổi sang hệ 8.
- chr(data) chuyển đổi sang dạng ký tự.
## 5. Function Print 
```python
print(content)
```
1. Show two 2 block into print once
```python
print("Hello, world!", "Created by HieuHoang")
```
2. Have a charset
```python
print(content, end = "charset")
```
- demo
```python
print("Hello, world!", end = " - ")
print("I am Hieu")
```
## 6. String
1. Show characters specified
You can use \ characters before specifying them
```python
print("Hello, world \"Hieu \" ")
```
- \n ngắt xuống dòng và bắt đầu dòng mời.
- \t đẩy nội dung phía sau nó cách 1 tab.
- \a chuông cảnh báo.
- \b xóa bỏ khoảng trắng phía trước nó.
- Ngoài ra bạn cũng có thể sử dụng để in ra các ký tự đặc biệt khác bằng việc sử dụng theo cú pháp \xnn, với n là 0->9, hoặc a->f hoặc A->F.
2. Fomat chuỗi.
```python
print("%type" %(binding))
```
Trong đó:
- type là các kiểu dữ liệu các bạn muốn binding và thay thế vào vị trí đó.
- binding là giá trị mà các bạn muốn binding vào vị trí được xác định trong chuỗi.
- Type là các kiểu sau:
- - %c : character
- - %s : chuoi
- - %i : so nguyen
- - %d : so nguyen
- - %u	số nguyên
- - %o	bát phân
- - %x	thập lục phân (in thường)
- - %X	thập lục phân (in hoa)
- - %e	số mũ  (với e thường)
- - %E	số mũ  (với e hoa)
- - %f	số thực
- - %g	dạng rút gọn của %f and %e
- - %G	dạng rút gọn của %f and %E
```python
guy = "Peter"
full = "Welcome to chanel, %s" %(guy)
print(full)
```
- bạn muốn binding nhiều chuỗi vào trong chuỗi thì mỗi giá trị bạn muốn binding cách nhau bởi 1 dấu ,
```python
guy = "Ban"
doamin = "toidicode.com"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)
```
3. Truy cap tung gia tri cua chuoi
De truy cap toi ky tu trong chuoi co su dung cu phap sau:
```python
stringName[index]
```
Trong đó:
- stringName là tên của biến chứa chuỗi, hoặc chuỗi.
- index là vị trí của ký tự bạn muốn lấy ra. Index này hỗ trợ chúng ta truy xuất được cả 2 chiều của chuỗi nếu:
- - Tính từ đầu thì nó bắt đầu từ 0.
- - Tính từ cuối thì nó bắt đầu từ -1.
```python
name = "Vu Thanh Tai"
print(name[0]) # V
print(name[-1]) # i
```
- Nếu trong trường hợp các bạn muốn lấy nội dung của một đoạn chuỗi trong chuỗi đó thì có thể sử dụng cú pháp sau:
```python
stringName[start:end]
```
- stringName là tên của biến chứa chuỗi, hoặc chuỗi.
- start là vị trí của ký tự bắt đầu lấy, nếu để trống start thì nó sẽ lấy từ 0.
- end là vị trí kết thúc (nó sẽ lấy trong khoảng từ start đến < end), nếu để trống end thì nó sẽ lấy đến hết chuỗi.
```python
name = "Vu Thanh Tai"

print(name[0:2]) # Vu

print(name[-3:12]) # Tai

print(name[9:]) # Tai

print(name[-3:]) # Tai
```
4. Các phương thức xử lý chuỗi:
- Độ dài chuỗi: hàm len() để lấy độ dài của chuỗi.
```python
my_string = "Hello"
print(len(my_string))  # Output: 5
```
- Chuyển đổi chuỗi: upper() và lower()
```python
string = "Hello, World!"
print(string.upper())  # Output: HELLO, WORLD!
print(string.lower())  # Output: hello, world!

```
- Loại bỏ khoảng trắng: strip() : Loại bỏ khoảng trắng ở cả hai đầu của chuỗi. , lstrip(): Loại bỏ khoảng trắng ở bên trái (đầu) của chuỗi. , và rstrip(): Loại bỏ khoảng trắng ở bên phải (cuối) của chuỗi.
```python
string = "   Hello, World!   "
print(string.strip())   # Output: 'Hello, World!'
print(string.lstrip())  # Output: 'Hello, World!   '
print(string.rstrip())  # Output: '   Hello, World!'
```
- Thay thế: replace(old, new): Thay thế tất cả các chuỗi con old trong chuỗi ban đầu thành new
```python
string = "Hello, World!"
print(string.replace('World', 'Python'))  # Output: Hello, Python!
```
- Tách chuỗi: split(separator): Tách chuỗi thành danh sách các phần tử dựa trên separator.
```python
string = "Hello, World!"
print(string.split(','))  # Output: ['Hello', ' World!']
```
- Kiểm tra chuỗi: startswith(prefix): Kiểm tra xem chuỗi có bắt đầu bằng prefix không; endswith(suffix): Kiểm tra xem chuỗi có kết thúc bằng suffix không.
```python
string = "Hello, World!"
print(string.startswith('Hello'))  # Output: True
print(string.endswith('World!'))   # Output: True
```
- Định dạng chuỗi: format(): Định dạng chuỗi với các giá trị được chèn vào chuỗi.
```python
name = "Alice"
age = 30
print("Her name is {} and she is {} years old.".format(name, age))
# Output: Her name is Alice and she is 30 years old.
```
## 7. Number
1. Integer : Lưu trữ các số nguyên không có phần thập phân.
```python
x = 10
y = -20
z = 0
```
2. Số thực (floats): Lưu trữ các số có phần thập phân.
```python
a = 3.14
b = -0.001
c = 2.0
```
3. Số phức (complex): Lưu trữ các số phức với một phần thực và một phần ảo.
```python
d = 2 + 3j
e = 4 - 5j
```
4. Các phép toán số học:
```python
# Cộng, trừ, nhân, chia
result_add = 10 + 5       # Output: 15
result_sub = 10 - 5       # Output: 5
result_mul = 10 * 5       # Output: 50
result_div = 10 / 5       # Output: 2.0 (Trong Python 3, kết quả chia sẽ luôn là số thực)

# Phép chia lấy phần dư
result_mod = 10 % 3       # Output: 1 (phần dư của 10 chia 3 là 1)

# Lũy thừa
result_exp = 2 ** 3       # Output: 8 (2 lũy thừa 3)
```
5. Su dung math
```python
import math

# Căn bậc hai
result_sqrt = math.sqrt(16)  # Output: 4 (căn bậc hai của 16)

# Logarit cơ số 10
result_log = math.log10(100)  # Output: 2 (logarit cơ số 10 của 100)
```
6. muốn giải phóng một vùng nhớ cho một biến
```python
del avariableName
# hoặc xóa nhiều biến
del avariableName1, avariableName2,..., avariableName3
```
```python
age = 22
print(age) # 22

del age
print(age)
# name 'age' is not defined
```
## 8. List
1. Khai bao
```python
lists = [value1, value2,..., valueN]
```
2. Truy cap element
```python
lists[index]
```
```python
name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0]) # Vu Thanh Tai
print(name[1]) # Nguyen Van A
print(name[2]) # Nguyen Thi E
# hoặc
print(name[-3]) # Vu Thanh Tai
print(name[-2]) # Nguyen Van A
print(name[-1]) # Nguyen Thi E
```
```python
list[start:end]
```
Trong đó:
- list là tên của biến chứa list.
- start là ví trí bắt đầu lấy ra list con. Nếu để trống thì nó sẽ lấy từ đầy list.
- end là vị trí kết thúc. Nếu để trống thì nó sẽ lấy đến phần tử cuối cùng của list.
```python
name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0:2])
# ['Vu Thanh Tai', 'Nguyen Van A']

# hoặc

print(name[-3:-1])
# ['Vu Thanh Tai', 'Nguyen Van A']
```
3. Change and Delete element
- Update element
```python
name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

name[1] = 1996
print(name)
# ['Vu Thanh Tai', 1996, 'Nguyen Thi E']
```
- Delete element
```python
name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

del name[2]
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A']
```
4. List lồng nhau
```python
option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]
```
```python
option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

subList = myList[1] # [12, 5, 1996]
subList[0] # 12

# hoặc có thể viết ngắn gọn như sau
myList[1][0] # 12
```
## 9. Tuple 
Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số). Còn lại thì cách lưu trữ của nó cũng khá giống như kiểu dữ liệu list
1. Khai bao
```python
tuples = (val1, val2,.., valn)
```
```python
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
```
Nếu bạn khai báo 1 biến chứa các giá trị mà không được bao quang bởi dấu () thì Python cũng nhận định nó là một tuple (nhưng mình khuyên mọi người lên sử dụng cách đầu tiên cho code được tường minh).
```python
day = 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday'
```
Và nếu như bạn muốn khai báo 1 tuple trống thì bạn chỉ cần khai báo như sau:
```python
a  = ()
```
Còn nếu như tuple của bạn chỉ chứa duy nhất một giá trị thì bắt buộc bạn phải thêm một dấu , nữa đằng sau giá trị đó
```python
a = (10,)
```
2. Truy cap phan tu
```python
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
day[0] # monday

day[-2] # saturday
```
```python
tupleName[start:end]
```
Trong đó:
- start là vị trí bắt đầu lấy. Nếu để trống start thì nó sẽ lấy từ đầu Tuple.
- end là vị trí kết thúc. Nếu để trống end thì nó sẽ lấy đến hết Tuple.
```python
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
day[1:3] # ('tuesday', 'wednesday')

day[:3] # ('monday', 'tuesday', 'wednesday')

day[1:] # ('tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
```
3. Cac tac vu khac tren Tuple
- Xóa Tuple.
```python
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
del day

print(day) # Error: name 'day' is not defined
```
- Thêm mới phần tử.
```python
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')

day = day1 + day2

print(day)
# ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
```
4. Tuple long
```python
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2

print(day2)
# ('thursday', 'friday', 'saturday', 'sunday', ('monday', 'tuesday', 'wednesday'))

print(day2[4][0]) # monday
```
## 10. Dictionary 
1. Khai bao
```python
dicts = {key1: value1, key2: value2,..., keyN: valueN}
```
```python
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }
```
2. Truy cap den phan tu dictionary
```python
dicName[key]
```
Trong đó:
- dicName là tên của của dictionary.
- key là tên của key các bạn muốn lấy ra trong dictionary.
```python
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }
person['name'] # Vũ Thanh Tài

person['status'] # signle
```
3. Thay đổi giá trị của dictionary.
```python
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'alone'        
    }

person['status'] = 'married'
print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True, 'status': 'married'}
```
4. Xóa phần tử
```python
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'alone'        
    }

del person['status']
print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True}
```
5. Xoa tat ca
```python
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'alone'        
    }

person.clear()
print(person)
#{}
```
6. Dictionary lồng nhau.
```python
person = {
    'name': 'Vũ Thanh Tài',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])
# 22
```
## 11. Opertator Precedence
1. (), [], {} : Parentheses and braces
2. [index], [index:index] : Subscription, slicing
3. await x : await expression
4. ** : Exponentiation
5. +x, -x, ~x : positive, negative, bitwise Not
6. *, @, /, // % : Multiplication, matrix multiplication, division, floor division, remainder
7. +, - : Addition and subtraction
8. <<, >> : left shifts, right shifts
9. & : bitwise AND
10. ^ : bitwise XOR
11. | : bitwise OR
12. in, not in, is, is not, <, <=,>, >=, !=, ==
13. not x
14. and
15. orr
16. if - else
17. lambda
18. := 

## 12. Toan tu so hoc - Arithmetic Operators
- `+` toan tu cong
- `-` toan tu tru
- `*` toan tu nhan
- `/` toan tu chia
- `%` toan tu chia lay phan du
- `**` toan tu mu a**b = a mu b
- `//` toan tu chia lam tron xuong
## 13. Toan tu gan
- `=`  c = a
- `+=` c += a => c = c+a
- `-=` c -= a => c = c - a
- `*=` c*=a   => c = c*a
- `/=` c/=a   => c = c/a
- `%=` c%=a  => c = c%a
- `**=` c**=a => c = c**a
- `//=` c//=a => c = c//a
## 14. Toan tu so sanh
- `<` a<b
- `>` a>b
- `<=` a<=b
- `>=` a>=b
- `==` a==b
- `!=` a!=b
## 15. Toan tu logic
- `and`
- `or`
- `not`
## 16. Toan tu biwter
- `&`
- `|`
- `^`
- `~`
- `<<`
- `>>`
## 17. Toan tu khai thac
- `in` check a elemnt in list
- `not in` check not in list
## 18. Toan tu xac thuc
- `is` => a == b
- `not is ` => a!=b
## 19. Control flow
1. The if statement : python provides if..elif..else control statement as a part of decision marking
2. The match statement: 
3. Loops or Iteration Statements : The for loop and the while loop
## 20. Match case statements
1. Syntax
```python
  match variable_name:
    case 'pattern 1': statement 1
    case 'pattern 2': statement 2
    ...
    case 'pattern n': statement n
    case '_': statement not true
```
2. Combined cases
Sometime, there may be a situation where for more thanone case, a similar action has to be taken. For this, you can combine cases wwith the OR operator represented by "|" symbol
```python
def access(user):
    match user:
        case "admin" | "manager": return "full access"
        case "guest" : return "limited access"
        case _: return "no access"
print(access("user"))
print(access("guest"))
print(access("admin"))
```
3. List as the argument
Since python can match the expression against any literal, you can use a list as a case value. Moreover, for variable number if items in the list, they can be parsed to a sequence with "*" operator
```python
def greeting(details):
    match details:
        case [time,name]:
            return f"Good {time} {name}!"
        case [time, *names]:
            msg = ''
            for name in names:
                msg += f'Good {time} {name}!\n'
            return msg
print(greeting(["Morning", "Hieu"]))
print(greeting(["Afternoon", "Hieu"]))
print(greeting(["Morning", "Hieu", "Cuong","hOANG"]))
```
4. Using "if" in "case" clauses
Python allows you to include if statements in the case clause for conditional computation of match varibles
## 21. Loops
```python
for interating_var in sequence:
    statements(s)
```
1. Using for with a string
A string is a sequence of unicode letters, each having a positional index. The following example compares each character
and displays if it is not a vowel ('a','e','I')
```python
# 1. Using "for" with a String
zen ='''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
print(zen)
for char in zen:
    if char not in 'aeiou':
        print(char, end=' ')
```
2. Using "for" with a tuple
Python's tuple object is also an indexed sequence, and hence we can traverse its items with a for loop
```python
numbers = (1,2,3,4,5,5,6,7)
total = 0
for num in numbers:
    total+=num
print("Total = ", total)
```
3. Using "for" with List
Python's list object is also an indexed sequence, and hence we can traverse its items with a for loop
```python
numbers  = [1,2,3,4,5,6,7]
for num in numbers:
    if num % 2 == 0:
        print(num, end=' ')
```
4. Using "for" with a range object
Pythons's built-in range object is also an indexed. 
```python
range(start, stop, step)
```
- `Start` - starting value of the range. Optional, default 0
- `Stop`  - The range goes upto stop -1
- `Step`  -  Integers in the range increment bt the step value. Option, default is 1
```python
numbers = range(5)
'''
start is 0 by default
step is 1 by default
range generated from 0 to 4
'''
print(list(numbers))
# step is 1 by default, range generated from 10 to 19
numbers = range(10,20)
print(list(numbers))
# range generated from 1 to 10 increment by step of 2
numbers = range(1,10,2)
print(list(numbers))
for num in numbers:
    print(num, end='')
```
5. Factorial of a number
Factorial is a product of all numbers from 1 to that number say n. It can alse be defined as profuct of 1,2, up, to n
```python
Factorial of a number n! = 1*2*...*n
```
6. Using "for" Loop with Sequence Index
To iterate over a sequence, we can obtain the list of indices using the range() function
```python
Indices = range(len(sequence))
```
7. Using "for" Loop with Dictionary
Unlike a list, tuple or a string, dictionary data type in python is not sequence, as the items do not have a position index. However, traversing a dictionary is still possible with deffent techniques
## 22. for else loops
```python
for count in range(6):
    print("Iteration no. {}".format(count))
else :
    print("For loop over. Now in else block ")
print("End of for loop")
```
2. Nested loops in python
```python
for interation_var in sequence:
    for interating_var in sequence:
        statemnets(n)
        statemnets(n)
```
```python
    while expression:
        while expression:
            statements(n)
        statement(n)
```
## 23. While loops in python
```python
# syntax
while expression:
    statement(n)
```
```python
count = 0
while count < 5 :
    count += 1
    print("Iteration no  %i"%(count))
print("End of while loop")
var = '0'
while var.isnumeric() == True:
    var = input('enter a number..')
    if var.isnumeric() == True:
        print("Your input:",var)
print("End of while loop")
```
2. The infinite loop
```python
var = 1
while var == 1:
    num = int(input('enter a number:'))
    print("Your input:",num)
print("Goodbye")
```