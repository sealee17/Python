class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f'{self.name}이고, {self.age}살 입니다.')

person1=Person('제이', 320)
person1.introduce()
