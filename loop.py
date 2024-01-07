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
# 2. Using "for" with a tuple
numbers = (1,2,3,4,5,5,6,7)
total = 0
for num in numbers:
    total+=num
print("Total = ", total)
# 3. Using "for" with a lists
numbers  = [1,2,3,4,5,6,7]
for num in numbers:
    if num % 2 == 0:
        print(num, end=' ')
# 4. Using "for" with a range object
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
# 5. Factorial of a number
fact = 1
N = 5
for x in range(1,N+1):
    fact = fact*x
print("Factorial of {}! is {}".format(N, fact))
# 6. Using "for" Loop with Sequence Index
numbers = [1,2,3,4,5,6,7,8,9]
indices = range(len(numbers))
for index in indices:
    print("index:", index, "number:", numbers[index])
#7 Using "for" Loop with dictionary
numbers = {10:"Ten", 20: "Twenty", 30:"Thirty", 40:"Forty"}
for x in numbers:
    print(x)
    print("get1: ",numbers[x])
    print("get2: ",numbers.get(x))

for x  in numbers.items():
    print(x)

for x, y in numbers.items():
    print(x," -- " ,y)

for x  in numbers.keys():
    print(x, "-------->", numbers[x])