class Animal():
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f'{self.name}(이)가 소리를 냅니다')
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1=Dog('Puppy')
dog1.sound()