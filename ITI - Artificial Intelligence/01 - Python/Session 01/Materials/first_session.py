# Compiler and Interpreter:
# compiler: computer program that read program written in a high level language it can translate it into
# the same program in a low level language including machine language

# interperter: program that execute programming code directly -> line by line 

# coding style
# x = 2
# losely typed -> type = value
# y = 'mohamed'

# type class -> to know what is the type of the variable
# type()
# print(x, type(x)) 
# print(y, type(y))

# assignment operators
# x = 2
# x = x+2
# x += 2

# print(x)

# printing 
# function
# print("Hello, ITI")
# print('Hello, ITI')

# print()
# print: function
# comment one line
# this function sum two numbers
"""
Doc string

multi line comment 
this class
1- method 1 -> 
2- method 2 -> 
"""

"""
print('' || "")
() -> parentheses
'' -> single quotes
"" -> double qoutes
Hello -> letter
hello world -> string -> sequance of letter
"""

# String -> sequance of charachter
# \n -> new line 
# \ -> scape charachter
# print("Hello \npython \nITI")
# print('hello',
#       'python',
#       'iti')

# comma in printing -> doing space
# print(1+2,5*3)
# / division 
# // division floor -> integer -> integer division
# print(7/2)
# print(type(7//2))
# print(type(7//2.0))
# syntax error
# print("Hello"
# EOF
# print('let's play)
# print("let's play ")
# print('let\'s play ')
# print('let"s play ')

# Python is a case sensetive -> cabital variable not equal small variable
# Indenation Error
# you have extra spaces
# x = 'python'
# print(x)
#  test = "error indentation"
#  print(test)

# Python Data Types

# Numeric -> Integer, Float , Complex Number.
# Dictionary {,} -> Key,Value
# Boolean -> True, False
# Set -> () -> haven't duplicate and order your data
# Sequance Type -> String, List, Tuple

# Identifier (Var name)
# can't start with digit (5address)
# can't start with space or spechial char: < > / \ ? ! ( ) # $ % ^ & ~ + - *
# pythn case sensitive ->  sum != SUM
# you shouldn't use reversed keyword (built in) -> print = 4, return = 'test' 


# String 
# print("Welcome in ITI")
# # concatination
# print("Welcome in" +" ITI") # concatination string

# str1 = "Welcom in"
# str2 = " ITI"
# # print(str1 + str2)
# print(str2 * 3)
# print(2* str1 + str2)
# str3 = str1 + str2 + str1
# print(str3)

# \t -> escape charachter for tab -> extra spacses -> 8 space 
#  handel data like table
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end ="\t")

# min , max function
# ans = min(5,6,7,8,9,...)
# print(ans)

# ans2 = max(5,6,7,8,9,...)
# print(ans2)

# args -> arguments
# def adder(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)

# lenght function len -> count -> start from 1
# str1 = 'python for machine learning'
# str2 = 'ITI '
# # print(len(str2))
# # print(len(str1)) 
# print(str2[-1])

# Casting | Conversion
# type to another type
# str1 = '10'
# print(str1,type(str1))

# conv_str_to_int = int(str1)
# print(conv_str_to_int, type(conv_str_to_int))
# print()
# conv_str_to_float = float(str1)
# print(conv_str_to_float, type(conv_str_to_float))
# print(len(str1))
# print()
# print()
# print(len(conv_str_to_float)) -> error

# Reading 
# input function
# inp = input("Enter Your name and brother name : ")
# print("Your name is:", inp)
# print(type(inp))
# input function accept anything -> as a string

# print("Hello",input("Enter your name: "))

# a = input("Enter Your name:")
# b = input("brother name: ")
# print(a+" "+b)

# print(type(a))
# print(type(b))

# casting input || conversion input
# a = int(input("Enter your input: "))
# # print(a,type(a))
# b = int(input("Enter your input: "))
# print(a+b)

# reading multiple inputs -> one line

# a,b,c = input("input 3 var ").split()
# print(a, b, c)
# print(type(a))


# def addition(n):
#     return n + n

# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# a,b,c = map(int, input("input 3 var: ").split())
# print(a, b, c)
# print(type(a),type(b),type(c))

# Arithmatic Operators
# + - * / // %
# x = 3
# y = 6

# Binary operators , Unary operators
# print(x + y) # 9
# print(x + 2*y - 1) # 14 we called for it expression
#
# print(x/y)
# z = ((x + y) /3)/3
# print(z)
# print(12 % 5)

# unary operator
# ++x , --y , ++++z
# z = 4
# z += +z
# print(z)
# print(x)
# x-=4

# power operators
# x = 5**3
# print(x)
# print(2.1**4)

# print(99 // 100.0)
# print(1500.0 // 99.0)

# Task
# num = 12345
# K -> remove last k numbers
# k=3 -> number result = 12
# remove 5,4,3
# num = 12345
# k = 3
# print(num // (10**k))

# multiple assignments
# x,y = 5,6
# print(x,y)

# x,y = y,x
# print(x,y)

# Boolean-> True=1 , False=0
# print(bool(0))      # False
# print(bool('0'))    # True
# print(bool(1))      # True
# print(bool(''))     # False
# print(bool(-5))     # True
# print(bool(5.5))    # True  
