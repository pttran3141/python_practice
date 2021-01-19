###############################################
# BASIC OF STATIC METHOD IN PYTHON OOP

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def sub5(x):
        return x - 5

print(Math.add5(5))
print(Math.sub5(5))


###############################################
# BASIC OF CLASS ATTRIBUTE IN PYTHON OOP

# class Person:
#     # Class attribute
#     number_of_people = 0

#     # Class method(function)
#     def __init__(self, name):
#         self.name = name
#         #Person.number_of_people += 1
#         Person.add_person()

#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
    
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("Tim")
# p2 = Person("Jill")

# print(Person.number_of_people_())

######################################
# BASIC OF OBJECT INHERITANCE IN PYTHON
# print("\n\n############################## \nBASIC OF INHERITANCE CLASS IN PYTHON \n")

# class Pet: # generalization class
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")

#     def speak(self):
#         print("I don't know what to say")

# class Dog(Pet): # Specific class
#     def speak(self):
#         print("Woof")

# class Cat(Pet): # Specific class
#     def __init__(self, name, age, color):
#         super().__init__(name,age)
#         self.color = color

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

#     def speak(self):
#         print("Meow")

# class Fish(Pet):
#     pass

# p = Pet("Tim", 19)
# c = Cat("Bill", 24, "Brown")
# d = Dog("Jill", 20)
# f = Fish("Bubbles", 10)

# p.show()
# p.speak()
# c.show()
# c.speak()
# d.show()
# d.speak()
# f.show()
# f.speak()

###################################
# BASIC OF MULTIPLE CLASS IN PYTHON

# print("\n\n############################## \nBASIC OF MULTIPLE CLASS IN PYTHON \n")

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # initiallize an attribute grade 0 - 100

#     def get_grade(self):
#         return self.grade

# class Course: 
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value  = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)

# s1 = Student("Phuc", 25, 95)
# s2 = Student("Phuc2", 26, 75)
# s3 = Student("Phuc3", 24, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)

# print(course.get_average_grade())
# print(course.add_student(s3))





########################
# BASIC OF OOP in PYTHON
# print("\n\n############################## \nBASIC OF OOP IN PYTHON \n")

# class Dog: 
#     def __init__(self, name, age): #define an method(function)
#         self.name = name #define an attribute name
#         self.age = age

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age

#     def set_age(self,age):
#         self.age = age

#     def add_one(self, x):
#         return x + 1

#     def bark(self):
#         print("bark")

# d = Dog("Testing init in Dog object",34)
# print(d.name, d.age)
# d.set_age(23)
# print(d.name, d.age)
