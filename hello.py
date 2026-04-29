# item = input("what are you buying")
# price = int(input("what is the price?"))
# quantity = int(input("what is the quantity??"))
# total = price*quantity
# print(f"your total for {quantity} {item} is ${total:.2f}")

# score = int(input("Enter the score: "))
# if (score>=90):
#   print("Grade A:")
# elif (score>=80):
#   print("Grade B:")
# else:
#   print("Grade: C or below")


# print(type(score))

# functions in python
# def greet_user(name):
#     return f"{name}, Welcome to code in Python!!"

# res = greet_user("Deepak")
# print(res)

# fruits = ['apple', 'banana', 'cherry']
# fruits.append('guava')
# print(fruits[0])
# print(fruits)
# fruits.insert(4, 'papaya')
# print(fruits)
# fruits.insert(-1, 'watermelon')
# print(fruits)
# fruits.pop()
# print(fruits)
# print(len(fruits))


# for fruit in fruits:
#   print(f"{fruit}")


# for i in range(0, len(fruits)):
#     print(f"{fruits[i]}")


# prices = {
#     "apple":0.5,
#     "banana":0.3
# }

# fruit = input("Enter the fruits you want to print: ")
# print(prices[fruit])
# user = {
#     'name': "alex",
#     'age': 25
# }
# user['age'] = 26
# print(user)
# user.update({"city": "New york", "status": "active"})
# print(user.keys())
# print(user.values())
# print(user.items())

# user.clear()

# try:
#     num = int(input("Enter a number to divide by 100: "))
#     result = 100/num
#     print(f"Result: {result}")
# except ValueError:
#     print("Error: you cannot divide by 20")
# except ZeroDivisionError:
#     print("Error: you cannot divide by zero!")
# except Exception as e:
#     print(f"An unexpected  error occured: ", e)
# finally:
#     print("Calculation attempt following")

# import os
# with open("notes.txt", "w") as file:
#     file.write("Learning with python file")
#     file.write("file handling is easy")

# print(prices(fruit))


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woff"


my_dog = Dog("Buddy", "golden retreiver")
print(my_dog.bark())


class Animal:
    def speak(self):
        print("Animal makes a sound")

    def walk(self):
        print("wow!!")


my_cat = Animal()
my_cat.speak()


class Cat(Animal):
    def speak(self):
        print("Meow!!")


my_cat = Cat()
my_cat.speak()
my_cat.walk()

# with open("example.txt", "w+") as file:
#     file.write("Learning with notes")
#     content = file.read()
#     print(content)


# if os.path.exists('example.txt'):
#     print("file is there")
# else:
#     print("file is missing")

# with open("requirements.txt","r") as file:
#     content = file.read()
#     print(content)
    
    



class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title

    def __str__(self):
        return f"{self.title} by {self.author}"


book = Book("Let's talk money", "Monika Halan")
print(book)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"Name: {self.name} and Salary: {self.salary}"
    def get_age(self,age):
        self.age = age
        return f"age:{self.age}"

class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language
    def get_details(self):
        return f"Name :{self.name} know language: {self.language} and get salary of {self.salary}"
    

dev = Developer("Deepak","62K","c++,js")
print(dev.get_details())
print(dev.get_age(25))

print(Developer.mro())