# Overriding Example

class Animal2():
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f'{self.name}(이)가 소리를 냅니다')
    
class Dog(Animal2):
# --> overriding
    def sound(self):
        print('Wuff Wuff')



dog1=Dog('Puppy')
dog1.sound()