# n = int(input("Enter the matrix order: "))
# print("Enter the matrix elements:")
# elements = list(map(int, input().split()))
# matrix = []
# k = 0
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(elements[k])
#         k += 1
#     matrix.append(row)
# primary_sum = 0
# secondary_sum = 0
# for i in range(n):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[i][n - 1 - i]
# print("Sum of primary diagonal:", primary_sum)
# print("Sum of secondary diagonal:", secondary_sum)


# from abc import ABC, abstractmethod
# class Bank(ABC):
#     def __init__(self, balance):
#         self.balance = balance
#     @abstractmethod
#     def calculate_interest(self):
#         pass
# class SBI(Bank):
#     def calculate_interest(self):
#         interest = self.balance * 0.05
#         return interest
# class HDFC(Bank):
#     def calculate_interest(self):
#         interest = self.balance * 0.065
#         return interest
# class ICICI(Bank):
#     def calculate_interest(self):
#         interest = self.balance * 0.07
#         return interest
# balance = float(input("Enter account balance: "))
# sbi = SBI(balance)
# hdfc = HDFC(balance)
# icici = ICICI(balance)
# print("SBI Interest:", sbi.calculate_interest())
# print("HDFC Interest:", hdfc.calculate_interest())
# print("ICICI Interest:", icici.calculate_interest())


# n,m = map(int, input("Enter number of rows and columns: ").split())
# print("Enter the matrix elements:")
# elements = list(map(int, input().split()))
# matrix = []
# k = 0
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(elements[k])
#         k += 1
#     matrix.append(row)
# print("Matrix:")
# for row in matrix:
#     print(' '.join(map(str, row)))
# for row in matrix:
#     max_element=row[0]
#     for element in row:
#         if element>max_element:
#             max_element=element
#     print("Maximum element in the row:", max_element)


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# a,b=map(int,input().split())
# print("GCD is:",gcd(a,b))


# n=int(input("Enter a number: "))
# value=2
# print(value,end=",")
# for i in range(1,n):
#     value+=i*13
#     print(value,end="," if i<n-1 else "")


# n=int(input("Enter a number: "))
# series=[1,3]
# series.append(series[0]+series[1])
# for i in range(3,n):
#     next_value=series[i-1]+series[i-2]+series[i-3]
#     series.append(next_value)
# for i in series:
#     print(i,end=",")


# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, target, source)
# n = int(input("Enter the number of disks: "))
# tower_of_hanoi(n, 'A', 'C', 'B')


# n = int(input("Enter number of rows: "))
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(2 * i - 1):
#         print("*", end=" ")
#     print()
# for i in range(2, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(2 * i - 1):
#         print("*", end=" ")
#     print()


# imagien you are developing gym membership management when new user wants to join the gym they provide personal details and name and membership plan is input like monthly or yearly
# class Gym:
#     def __init__(self, name, plan):
#         self.name = name
#         self.plan = plan
#     def display_details(self):
#         print(f"Member Name: {self.name} selected {self.plan} membership plan.")
# name = input("Enter your name: ")
# plan = input("Enter membership plan (monthly/yearly): ")
# member = Gym(name, plan)
# member.display_details()


# n=input("Enter a character: ")
# if n in 'aeiouAEIOU':
#     print(f"{n} is a vowel.")
# elif n.isalpha():
#     print(f"{n} is a consonant.")
# else:
#     print("Invalid input.")


# investment,earnings=map(float,input("Enter investment and earnings: ").split())
# if investment<=0 or earnings<0:
#     print("Invalid amount.")
# else:
#     if earnings>investment:
#         print("Profit")
#         print(f"Profit Percentage: {((earnings - investment)/investment)*100:.2f}%")
#     elif earnings<investment:
#         print("Loss")
#         print(f"Loss Percentage: {((investment - earnings)/investment)*100:.2f}%")
#     else:
#         print("No Profit No Loss")
        

# input is  1 2 3 4 5 6 7 8 9 matrix of order 3 and output is 7 4 1 8 5 2 9 6 3 i.e, 90 degree rotation of matrix
# n = int(input("Enter the matrix order: "))
# print("Enter the matrix elements:")
# elements = list(map(int, input().split()))
# matrix = []
# k = 0
# for i in range(n):  
#     row = []
#     for j in range(n):
#         row.append(elements[k])
#         k += 1
#     matrix.append(row)
# for row in matrix:
#     print(' '.join(map(str, row)))
# rotated_matrix = []
# for j in range(n):
#     new_row = []
#     for i in range(n - 1, -1, -1):
#         new_row.append(matrix[i][j])
#     rotated_matrix.append(new_row)
# print("Rotated Matrix:")
# for row in rotated_matrix:
#     print(' '.join(map(str, row)))


# input is 4 5 10 20 30 40 50 15 10 5 0 -5 5 5 6 7 8 9 11 10 13 14, first two numbers are m (number of rows) and n (number of columns) for the next series of input and output should be number of rows with sorted in ascending order in this case : 10,20,30,40,50 sorted and 5 5 6 7 8 sorted remaining two rows not sorted and each have 5 coloumns
# Read all input in one line
# data = list(map(int, input().split()))
# m = data[0]
# n = data[1]
# values = data[2:]
# count = 0
# k = 0
# for i in range(m):
#     row = values[k:k+n]
#     k += n
#     if row == sorted(row):
#         count += 1
# print(count)


# input is string of seating arrangement like abcxyzgh and output is integer of correctly positioned in order i.e, 5
# seating = input("Enter the seating arrangement: ")
# correct_order = 'abcdefghijklmnopqrstuvwxyz'
# count = 0
# for i in range(min(len(seating), len(correct_order))):
#     if seating[i] == correct_order[i]:
#         count += 1
# print("Number of correctly positioned seats:", count)


# input is string s of server log like aaabbccddeeffggg, with max length of 50, output is compressed string in reverse order like gfedcba
# log = input("Enter the server log string: ")
# compressed = []
# i = 0
# while i < len(log):
#     count = 1
#     while i + 1 < len(log) and log[i] == log[i + 1]:
#         count += 1
#         i += 1
#     compressed.append(log[i])
#     i += 1
# compressed.reverse()
# print("".join(compressed))


# input is positive integer n and output is number of digits in number
# n = int(input("Enter a positive integer: "))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print("Number of digits:", count)


# input is integer n and output is count of set bits in binary representation of n
# def count_set_bits(n):
#     if n == 0:
#         return 0
#     return (n & 1) + count_set_bits(n >> 1)
# n = int(input("Enter an integer: "))
# print("Number of set bits:", count_set_bits(n))

# write a python program to demonstrate diff between class variable and instance variable
# class Car:
#     wheels = 4  # Class variable
#     def __init__(self, color, model):
#         self.color = color  # Instance variable
#         self.model = model  # Instance variable
# car1 = Car("Red", "Sedan")
# car2 = Car("Blue", "SUV")
# print(f"Car 1: Color={car1.color}, Model={car1.model}, Wheels={car1.wheels}")
# print(f"Car 2: Color={car2.color}, Model={car2.model}, Wheels={car2.wheels}")
# Car.wheels = 5
# print("After changing class variable:")
# print(f"Car 1: Color={car1.color}, Model={car1.model}, Wheels={car1.wheels}")
# print(f"Car 2: Color={car2.color}, Model={car2.model}, Wheels={car2.wheels}")


# implment a pythin program to demonstrate composition (HAS-A relationship)
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#     def start(self):
#         return "Engine started with horsepower: " + str(self.horsepower)
# class Car:
#     def __init__(self, color, model, engine):
#         self.color = color
#         self.model = model
#         self.engine = engine  # Car has an Engine
#     def start_car(self):
#         return self.engine.start()
# engine = Engine(150)
# car = Car("Red", "Sedan", engine)
# print(f"Car Model: {car.model}, Color: {car.color}")
# print(car.start_car())


# demonstrate run time polymorphism using the same method name in different class in python
# class Dog:
#     def sound(self):
#         return "Woof"
# class Cat:
#     def sound(self):
#         return "Meow"
# def animal_sound(animal):
#     print(animal.sound())
# dog = Dog()
# cat = Cat()
# animal_sound(dog)
# animal_sound(cat)


# n=10
# try:
#     result=n/0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


# try:
#     n=0
#     result=100/n
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid value provided.")
# else:
#     print("Result is:",result)
# finally:
#     print("Execution completed.")


# try:
#     x=int("str")
#     inv=1/x
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid value provided.")


# a=[10,"string",20]
# try:
#     total=int(a[0])+int(a[1])
#     print("Total is:",total)
# except (ValueError, TypeError) as e:
#     print("Error:",e)
# except IndexError:
#     print("Error: Index out of range.")


# atm allows user to withdraw money , it should fail if the amount is more than balance or if the amount is negative or if it is not a number
# class ATM:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         try:
#             amount = float(amount)
#             if amount <= 0:
#                 raise ValueError("Withdrawal amount must be positive.")
#             if amount > self.balance:
#                 raise ValueError("Insufficient balance.")
#             self.balance -= amount
#             print(f"Withdrawal successful. New balance: {self.balance}")
#         except ValueError as e:
#             print("Error:", e)
# atm=ATM(1000)
# amount=input("Enter amount to withdraw: ")
# atm.withdraw(amount)


# marks=int(input("Enter marks obtained: "))
# try:
#     if marks<0 or marks>100:
#         raise ValueError("Marks should be between 0 and 100.")
#     else:
#         print("Valid marks entered:",marks)
# except ValueError as e:
#     print("Error:",e)


# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# try:
#     # if a and b are non numeric
#     if a<0 or b<0:
#         raise ValueError("Numbers must be non-negative.")
#     if b==0:
#         raise ZeroDivisionError("Division by zero is not allowed.")
#     result=a/b
#     print("Result is:",result)
# except ZeroDivisionError as e:
#     print("Error:",e)
# except ValueError as e:
#     print("Error:",e)
    

# username="Dharaneesh"
# password="D@ra1234"
# uname=input("Enter username: ")
# pwd=input("Enter password: ")
# try:
#     if uname!=username or pwd!=password:
#         raise ValueError("Invalid credentials.")
#     print("Login successful.")
# except ValueError as e:
#     print("Error:",e)


# age=int(input("Enter your age: "))
# try:
#     if age<18:
#         raise ValueError("Invalid Age.")
#     print("Age Accepted.")
# except ValueError as e:
#     print("Error:",e)


# balance=int(input("Enter account balance: "))
# withdrawal_amount=int(input("Enter withdrawal amount: "))
# try:
#     if balance-withdrawal_amount<1000:
#         raise ValueError("Minimum balance violation.")
#     balance-=withdrawal_amount
#     print("Withdrawal successful. New balance:",balance)
# except ValueError as e:
#     print("Error:",e)
    
    
# input first line contains integer n which represents number of rows and coloumns of n *n grid and next n lines contains n space separated integers representing the grid elements. output is the sum of elements in each row and coloumn
# n=int(input("Enter the order of matrix: "))
# matrix=[]
# elements = list(map(int, input("Enter the matrix elements: ").split()))
# k = 0
# for i in range(n):  
#     row = []
#     for j in range(n):
#         row.append(elements[k])
#         k += 1
#     matrix.append(row)
# print("Matrix:")
# for row in matrix:
#     print(' '.join(map(str, row)))
# for i in range(n):
#     row_sum=sum(matrix[i])
#     print(f"Sum of row {i+1}: {row_sum}")
# col_sums = [0] * n
# for i in range(n):
#     for j in range(n):
#         col_sums[j] += matrix[i][j]
# for j in range(n):
#     print(f"Sum of column {j+1}: {col_sums[j]}")


# def set(age):
#     if age<0:
#         raise ValueError("Age cannot be negative.")
#     print(f"Age is set to: {age}")
# try:
#     age=int(input("Enter your age: "))
#     set(age)
# except ValueError as e:
#     print("Error:",e)

# def climb_stairs(n):
#     if n<=2:
#         return n
#     first, second = 1, 2
#     for _ in range(3, n + 1):
#         first, second = second, first + second
#     return second
# n = int(input("Enter the number of stairs: "))
# print("Number of ways to climb the stairs:", climb_stairs(n))


# amount=int(input("Enter the amount to withdraw: "))
# #withdrawal limit should be 25000 per day if it exceeds should raise exception
# try:
#     if amount>25000:
#         raise ValueError("Daily limit exceeded")
#     print("Withdrawal allowed: ",amount)
# except ValueError as e:
#     print("Error:",e)


# pin="2005"
# user_pin=input("Enter your pin: ")
# try:
#     if user_pin!=pin:
#         raise ValueError("Invalid PIN")
#     print("Access granted")
# except ValueError as e:
#     print("Error:",e)


# salary=int(input("Enter your salary: "))
# try:
#     if salary<=20000:
#         raise ValueError("Loan Rejected")
#     print("Loan Approved")
# except ValueError as e:
#     print("Error: ",e)


# class A:
#     def show(self):
#         print("show() from class A")
# class B(A):
#     def show(self):
#         print("show() from class B")
# class C(A):
#     def show(self):
#         print("show() from class C")
# class D(B, C):
#     pass
# obj = D()
# obj.show()
# print(D.mro())


# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)
#     def __sub__(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)
# c=ComplexNumber(3, 2)
# d=ComplexNumber(1, 7)
# e=c+d
# f=c-d
# print(f"Addition: {e.real} + {e.imag}i")
# print(f"Subtraction: {f.real} + {f.imag}i")


# class Student:
#     def __init__(self, sid, deptid):
#         self.__sid = sid
#         self.__deptid = deptid

#     def get_student_id(self):
#         return self.__sid

#     def get_dept_id(self):
#         return self.__deptid


# class Faculty:
#     def __init__(self, fid, deptid):
#         self.__fid = fid
#         self.__deptid = deptid

#     def get_faculty_id(self):
#         return self.__fid


# class PhDStudent(Student, Faculty):
#     def __init__(self, sid, deptid, fid):
#         Student.__init__(self, sid, deptid)
#         Faculty.__init__(self, fid, deptid)

#     def get_full_info(self):
#         return (
#             f" Student ID: {self.get_student_id()}\n "
#             f"Faculty ID: {self.get_faculty_id()}\n "
#             f"Department ID: {self.get_dept_id()}"
#         )
# p = PhDStudent("S123", "D001", "F456")
# print(p.get_full_info())


# class Employee:
#     def __init__(self, id, salary):
#         self.__id = id
#         self.__salary = salary


# class SalesEmployee(Employee):
#     def __init__(self, id, salary, sales, bonus, pf, advanced_amount, annual_income):
#         super().__init__(id, salary)
#         self.__sales = sales
#         self.__bonus = bonus
#         self.__pf = pf
#         self.__advanced_amount = advanced_amount
#         self.__annual_income = annual_income


# # -------- USER INPUT --------
# id = int(input("Enter employee id: "))
# salary = int(input("Enter salary: "))
# sales = int(input("Enter sales amount: "))
# bonus = int(input("Enter bonus: "))
# pf = int(input("Enter PF amount: "))
# advanced_amount = int(input("Enter advanced amount: "))
# annual_income = int(input("Enter annual income: "))

# se = SalesEmployee(id, salary, sales, bonus, pf, advanced_amount, annual_income)

# # -------- OUTPUT --------
# print("\nEmployee object dictionary:")
# print(se.__dict__)

# print("\nAccessing private variables using name mangling:")
# print(se._Employee__id)
# print(se._Employee__salary)
# print(se._SalesEmployee__sales)
# print(se._SalesEmployee__bonus)
# print(se._SalesEmployee__pf)
# print(se._SalesEmployee__advanced_amount)
# print(se._SalesEmployee__annual_income)


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     def __init__(self,c):
#         self.c=c
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#     def get_color(self):
#         return self.c
# class Sqaure(Shape):
#     def __init__(self,side,color):
#         super().__init__(color)
#         self.side=side
#     def get_area(self):
#         return self.side*self.side
#     def get_perimeter(self):
#         return 4*self.side
#     def natural(self,n):
#         for i in range(1,n+1):
#             print(i)
# s=Sqaure(5.0,"Red")
# print(s.get_area())
# print(s.get_color())
# print(s.get_perimeter())
# s.natural(10)


# class Student:
#     def __init__(self, name, age, dl_number,
#                  english, telugu, maths, science, social):
#         self.name = name
#         self.age = age
#         self.dl_number = dl_number
#         self.english = english
#         self.telugu = telugu
#         self.maths = maths
#         self.science = science
#         self.social = social
#     def get_age(self):
#         return self.age
#     def set_age(self, age):
#         if age >= 5 and age <= 100:
#             self.age = age
#         else:
#             print("Invalid age")
#     def get_dl_number(self):
#         return self.dl_number
#     def set_dl_number(self, dl):
#         if len(dl) >= 5:
#             self.dl_number = dl
#         else:
#             print("Invalid DL number")
#     def get_english(self):
#         return self.english
#     def set_english(self, marks):
#         if 0 <= marks <= 100:
#             self.english = marks
#         else:
#             print("Invalid English marks")
#     def get_telugu(self):
#         return self.telugu
#     def set_telugu(self, marks):
#         if 0 <= marks <= 100:
#             self.telugu = marks
#         else:
#             print("Invalid Telugu marks")
#     def get_maths(self):
#         return self.maths
#     def set_maths(self, marks):
#         if 0 <= marks <= 100:
#             self.maths = marks
#         else:
#             print("Invalid Maths marks")
#     def get_science(self):
#         return self.science
#     def set_science(self, marks):
#         if 0 <= marks <= 100:
#             self.science = marks
#         else:
#             print("Invalid Science marks")
#     def get_social(self):
#         return self.social
#     def set_social(self, marks):
#         if 0 <= marks <= 100:
#             self.social = marks
#         else:
#             print("Invalid Social marks")
# s = Student("John", 25, "DL12345", 80, 75, 90, 85, 88)
# print("Maths marks:", s.get_maths())
# s.set_maths(95)
# print("Updated Maths:", s.get_maths())
# s.set_age(150)       
# s.set_english(105)    


# class Student:
#     def __init__(self, name, marks, DL):
#         self.__name = name
#         self.__marks = marks
#         self.__DL = DL

#     def get_name(self):
#         return self.__name

#     def set_name(self, value):
#         self.__name = value

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, value):
#         if value < 0 or value > 100:
#             print("Invalid marks")
#         else:
#             self.__marks = value

#     def get_DL(self):
#         return self.__DL

#     def set_DL(self, value):
#         self.__DL = value
# s= Student("Rahul", 85, "DL123")
# print(s.get_name())
# s.set_name("Amit")
# print(s.get_name())
# print(s.get_marks())
# s.set_marks(92)
# print(s.get_marks())
# s.set_marks(150)
# print(s.get_DL())
# s.set_DL("DL456")
# print(s.get_DL()) 


# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#  def __init__(self,brand):
#      self._brand=brand
#  @abstractmethod
#  def start(self):
#      pass
#  @abstractmethod
#  def fuel_type(self):
#      pass
# class Car(Vehicle):
#  def start(self):
#      print(self._brand+" car starting")
#  def fuel_type(self):
#      return"Petrol"
# class Bike(Vehicle):
#  def start(self):
#      print(self._brand+" bike starting")
#  def fuel_type(self):
#      return"Petrol"
# class ElectricCar(Vehicle):
#  def start(self):
#      print(self._brand+" electric car starting")
#  def fuel_type(self):
#      return"Electric"
# def vehicle_info(v):
#  v.start()
#  print(v.fuel_type())
# v1=Car("Toyota")
# v2=Bike("Yamaha")
# v3=ElectricCar("Tesla")
# vehicle_info(v1)
# vehicle_info(v2)
# vehicle_info(v3)


# input is n with number of rows in pyramid and output is 1 23 456 78910 1112131415 i.e, each row the numbers should be in order and the same quantity of row number
# n=int(input("Enter number of rows: "))
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end="")
#         num += 1
#     print(" ",end="")


# N, K = map(int, input("Enter N and K: ").split())
# types = list(map(int, input("Enter types of chocolates: ").split()))
# prices = list(map(int, input("Enter prices of chocolates: ").split()))
# chocolate_dict = {}
# for i in range(N):
#     t = types[i]
#     p = prices[i]
#     if t not in chocolate_dict:
#         chocolate_dict[t] = p
#     else:
#         chocolate_dict[t] = min(chocolate_dict[t], p)
# if len(chocolate_dict) < K:
#     print(-1)
# else:
#     sorted_prices = sorted(chocolate_dict.values())
#     print(sum(sorted_prices[:K]))


# username="admin"
# password="Admin@123"
# uname=input("Enter username: ")
# pwd=input("Enter password: ")
# balance=int(input("Enter account balance: "))
# withdrawal_amount=int(input("Enter withdrawal amount: "))
# try:
#     if uname!=username or pwd!=password:
#         raise ValueError("Authentication Failed")
#     print("Authentication Successful")
#     if balance-withdrawal_amount<0:
#         raise ValueError("Insufficient balance.")
#     balance-=withdrawal_amount
#     print("Withdrawal successful")
# except ValueError as e:
#     print("Error:",e)
# finally:
#     print("Session Closed")


# card_number="1234-5678-9012-3456"
# balance=10000
# #use nested try except to validate card number and payment failure seperately, input has balance and amount to pay
# try:
#     try:
#         user_card=input("Enter card number: ")
#         if user_card!=card_number:
#             raise ValueError("Invalid Card Number")
#         print("Card Validated")
#         amount_to_pay=int(input("Enter amount to pay: "))
#         if amount_to_pay>balance:
#             raise ValueError("Payment Failed: Insufficient Balance")
#         balance-=amount_to_pay
#         print("Payment Successful. Remaining Balance:",balance)
#     except ValueError as e:
#         print("Error:",e)
# except Exception as e:
#     print("An unexpected error occurred:",e)


# create custom exception class that accepts an error message, input is single line salary and credit_score, if salary<25000 or credit_score<700 raise seperate exceptions low credit score and low salary if not then Loan approved
# class LowSalaryError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
# class LowCreditScoreError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
# salary, credit_score = map(int, input("Enter salary and credit score: ").split())
# try:
#     if salary < 25000:
#         raise LowSalaryError("Low Salary")
#     if credit_score < 700:
#         raise LowCreditScoreError("Low Credit Score")
#     print("Loan Approved")
# except (LowSalaryError, LowCreditScoreError) as e:
#     print("Error:", e.message)


# s=input("Enter a string: ")
# l=len(s)
# c=input("Enter a character: ")
# count=0
# for i in s:
#     if i==c:
#         count+=1
# print(count)


# s=input("Enter a string: ")
# string=list(s)
# c=input("Enter a character: ")
# for i in s:
#     if i==c:
#         string.remove(i)
# new_string="".join(string)
# print(new_string)


# import json
# f=open("/Users/dharaneeshkuruba/Desktop/Capgemini/test.txt","r")
# cont=f.read()
# print(cont)


# created=open("test.txt","w")
# print(open("test.txt").read()==False)


# file=open("test.txt","r")
# file.close()


# file=open("test.txt","r")
# file.close()
# print("Is closed?",file.closed)
# print("File name is:",file.name)
# print("File mode is:",file.mode)


# file=open("test.txt","w")
# file.write("Hello World")
# file.close()


# file=open("test.txt","r")
# content=file.read()
# print(content)
# file.close()


# with open("test.txt","r") as file:
#     content=file.read()
#     print(content)
    

# with open("test.txt","a") as file:
#     file.write("\nWelcome to Capgemini")


# with open("test.txt","r") as file:
#     for line in file:
#         print(line.strip())


# file=open("test.txt","r")
# line=file.readline()
# while line:
#     print(line.strip())
#     line=file.readline()
# file.close()


# file=open("img.jpg","rb")
# data=file.read()
# print(data)
# file.close()


# file=open("test.txt","r")
# content=file.read(10)
# print(content)
# file.close()


# import csv
# import io
# csv_data="""Name,Age,Department
# Alice,30,HR
# Bob,25,Engineering
# Charlie,28,Marketing
# """
# csvfile=io.StringIO(csv_data)
# csvreader=csv.reader(csvfile)
# for row in csvreader:
#     print(row)
# csvfile.close()


# import json
# with open("data.json","w") as file:
#     json.dump({"name":"Dharaneesh","age":24},file)
# with open("data.json","r") as file:
#     data=json.load(file)
#     print(data)


# with open("test.txt","w",encoding="utf-8") as file:
#     file.write("This is a test file.")
#     file.write("\nIt contains multiple lines.")
# with open("test.txt","r",encoding="utf-8") as file:
#     content=file.read()
#     print(content)


# with open("test.txt","a") as file:
#     file.write("\nAppending a new line to the file.")
# with open("test.txt","r") as file:
#     content=file.read()
#     print(content)


# try:
#     with open("test.txt","x",encoding="utf-8") as file:
#         file.write("This file is created using 'x' mode.")
# except FileExistsError:
#     print("File already exists.")


# lines=["Line A","Line B","Line C"]
# text="\n".join(lines)+"\n"
# with open("test.txt","w",encoding="utf-8") as file:
#     file.write(text)
# with open("test.txt","r",encoding="utf-8") as file:
#     content=file.read()
#     print(content)


# data=b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21'
# with open("output.bin","wb") as file:
#     file.write(data)


# try:
#     file=open("test.txt","r")
#     content=file.read()
#     print(content)
# finally:
#     file.close()


# re raising exception in account closure scenario
# class AccountClosureError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
# def close_account(balance):
#     try:
#         if balance > 0:
#             raise AccountClosureError("Account has pending balance")
#         print("Account closed")
#     except AccountClosureError as e:
#         print("Error:", e.message)
#         raise
# try:
#     balance = float(input("Enter account balance: "))
#     close_account(balance)
# except AccountClosureError:
#     print("Please withdraw remaining balance before closing the account")


# student_id=input("enter the student id: ")
# try:
#     if len(student_id)<6 or not student_id.isdigit() or len(student_id)>6:
#         raise Exception("Invalid Student ID")
#     print("logged in successfully")
# except Exception as e:
#     print("Error: ",e)


# class InsufficientSeatsError(Exception):
#     pass
# def book_ticket(username, requested, available):
#     if requested <= 0:
#         raise ValueError("Number of tickets must be a positive integer")
#     if requested > available:
#         raise InsufficientSeatsError("Requested tickets exceed available seats")
#     available -= requested
#     print(f"Booking successful for {username}")
#     print(f"Tickets booked: {requested}")
#     print(f"Remaining seats: {available}")
#     return available
# try:
#     username = input("Enter user name: ")
#     requested = int(input("Enter number of tickets requested: "))
#     available = int(input("Enter available seats: "))
#     available = book_ticket(username, requested, available)
# except ValueError as e:
#     print("Invalid input:", e)
# except InsufficientSeatsError as e:
#     print("Booking failed:", e)
# except Exception as e:
#     print("Unexpected error:", e)


# trails=int(input("enter number of trails: "))
# trail_size=list(map(int, input("enter the size of each trail: ").split()))
# print(max(trail_size))


# n = int(input("Enter the length of array: "))
# arr = list(map(int, input("Enter the numbers: ").split()))
# unique = sorted(set(arr))
# if len(unique) < 2:
#     print(0)
# else:
#     second_largest = unique[-2]
#     print(arr.count(second_largest))


# n=int(input("enter the length of array: "))
# arr=list(map(int,input("enter the numbers: ").split()))
# i=0
# j=1
# while j<len(arr):
#     res=arr[j]-arr[i]
#     i+=1
#     j+=1
#     print(res)


# n = int(input("enter the number of students: "))
# MOD = 10007
# total = 0
# for i in range(1, n + 1):
#     x = i
#     while x % 2 == 0:
#         x //= 2
#     total = (total + x) % MOD
# print(total)


# n=int(input("number of printing jobs: "))
# w=int(input("enter time duration for the next job to enter: "))
# time=(n-1)*10
# wait=(n-1)*w
# print(time-wait)


# r=int(input("enter the radius: "))
# h=int(input("enter the height: "))
# water=3.14*r*r*h
# print(round(water))


# name=input("enter the person name: ")
# course=int(input("enter number of courses selected: "))
# max_allowed=5
# try:
#     if course>max_allowed:
#         raise Exception("Course limit exceeded")
#     print("Enrollment process completed")
# except Exception as e:
#     print("Error: ",e)


# def fun(n):
#     if n==0:
#         return 1
#     return 2*fun(n-1)
# n=int(input("enter the number: "))
# res=fun(n)
# print(f"the value is: {res}")


# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input("enter n: "))
# for i in range(n):
#     print(fib(i),end=" ")


# def array_sum(arr, n):
#     if n == 0:
#         return 0
#     return arr[n-1] + array_sum(arr, n-1)
# arr = list(map(int, input("Enter array elements: ").split()))
# print("Sum:", array_sum(arr, len(arr)))


# def count_alnum(s, i=0):
#     if i == len(s):
#         return -1
#     return (1 if s[i].isalnum() else 0) + count_alnum(s, i+1)
# s = input("Enter a string: ")
# print("Alphanumeric count:", count_alnum(s))


# s=input("enter the string: ")
# result=""
# word=""
# for ch in s:
#     if ch!=" ":
#         word+=ch
#     else:
#         result=word+" "+result
#         word=""
# result=word+" "+result if result else word
# print(result.strip())


# n = int(input("Enter n: "))
# elements = list(map(int, input().split()))
# matrix = []
# k = 0
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(elements[k])
#         k += 1
#     matrix.append(row)
# is_upper = True
# for i in range(n):
#     for j in range(i):
#         if matrix[i][j] != 0:
#             is_upper = False
#             break
# if is_upper:
#     print("upper triangular matrix")
# else:
#     print("not upper triangular matrix")


# n=int(input("enter n: "))
# elements=list(map(int,input().split()))
# k=0
# matrix=[]
# for i in range(n):
#     row=[]
#     for j in range(n):
#         row.append(elements[k])
#         k+=1
#     matrix.append(row)
# for i in range(n):
#     for j in range(n-1, -1, -1):
#         print(matrix[i][j], end=" ")
#     print()


# n=int(input("enter the number of houses: "))
# print(f"enter stairs for {n} houses: ")
# val=list(map(int,input().split()))
# count=0
# for i in val:
#     if i%3==0:
#         count+=1
# print(count)


# h=int(input("enter height: "))
# v=int(input("enter initail velocity: "))
# vn=int(input("enter final velocity: "))
# print("rebound height is: ", h*(v/vn)*(v/vn))


# import numpy as np
# a1=np.array([1,2,3])
# a2=np.array([[1,2],[3,4]])
# a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a1)
# print(a2)
# print(a3)


# import numpy as np
# a0=np.zeros([3,3])
# a1=np.ones([2,2])
# a2=np.arange(0,10,2)
# print(a0)
# print(a1)
# print(a2)


# import numpy as np
# a1=np.array([10,20,30,40,50])
# print(a1[2])
# print(a1[-1])
# a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a2[1,0])
# print(a2)


# import numpy as np
# a=np.array([10,20,30,40,50])
# idx=np.array([1,3,4])
# print(a[idx])
# cond=a>30
# print(a[cond])


# import numpy as np
# x=np.array([1,2,3])
# y=np.array([4,5,6])
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)


# import numpy as np
# a=np.array([-3,-1,0,1,3])
# print(np.absolute(a))


# import numpy as np
# x=np.array([1,2,3])
# y=np.array([4,5,6])
# res=np.add(x,y)
# print(res)


# import numpy as np
# a=np.array([0,np.pi/2,np.pi])
# print(np.sin(a))
# b=np.array([0,1,2,3])
# print(np.exp(b))
# print(np.sqrt(b))
# print(np.sqrt(a))

# import numpy as np
# dtype = [('name', 'U10'), ('year', int), ('cgpa', float)]
# vals = [
#     ('Hrithik', 2009, 8.5),
#     ('Ajay', 2008, 7.9),
#     ('Adarsh', 2009, 9.0)
# ]
# a = np.array(vals, dtype=dtype)
# print(np.sort(a, order='name'))
# print(np.sort(a, order=['year', 'cgpa']))


# import numpy as np
# zeros_array = np.zeros((2,3))
# ones_array = np.ones((3,3))
# constant_array = np.full((2,2), 7)
# range_array = np.arange(0, 10, 2)
# linspace_array = np.linspace(0, 1, 5)
# print("Zeros array:")
# print(zeros_array)
# print("\nOnes array:")
# print(ones_array)
# print("\nConstant array:")
# print(constant_array)
# print("\nRange array:")
# print(range_array)
# print("\nLinspace array:")
# print(linspace_array)


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import binom
# n=10
# p=0.5
# size=1000
# data=np.random.binomial(n,p,size)
# plt.hist(data,bins=np.arange(-0.5,n+1.5,1),density=True,edgecolor='black',alpha=0.7,label='Histogram')
# x=np.arange(0,n+1)
# pmf=binom.pmf(x,n,p)
# plt.scatter(x,pmf,color='red',label='Theoretical PMF')
# plt.vlines(x,0,pmf,colors='red',linestyles='dashed')
# plt.title("Binomial Distribution (n=10,p=0;5)")
# plt.xlabel("number of successes")
# plt.ylabel("probability")
# plt.legend()
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt
# x=[0,1,2,3,4]
# y=[0,1,4,9,16]
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as plt
# x=[0,2,4,6,8]
# y=[0,4,16,36,64]
# fig,ax=plt.subplots()
# ax.plot(x,y,marker='o',label="Data Points")
# ax.set_title("Basic components of Matplotlib figure")
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7]
# y=[1,2,1,2,1,2,1]
# y_error=0.2
# plt.plot(x,y)
# plt.errorbar(x,y,yerr=y_error,fmt='o')
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7]
# y=[1,2,1,2,1,2,1]
# x_error=0.5
# plt.plot(x,y)
# plt.errorbar(x,y,xerr=x_error,fmt='o')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# days=['Mon','Tue','Wed','Thu','Fri']
# temperature=[22,24,23,26,25]
# plt.plot(days,temperature,marker='o')
# plt.title('Weekly temperature')
# plt.xlabel('Days')
# plt.ylabel('Temperature(C)')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4])
# y=x*2
# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-label")
# plt.title("Simple line plot with labels")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4,5])
# y=[3,6,9,12,15]
# plt.plot(x,y,marker='o',linestyle='-',label='Data Points')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line plot with markers")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.plot(x,y)
# plt.grid(True)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line plot with grid")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# fruits=['Aplles','Bananas','Cherries','Dates']
# sales=[400,350,300,450]
# plt.bar(fruits,sales)
# plt.title("Fruits Sales")
# plt.xlabel("fruits")
# plt.ylabel("sales")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# fruits=['Aplles','Bananas','Cherries','Dates']
# sales=[400,350,300,450]
# plt.barh(fruits,sales)
# plt.title("Fruits Sales")
# plt.xlabel("fruits")
# plt.ylabel("sales")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# N=5
# boys=[20,35,30,35,27]
# girls=[25,32,34,20,25]
# boyStd=(2,3,4,1,2)
# girlStd=(3,5,2,3,3)
# ind=np.arange(N)
# width=0.35
# fig=plt.subplots(figsize=(10,7))
# p1=plt.bar(ind,boys,width,yerr=boyStd)
# p2=plt.bar(ind,boys,width,bottom=boys,yerr=girlStd)
# plt.ylabel('Contribution')
# plt.title('Contribution by the teams')
# plt.xticks(ind,('T1','T2','T3','T4','T5'))
# plt.yticks(np.arange(0,81,10))
# plt.legend((p1[0],p2[0]),('boys','girls'))
# plt.show()


# data=np.random.randn(1000)
# plt.hist(data,bins=30,color='skyblue',edgecolor='black')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Basic Histogram')
# plt.show()


# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter
# np.random.seed(23685752)
# N_points=10000
# n_bins=20
# x=np.random.randn(N_points)
# y=0.8**x+np.random.randn(N_points)+25
# legend=['Distribution']
# fig,axs=plt.subplots(1,1,figsize=(10,7),tight_layout=True)
# for s in ['top','bottom','left','right']:
#     axs.spines[s].set_visible(False)
# axs.xaxis.set_ticks_position('none')
# axs.yaxis.set_ticks_position('none')
# axs.xaxis.set_tick_params(pad=5)
# axs.yaxis.set_tick_params(pad=10)
# axs.grid(visible=True,color='grey',linestyle='-.',linewidth=0.5,alpha=0.6)
# fig.text(0.9,0.15,'Jeeteshgavande30',fontsize=12,color='red',ha='right',va='bottom',alpha=0.7)
# N,bins,patches=axs.hist(x,bins=n_bins)
# fracs=((N**(1/5))/N.max())
# norm=colors.Normalize(fracs.min(),fracs.max())
# for thisfrac,thispatch in zip(fracs,patches):
#     color=plt.cm.viridis(norm(thisfrac))
#     thispatch.set_facecolor(color)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend(legend)
# plt.title('Customized histogram with Watermark')
# plt.show()


# import seaborn as sns
# sns.set(style="white")
# rs=np.random.RandomState(10)
# d=rs.normal(size=100)
# sns.histplot(d,kde=True,color="m")
# plt.show()


# sns.set(style="dark")
# fmri=sns.load_dataset("fmri")
# sns.lineplot(x="timepoint",y="signal",hue="region",style="event",data=fmri)
# plt.show()


# x=['sun','mon','fri','sat','tue','wed','thu']
# y=[5,6.7,4,6,2,4.9,1.8]
# ax=sns.stripplot(x=x,y=y)
# ax.set(xlabel="Days",ylabel="Amount spent")
# plt.title("Daily spending(customer data)")
# plt.show()


# sns.set(style="whitegrid")
# iris=sns.load_dataset("iris")
# sns.swarmplot(x="species",y="sepal_length",data=iris)
# plt.title("Swarm plot of sepal length by species")
# plt.show()


# tips=sns.load_dataset("tips")
# sns.countplot(x="sex",data=tips)
# plt.title("Count of gender in dataset")
# plt.show()


# tips = sns.load_dataset("tips")
# sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
# plt.title("total bill distribution by day and smoking status")
# plt.show()


# tips = sns.load_dataset("tips")
# sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
# plt.title("violin plot of total bill by day and calendar)
# plt.show()



# tips = sns.load_dataset("tips")
# sns.stripplot(x="day", y="total_bill", data=tips,jitter=True, hue="smoker", dodge=True)
# plt.title("Total bill distribution with smoking status")
# plt.show()


# plt.plot([0,1],[10,11],label="line 1")
# plt.plot([0,1],[11,10],label="line 2")
# plt.scatter([0,1],[10.5,10.5],color='blue',marker='o',label='Dots')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line and dot plot")
# plt.legend()
# plt.show()


# sns.set_theme(style="darkgrid")
# x=[1,2,3,4,5]
# y=[10,12,15,18,22]
# plt.plot(x,y,marker='o',linestyle='-',color='blue',label='Trend')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Matplotlib plot with seaborn theme")
# plt.legend()
# plt.show()


# data=np.random.randn(1000)
# plt.figure(figsize=(8,5))
# sns.histplot(data,kde=True,bins=30,color='purple')
# mean_value=np.mean(data)
# plt.axvline(mean_value,color='red',linestyle='dashed',linewidth=2)
# plt.text(mean_value+0.1,50,f'Mean:{mean_value:.2f}',color='red')
# plt.title("Distribution with seaborn and matplotlib customization")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


# import pandas as pd
# s=pd.Series()
# print("panda series: ",s)
# data=np.array(['g','e','e','k','s'])
# s=pd.Series(data)
# print("panda series:\n ",s)


# df=pd.DataFrame()
# print(df)
# lst=['she','will','not','use','the','portal']
# df=pd.DataFrame(lst)
# print(df)


# df=pd.read_csv("data-.csv")
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# df=df.fillna(0)
# ages=df[df['age']>25]
# print(ages)
# df['total']=df['a']+df['b']
# print(df.head())


# import unittest

# def sqaure(n):
#     return n*n
# class TestSquare(unittest.TestCase):
#     def TestSquare(self):
#         self.assertEqual(sqaure(2),4)
# unittest.main()


# class TestDemo(unittest.TestCase):
#     def setUp(self):
#         self.a=10
#         self.b=5
#     def test_add(self):
#         self.assertEqual(self.a+self.b,15)
#     def tearDown(self):
#         pass
# unittest.main()


# def withdraw(balance,amount):
#     if amount>balance:
#         raise ValueError("insufficient balance")
#     return balance-amount
# def test_expectation(self):
#     with self.assetRaises(ValueError):
#         withdraw(100,200)
        
        
# class Bank:
#     def deposit(self,amt):
#         return amt
# class TestBank(unittest.TestCase):
#     def test_deposit(self):
#         bank=Bank()
#         self.assertEqual(bank.deposit(1000),1000)
# @unittest.skip("Feature not ready")
# def test_future(self):
#     pass
# unittest.main()


# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#     def test_strip(self):
#         s='jayamamam'
#         self.assertEqual(s.strip('jaya'), 'jayanan')
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)
# if __name__ == '__main__':
#     unittest.main()


# class Widget:
#     def __init__(self, name):
#         self.name = name
#     def size(self):
#         return (50, 50)
# class DefaultWidgetSizeTestCase(unittest.TestCase):
#     def test_default_widget_size(self):
#         widget = Widget('The widget')
#         self.assertEqual(widget.size(), (50, 50))
# if __name__ == '__main__':
#     unittest.main()


# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget=Widget('The widget')
#     def tearDown(self):
#         self.widget.dispose()
# if __name__ == '__main__':
#     unittest.main()


# def suite():
#     suite=unittest.TestSuite()
#     suite.addTest(WidgetTestCase('test_default_widget_size'))
#     suite.addTest(WidgetTestCase('test_widget_resize'))
#     return suite
# if __name__=="__main__":
#     runner=unittest.TextTestRunner()
#     runner.run(suite())


# def tower_of_hanoi(n, source, auxiliary, destination):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return
#     tower_of_hanoi(n-1, source, destination, auxiliary)
#     print(f"Move disk {n} from {source} to {destination}")
#     tower_of_hanoi(n-1, auxiliary, source, destination)
# n=int(input("enter number of disks: "))
# tower_of_hanoi(n, 'A', 'B', 'C')


# class WidgetTestCase(unittest.TestCase):
#     def test_default_widget_size(self):
#         self.assertEqual(1, 1)
#     def test_widget_resize(self):
#         self.assertTrue(True)
# def suite():
#     suite=unittest.TestSuite()
#     suite.addTest(WidgetTestCase('test_default_widget_size'))
#     suite.addTest(WidgetTestCase('test_widget_resize'))
#     return suite
# if __name__=="__main__":
#     runner=unittest.TextTestRunner()
#     runner.run(suite())


# class Widget:
#     def __init__(self):
#         self.width=50
#         self.height=50
#     def resize(self,width,height):
#         self.width=width
#         self.height=height
# class WidgetTestCase(unittest.TestCase):
#     def test_default_widget_size(self):
#         widget=Widget()
#         self.assertEqual(widget.width,50)
#         self.assertEqual(widget.height,50)
#     def test_widget_resize(self):
#         widget=Widget()
#         widget.resize(100,150)
#         self.assertEqual(widget.width,50)
#         self.assertEqual(widget.height,50)
# if __name__=='__main__':
#     unittest.main()


# import sys
# import mylib
# class Mytest(unittest.TestCase):
#     @unittest.skip("demonstrating skip")
#     def test_not(self):
#         self.fail("shouldn't happen")
#     @unittest.skipIf(mylib.__version__<(1,3),"not supported")
#     def test_for(self):
#         pass
#     @unittest.skipUnless(sys.platform.startwith("win"),"require windows")
#     def test_win(self):
#         pass
#     def test_may(self):
#         if not external_resource_available():
#             self.skipTest("external resource not available")
#         pass
# @unittest.skip("showing class skip")
# class MyskippedTestClass(unittest.TestCase):
#     def test_not_run(self):
#         pass
# class ExpectedFailureTestCase(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_fail(self):
#         self.assertEqual(1,0,'broken')
#     def skipunlesshasattr(obj,attr):
#         if hasattr(obj,attr):
#             return lambda func:func
#         return unittest.skip("{lr} doesn't have {lr}".format(obj,attr))
# if __name__=='__main__':
#     unittest.main()


# class NumbersTest(unittest.TestCase):
#     def test_even(self):
#         for i in range(0,6):
#             with self.subTest(i=i):
#                 self.assertEqual(i%2,0)
# unittest.main()     


# def square(n):
#     return n*n
# class TestSquare(unittest.TestCase):
#     def test_square_values(self):
#         test_data=[
#             (2,4),
#             (3,9),
#             (4,16),
#             (5,25)
#         ]
#         for num,expected in test_data:
#             with self.subTest(num=num):
#                 self.assertEqual(square(num),expected)
# unittest.main()


# class TestStringLength(unittest.TestCase):
#     def test_len(self):
#         strings={
#             "apple":5,
#             "banana":4,
#             "cat":3
#         }
#         for text,length in strings.items():
#             with self.subTest(string=text):
#                 self.assertEqual(len(text),length)
# unittest.main()


# class TestFloatValues(unittest.TestCase):
#     def test_float_values(self):
#         values = {
#             1.5: 1.5,
#             2.0: 2.0,
#             -3.25: -3.25,
#             0.1 + 0.2: 0.3
#         }
#         for value, expected in values.items():
#             with self.subTest(value=value):
#                 self.assertAlmostEqual(value, expected, places=7)
# if __name__ == '__main__':
#     unittest.main()


# def is_valid(pwd):
#     return len(pwd)>=8
# class TestPwd(unittest.TestCase):
#     def test_pwd(self):
#         passwords=[
#             ("password123",True),
#             ("abc",False),
#             ("welcome122",True),
#             ("12345",False)
#         ]
#         for pwd,excepted in passwords:
#             with self.subTest(password=pwd):
#                 self.assertEqual(is_valid(pwd),excepted)
# unittest.main()


# def divide(a,b):
#     if b==0:
#         raise ValueError("Division by 0")
#     return a/b
# class TestDivide(unittest.TestCase):
#     def test_division(self):
#         test_cases=[
#             (10,2,5),
#             (20,4,5)
#         ]
#         for a,b,result in test_cases:
#             with self.subTest(a=a,b=b):
#                 self.assertEqual(divide(a,b),result)
#     def test_divide_by_zero(self):
#         for b in [0]:
#             with self.subTest(b=b):
#                 self.assertRaises(ValueError,divide,10,b)
# unittest.main()


# def add(a,b):
#     return a+b
# class Add(unittest.TestCase):
#     def test_add_pos(self):
#         self.assertEqual(add(1,2),3)
#     def test_add_neg(self):
#         self.assertEqual(add(-1,-2),-3)
#     def test_add_mix(self):
#         self.assertEqual(add(1,-2),-1)
#         self.assertEqual(add(-1,2),1)
# unittest.main()


# def is_even(number):
#     return number%2==0
# class Even(unittest.TestCase):
#     def test_even(self):
#         self.assertTrue(is_even(4))
#     def test_odd(self):
#         self.assertFalse(is_even(7))
#     def test_zero(self):
#         self.assertTrue(is_even(0))
# unittest.main()