# comparing strings

# print("letters" < "letter") # False
# print("char" < "letter") # true
# print("char" != "char") # False
# print("char" != "cher") # true
# print("A" != "a") # True



# Logical Operators

# age , salary = 30 , 7000
# result = (age > 25) and (salary < 8000)
# # result = True and True
# # result = True
# print(result)

# print(age > 25 and salary > 9000)
# print(age > 35 or salary < 8000)
# print(age > 35 and salary > 9000)

# mixing logical operators
# age , salary  , weight = 30 , 7000 , 110

#  True or False
# print(age > 25 and salary < 8000 and weight < 150)
# print(age > 25 and salary < 8000 and weight > 200)
# print(age > 35 and salary > 6000 or weight < 200)
# print(False and True or True )
# print(False or True )

"""
Conditions:
if statement -> 
1st style 
if condition:
    body -> single line or multi line or complex logic or more if's
    "Identation" 
    
2nd Style
if condition:
    body
elif condition:
    body
elif condition:
    body
elif condition:
    body
    
    
3rd Style:
if condition:
    body
elif condition:
    body
elif condition:
    body
elif condition:
    body
else:
    body
"""

# x = 5
# if x < 10:
#     print("Smaller")

# if x > 20:
#     print("Bigger")

# print("Finish Program")


# comparing operators
# x = 5
# if x == 5:
#     print("Equal 5")
# if x > 4:
#     print("Greater than 4")
# if x >= 5:
#     print("Greater than or equal 5")
# if x < 6:
#     print("Less than 6")
# if x <= 5:
#     print("Less than or equal 5")
# if x != 6:
#     print("Not equal 6")
    
    # """"
    # Equal 5
    # Greater than 4
    # Greater than or equal 5
    # Less than 6
    # Less than or equal 5
    # Not equal 6
    # """
    
# x = 5
# print("Before 5")

# if x == 5:
#     print("Is 5")
#     print("Is still 5")
#     print("Third 5")

# print("After 5")
# print("Before 6")

# if x == 6:
#     print("Is 6")
#     print("Is still 6")
#     print("Third 6")

# print("After 6")

# nested if conditions
# num = int(input("Enter Number: "))
# if 100 <= num <= 200:
#     print("Let's go ")
#     if num % 2 == 0:
#         print("Even Number ")
#         if num == 150:
#             print("150 is Lucky number")    
#         else:
#             print("not a lucky number")
#     else:
#         print("Bye Mr Odd")
# else:
    # print("Have a good day")
    
# Simple calculator
# num1 , op, num2 = input("Enter your number and operator: ").split()
# num1, num2 = float(num1), float(num2)

# if op == '+':
#     print( num1 + num2 )
# elif op == '-':
#     print( num1 - num2 )
# elif op == '*':
#     print( num1 * num2 )
# elif op == '/':
#     if num2 > 0:
#         print(num1 / num2)
#     else:
#         print("N/A")
# else:
#     print("Check your inputs")
    
# Minimum of 3 numbers
# num1, num2, num3 = map(int, input("Enter 3 numbers: ").split())

# if num1 < num2:
#     if num1 < num3:
#         print("Num 1: ", num1,"Is a minimum number")
# else:
#     if num2 < num3:
#         print("Num 2: ", num2,"Is a minimum number")
    # else:
    #     print("Num 3: ", num3,"Is a minimum number")

# if num1 < num2 and num1 < num3:
#     print("Num 1: ", num1,"Is a minimum number")
# elif num2 <= num1 and num2 <= num3:
#     print("Num 2: ", num2,"Is a minimum number")
# else:
#     print("Num 3: ", num3,"Is a minimum number")

"""
num1 = 5
num2 = 3
num3 = 2

ans = num1 = 5
ans = num2 = 3
ans = num3 = 2
"""
# ans = num1
# if ans > num2:
#     ans = num2
# if ans > num3:
#     ans = num3
# print(ans)

"""
Loops
While loop
for loop
"""

"""
while loop
1- initialization
2- condition
3- action
4- steps
"""
# x = 1 # initialization
# while x <= 5: # condition
#     print(x, end = " ") # action
#     x+=1 # increment step
# print()
# print(x)

# x = 6
# while 2 < 5 and x >= 0:
#     print("Hello")
#     x-=1

# sum 1+2+3+4+5
# x = 1
# sum_ = 0
# while x <=5:
#     sum_ += x
#     x+=1
# print(sum_)


"""
break -> tell computer stop this condition

continue -> tell computer jump to the while start again continue from there 
"""
# read 2 number from user print float division if 2nd number zero -> print bye and end the program

# while True:
#     num1,num2 = map(float, input("Enter 2 number: ").split())
#     if num2==0:
#         print("Num2 is zero: ")
#         break
#     print(num1/num2)
    
# print("bye")


# while True:
#     num1,num2 = map(float, input("Enter 2 number: ").split())
#     if num2==0:
#         print("Num2 is zero: ")
#         continue # jump to while loop line
#     print(num1/num2)
#     break
# print("bye")

# read number from user print number is divisible by 3
# 10 -> 3 , 6, 9
# num = int(input("Enter your number"))
# start = 1
# while start < num:
#     if start % 3 == 0:
#         print(start, end = " ")
#     start += 1
# print()
# print()

# num = 00592 -> 592
"""
112
num = 5
digit += 1
digit  = 1

num = 9
digit += 1
digit  = 2

num = 5
digit += 1
digit  = 3

//
592 // 10
59.2

"""

# num = int(input("Enter your number: "))
# print(num)
# digits = 0
# while num > 0:
#     digits +=1
#     num = num // 10
# print(digits)

"""
for loops
the range function return
sequance of number:
start from 0
increment default by 1
stop before a specified number -> n-1

for loop syntax
for iterator in range(start, end, steps):
    action
"""
# i = 0
# while i < 5:
#     print(i, end = " ")
#     i+=1
# print()
# for i in range(5):
#     print(i, end = " ")

# for i in range(2,5):
#     print(i, end= " ")


# for i in range(1,21,4):
#     print(i , end= " ")

# rng = range(1,21,4)
# for i in rng:
#     print(i, end= " ")

# iterate backword
# for i in range(5,0,-1):
#     print(i, end = " ")

# for i in range(5):
#     pass
#     ...

# for with string 
# String -> sequance of chars
# mystr = "Python"
# for i in mystr:
#     print(i, end = " ")

# enumerate -> get index of position
# mystr_2 = "Machine"
# # for i in enumerate(mystr_2):
# #     print(i, type(i))
# for i,j in enumerate(mystr_2):
#     print(i,j, type(j))

# for i,j in enumerate(range(5,10)):
#     print(i,j)

# for i in enumerate(range(5,10)):
#     idx,val = i
#     print(idx,val)

# nested for loop
"""
input -> tc 3 -> 5 , 10 , 3
sum from 1 to num
1 -> 1 + 2 + 3 + 4 + 5 = result = 15
2 -> 1 + 2 + 3 + 4 + 5 + ... + 10 =  result = 55
3 -> 1 + 2 + 3 = result = 6
"""

# tc = int(input("Enter number of Test Cases: "))
# for i in range(tc):
#     n = int(input("Enter number: "))
#     sum_ = 0
#     for pos in range(1,n+1):
#         sum_ += pos
#         """
#         sum = 1
#         sum = 1 + 2
#         sum = 1 + 2 + 3
#         sum = 1 + 2 + 3 + 4
#         sum = 1 + 2 + 3 + 4 + 5
#         """
#     print("Sum from 1 to -> ", n ,"=", sum_)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end = "\t")

# for i in range(5):
#     print(i)
# else:
#     print("No items left")

# for i in range(6):
#     print(i)
# print(i)
# if i == 5:
#     print("No Item left")
# else:
#     print("We stop at 4")



# data structure in python
# List , Tuple , Dictionary , set
# list - mutable, any kind of data or data type

# bracket []-> [0,1,2,3,..]
# seperate betwwen item using comma ','
# str1 = "Python"
# for i in str1:
#     print(i)

# lst = [5,6,1,2,8]
# print(len(lst))

# check num in lst
# print(5 in lst)

# print(lst)
# for i in lst:
#     print(i)    

# List can contain different data type
# lst =  [1, "iti",5.3,[4,5,6,7]]
# for i in lst:
#     print(i, type(i))

# index of list start from 0
# print(lst[0])

# build list from scratch
# lst = list() # empty list
# # append function
# lst.append("ITI")
# lst.append("Python")
# lst.append(1)
# lst.append(5)
# print(lst)
# lst2 = lst
# print(lst.pop())
# print(lst2)
# print(lst2[-1])


# 0   1  2  3  4 -> index of value
# 5   3  4  8  9 -> value
#-5  -4 -3 -2 -1

# Mutable
# lst = [1,2,3,4,5]
# lst[0] = 9
# print(lst)

# indexing
# num = [10 ,2, 7, 5, 3]
# num[0] = 9
# num[2] *=3
# num[4] +=1
# print(num[4])
# print(num)

# for i in range(5):
#     print(num[i], end = " ")

# lst = [1, 'ITI' , 5]
# another_list = [99, 11.5]
# # concatination lists
# conc_lst = lst + another_list
# # print(conc_lst)
# # [][]
# # [[],[]]
# # []
# # print(conc_lst)
# #
# thrd_lst = 3 * conc_lst
# print(thrd_lst)


# Append , extend and insert
# lst = [1,2,3,4,5]
# lst.append('Hello')
# print(lst)
# # #
# another_lst = [3,1]
# lst.extend(another_lst)
# print(lst)

# #insert take position and value
# lst.insert(2 , "wow")
# print(lst)
# print(lst[3])

# for i in lst:
#     print(i , end = " ")
# print()

# Pop , remove , del
#
# lst = [1,5,10,17, 2,"ITI"]
# print(lst.pop())
# print(lst)
# # take index
# print(lst.pop(3))
# print(lst)

# remove take value
# lst.remove(17)
# print(lst)

# del take index
# del lst[0]
# print()
# print(lst)

# clear
# print(lst.remove(5))
# print(lst.clear())
# print(lst)

# ____________________________________________________


# slicing in list
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(type(lst))

# print(type(range(5)))

# lst[start:end]
# lst[start:end:steps]

# slice_lst = lst[2:8]
# print(slice_lst)

# sl_lst = lst[2:] # from index 2 to end
# sl_lst = lst[2:100000]
# print(sl_lst)
# sl_lst = lst[:5]
# print(sl_lst)
# sam_val = lst[:4] + lst[4:6]
# print(sam_val)
# print(lst[:])

# slice with steps
# slicing list[st:end:stp]
# lst = [0,1,2,3,4,5,6,7,8,9,10]
# sub_lst = lst[: :-2]
# print(sub_lst)


# list comperehinsion

# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = []
# for i in lst1:
#     lst2.append(i*i+1)
# print(lst2)

# lst2 = [expression for increment in lst]
# lst2 = [i*i+1 for i in lst1]
# print(lst2)

# lst1 = [1,2,-4,3,-3,-7,6,-1]
# lst2 = []
# for i in lst1:
#     if i > 0:
#         lst2.append(i)
# print(lst2)

# lst3 = [i for i in lst1 if i > 0 if i%2==0]
# print(lst3)

# lst1 = [1,2,3]
# lst2 = [4,5,6]

# conc = lst1+lst2
# lst2.extend(lst1)
# print(conc,"\n")
# print(lst2)

# conc3 = [*lst1, *lst2]
# print(conc3)onc3 = [*lst1, *lst2]
# print(conc3)


# Tuples
# another an order collections of objects
# similer list
# iter , indexing, slicing, comparason, func -> min, max, sorted()

# more
"""
immutable data type: we can't change or delete iths item
many methods -> append , insert , remove
"""

# tup = (5,6,7)
# x,y,z = tup
# print(x,y,z)


# creation
# tup = ("iti" , 12, 3.4 , [1,2,3])
# print(tup)
# print(len(tup))
# print(type(tup))

# t = tuple('ITI')
# print(len(t))
# print(t)
# print(type(t))

# Unpacking
# lst = 1,2,3,4,5
# a,b,*c = lst
# print(a)
# print(b)
# print(c)

# *a,b,c = lst
# print(a)
# print(b)
# print(c)

# a,*b,c = lst
# print(a)
# print(b)
# print(c)


#  set -> () -> not repeated any values and sorted this values
# lst = [1,2,1,4,2,6,4,5,1,8,2,8,9,8,4,9,"ITI","ITI"]
# st = set(lst)
# print(st)
# # st[0] = 1 -> error
# print(st)

"""
Dictionary and Set
dictionary like list but it have key, value
key -> immutable
value -> mutable
"""

# lst = [1,2,33]
# print(lst[1]) # -> index

# dictionary = {Key : Value}
# dic = {0:1 , 1:2 , 213: 3}
# print(dic[213])
# print(dic[0])

# dic = {
#     'p' : 'Python',
#     'i' : "ITI",
#     'w' : "Winter"
# }
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic['p'])

# update and delete
# dic = {}

# # key       #value
# dic[12] = [234,(1,"ITI")]
# dic["ITI"] = 20
# print(dic.keys())
# print(dic.values())
# print(dic)

# # del func
# del dic[12]
# print(dic)
# print(type(dic))

# Indinxing dic values
# dic = {
#     "ITI" : "Learn",
#     1 : [1,5,7,8],
#     3: [[3,4],[8,9,10]]
# }

# print(dic["ITI"])
# print(dic["ITI"][-1])
# print(dic[1][1])
# print(dic[3][0][1])

# dic = {
#     int : [1,2,3],
#     2: 40,
#     2: 50
# }
"""
key    value
2   ->  50
"""
# print(dic[2])
# # # # get method
# print(dic.get(2))
# print(dic.get(int))

# dic = {'x':11 , 'b':22 , 'y': 30}
# dic['a'] = 33
# print(dic)

# while dic:
#     print(dic.popitem())

# clear -> dic.clear() -> remove all keys
# print(dic)
# print(dic.clear())
# print(dic)
