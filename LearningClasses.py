import math
import random

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hired(self, title, salary):
        return Job(self, title, salary)

human1 = Human("John", 25)
human2 = Human("Jane", 23)

#print(human1.name)
#print(human1.age)

def birthday(self):
    self.age += 1
    print(f"{self.name} is now {self.age} years old! Happy Birthday!")

#birthday(human1)


class Job:
    def __init__(self, person : Human, title, salary):
        self.title = title
        self.salary = salary
        self.person = person

    def get_title(self):
        return self.title
    
    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.person.name

human1 = human1.hired("Teacher", 50000)
human2 = human2.hired("Banker", 65000)

print(f"{human2.get_name()} is a {human2.get_title()} and makes {human2.get_salary()} a year!")
print(f"{human1.get_name()} is a {human1.get_title()} and makes {human1.get_salary()} a year!")

def getRaise(self):
    if random.randint(0, 1) == 0:
        self.salary *=1.05
        print(f"{self.get_name()} got a raise and now makes {self.get_salary()} a year!")
    else:
        self.salary *=1.00
        print(f"{self.get_name()} did not get a raise and still makes {self.get_salary()} a year!")
    
    return self
getRaise(human1)
    

def fired(self):
    if 