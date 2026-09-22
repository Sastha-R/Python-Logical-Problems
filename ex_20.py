class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        print("parent assigned") 

class Emp(Person):
    def __init__(self,salary,name,age):
        self.salary = salary
        super().__init__(name,age)
        print(self.name,self.age,self.salary)

obj = Emp(10000,"wick",30)


