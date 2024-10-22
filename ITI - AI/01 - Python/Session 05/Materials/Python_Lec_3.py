"""
function -> block of code
def -> define function

1- somthing is written and ready to use at any time
2- it saves everyone time
3- python provid built in function 
"""

# def helloFunc():
#     print("Hello")

# helloFunc()

# Parameter vs Argument
"""
Parameter: the var used in definig function
Argument: is an expression passed to the function when you call your function.
"""

# def fun1(fname,lname):
#     print("Hello: ")
#     print("Concate",fname+" "+lname)

# if __name__ == "__main__":
#     fun1("Mohamed", "Elgindy")
#     print("Hello")

# def sub(fnum,snum):
#     print("Subtract: ",fnum - snum)

# if __name__ == "__main__":
#     sub(9,4)

# return keyword
# return some result from our function
# def our_min(fnum, snum):
#     if fnum < snum:
#         print(fnum)
#     else:
#         print(snum)

# if __name__ == "__main__":
#     print(our_min(9,5))

# multiple return 
# def fun():
#     return 1,2,3


# a,b,c = fun()

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# creat function take start , end -> 5,10 -> 5,6,7,8,9,10
# def num(start , end):
#     for i in range(start,end+1):
#         print(i, end=" ")

# if __name__ =="__main__":
#     num(5,10)

# Global  variable, Local variable
"""
Global -> global variable is scope at anywhere within program
Local  -> local scope of a variable define in your function within the function only
local: is visible in function() but not outside function
"""

# globl = 20
# def fun():
#     locl = 30
#     print(locl) # 30
#     print(globl) # 20
#     return locl # 30

# print(fun())
# print(globl) # 20

# global var
# a = 5 
# b = 6

# def fun2():
#     a = b+1
#     print(a)
#     return a

# fun2()
# print(fun2())
# print(a)
# 7 7 7 5

# Name Binding
# def fun(x,*,y):
#     return x+y

# if __name__ == "__main__":
#     print(fun(5,y=4))

"""
Creating System Company
1- many of department
2- employees
3- each department has employee
"""
# class Employee:
#     name = None
#     salary = None
#     address = None

# if __name__ == "__main__":
#     emp = Employee()
#     emp.name = "Mohamed"
#     emp.salary = 1000
#     emp.address = "Mansoura"
#     print(emp.name)
#     print(emp.salary)
#     print( emp.address)

#     emp2 = Employee()
#     emp2.name = "Ahmed"
#     emp2.salary = 2000
#     emp2.address = "Giza"
#     print(emp2.name)
#     print(emp2.salary)
#     print( emp2.address)

# class Employee:
#     def __init__(self,name,salary,address):
#         self.name = name
#         self.salary = salary
#         self.address = address

# if __name__ == "__main__":
#     emp = Employee("Ahmed",2000,"Giza")
#     # print(emp)
#     print(emp.name)
#     print(emp.salary)
#     print( emp.address)



# class Employee:
#     name = None
#     salary = None
#     address = None

# def print_emp(obj):
#     print("Employee name:", obj.name)
#     print("Employee Salary:", obj.salary)
#     print("Employee Address:",obj.address)


# if __name__ == "__main__":
#     emp = Employee()
#     emp.name = "Mohamed"
#     emp.salary = 1000
#     emp.address = "Mansoura"
#     print_emp(emp)


# function with class
# class Employee:
#     name = None
#     salary = None
#     address = None

# def print_emp(obj):
#     print("Employee name:", obj.name)
#     print("Employee Salary:", obj.salary)
#     print("Employee Address:", obj.address)

# def read_emp():
#     obj = Employee()
#     obj.name = input("Enter Your name: ")
#     obj.salary = float(input("Enter yur salary: "))
#     obj.address = input("Enter yur Address: ")

#     return obj

# if __name__ == "__main__":
#     emp = read_emp()
#     print_emp(emp)



# method with class
# method it's function define inside class 
# class Employee:
#     name = None
#     salary = None
#     address = None

#     def print_emp(self):
#         print("Employee name:", self.name)
#         print("Employee Salary:", self.salary)
#         print("Employee Address:", self.address)

#     def read_emp(self):
#         self.name = input("Enter Your name: ")
#         self.salary = float(input("Enter yur salary: "))
#         self.address = input("Enter yur Address: ")

# if __name__ == "__main__":
#     emp = Employee()
#     emp.read_emp()
#     emp.print_emp()


"""
Encapsulation: 
is a grouping of variables and functions of specific concept in a single component named class
"""

# Constractor: -> init() -> initialization

# class Employee:
#     def __init__(self, name, salary, project):
#         # data members
#         self.nm = name
#         self.sal = salary
#         self.pr = project
        
#     def show(self):
#         print("Name is : ", self.nm, '\nSalary: ',self.sal)
        
#     def work(self):
#         print(self.nm, " is working on " , self.pr)

# emp = Employee("Mohamed", 1000, "Machine Learning")
# emp.show()
# emp.work()    

# class FullName:
#     def __init__(self, fName, lName):
#         # data members
#         self.firstName = fName
#         self.lastName = lName
        
# class Employee:
#     # use constructor of class inside another class
#     def __init__(self, first_name, last_name, salary, address):
#         self.full_name = FullName(first_name,last_name)
#         self.salary = salary
#         self.address = address
        
#     def print_emp(self):
#         print('Employee name: ', self.full_name.firstName + ' '+ self.full_name.lastName)
#         print('Employee Salary: ', self.salary)
#         print('Employee address: ', self.address)

# emp = Employee('Ahmed', 'Mohamed', 10000, 'Egypt')
# emp.print_emp()


# Polymorphism -> use function other ways
# print(len("Ahmed"))
# print(len([1,2,35,6,8,8,9,6,7]))

# class Rectangle:
#     def __init__(self, width, height):
#         self.w = width
#         self.h = height
        
#     def get_area(self):
#         return self.w * self.h
    
# class Circle:
#     def __init__(self, redius):
#         self.r = redius
        
#     def get_area(self):
#         from math import pi
#         return pi*self.r * self.r
    
# r = Rectangle(2,5)
# print(r.get_area())

# c = Circle(5)
# print(c.get_area())



# single inheritance
# class Person:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
    
#     def is_valid(self):
#         return self.email.endswith('@gmail.com')
    
#     def print_info(self):
#         print(self.name, self.email)

# class Student(Person):
#     def __init__(self,name,email):
#         Person.__init__(self,name,email) # call parent initialize
#         self.GPA = 4.0
#         self.studen_courses = ["Python", "AI"]

#     def print_info(self):
#         print(self.name, self.email, self.is_valid())

# if __name__ == "__main__":
#     st = Student("Ahmed","ahmed@gmail.com")
#     # st.print_info()
#     # print(st.email)
    
#     p = Person("Mohamed", "Mohamed@gmail.com")
#     p.print_info()
#     print(p.is_valid())

#     st.print_info()
#     print(st.email)






























