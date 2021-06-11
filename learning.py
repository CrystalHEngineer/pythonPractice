# print("Hello World!")
# print("this is a sample string")

# name = "Zen"
# print("My name is", name)
# print("My name is " + name)

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# print("My name is {} {} and I am {} years old".format(first_name, last_name, age))

# hw = "Hell0 %s" % "world"
# py = "I love Python %d" % 3
# print(hw, py)

# x = "hello world"
# print(x.title())

# x = 10
# if x > 50:
#     print("bigger than 50")
# else: 
#     print("smaller than 50")

# # dog = ('Bruce', 'cocker spaniel', 19, False)
# # print(dog[0])
# # dog[1] = 'dashshund'

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2])
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)
# ninjas.pop()
# print(ninjas)
# ninjas.pop(1)
# print(ninjas)

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')
# print(w)
# # output: 160.2
# print(new_person)
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# print(type(2.63))
# # output: <class 'float'>
# print(type(new_person))
# # output: <class 'dict'>

# print(len(new_person))
# # output: 4
# print(len('Coding Dojo'))
# # output: 11

# print("Hello " + str(42))
# # output: Hello 42

# total = 35
# user_val = "26"
# total = total + int(user_val)
# print(total)
# # output: 61

# x = 12
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")
# # output: smaller than 50

# x = 55
# if x > 10:
#     print("bigger than 10")
# elif x > 50:
#     print("bigger than 50")
# else: 
#     print("smaller than 10")
# # output: bigger than 10

# for x in range(0, 10, 2):
#     print(x)
#     # output: 0, 2, 4, 6, 8
# for x in range(5, 1, -3):
#     print(x)
#     # output: 5, 2

# my_list = ["abc", 123, "xyz"]
# for i in range( 0, len(my_list)):
#     print(i, my_list[i])
#     # output: 0 abc, 1 123, 2 xyz

# for v in my_list:
#     print(v)
#     # output: abc, 123, xyz

# my_dict = {"name": "Noelle", "language": "Python"}
# for k in my_dict:
#     print(k)

#     # output: name, Noelle

#     print(my_dict[k]) 

#     # output: language, Python

# for key in my_dict.keys():
#     print(key)
#     # output: name, language

# for val in my_dict.values():
#     print(val)
#     # output: Noelle, Python

# for key, val in my_dict.items():
#     print(key, " = ", val)
#     # output: name  =  Noelle
#     # language  =  Python

# for count in range(0,5):
#     print("looping -", count)
# #     output: looping - 0
# # looping - 1
# # looping - 2
# # looping - 3
# # looping - 4

# # rewritten as a while loop: 
# count = 0
# while count < 5:
#     print("looping -", count)
#     count += 1
# #     output: 
# #     looping - 0
# # looping - 1
# # looping - 2
# # looping - 3
# # looping - 4

# y = 3 
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")
# # output: 3
# # 2
# # 1
# # Final else statement

# for val in "string":
#     if val == "i":
#         break
#     print(val)
#     # output: s, t, r

# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# # output: s, t, r, n, g

# y = 3 
# while y > 0:
#     print(y)
#     y = y - 1
#     if y == 0:
#         break
# else:
#     print("Final else statement")
# # output: 3, 2, 1

# def add(a, b):
#     x = a + b
#     return x

# new_val = add(3,5)
# print(new_val)
# # output: 8

# def say_hi(name):
#     print("Hi, " + name)

# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')

# def say_hi(name):
#     return "Hi " + name
# greeting = say_hi("Michael")
# print(greeting)

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4, 6)
# sum2 = add(1, 4)
# sum3 = sum1 + sum2
# print(sum3)
# # output: 15


# def beCheerful(name='', repeat=2):
#     print(f"Good morning {name} " * repeat)
# beCheerful()
# beCheerful("Tim")
# beCheerful(name="John")
# beCheerful(repeat=6)


# arr = [1, 3, 5, 7]
# arr[0], arr[1] = arr[1], arr[0]
# print(arr)


# class User:
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()

# print(guido.name)
# print(monty.name)

# guido.name = "Guido"
# monty.name = "Monty"

# print(guido.name)


# class User:
#     def __init__(self, username, email_address):
#         self.name = username
#         self.email = email_address
#         self.account_balance = 0
#     def make_deposit(self, amount):
#         self.account_balance += amount

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)
# print(monty.name)
# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)
# print(monty.account_balance)

# import urllib.request
# response = urllib.request.urlopen("http://www.codingdojo.com")
# html = response.read()
# print(html)

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")

dad = Parent()
son = Child()
dad.method_a()
son.method_a()