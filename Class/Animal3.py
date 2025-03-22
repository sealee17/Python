class Animal3():
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f'{self.name}(이)가 소리를 냅니다')

class Dog(Animal3):
    def sound(self):
        super.sound()
        print('Wuff Wuff')

class Cat(Animal3):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def purr(self):
        print(f'{self.color}인 {self.name} 그르렁거립니다')

cat1=Cat('솜이','이솜','하얀색')
cat1.purr()



'''
AttributeError: 'Animal3' object has no attribute 'purr'
'''

# animal1=Animal3('호랭이')
# animal1.purr()

# package에 없는 method를 가져와 쓰려고 할 때도 오류 발생 (e.g., import random)
# import random
# random.hi()

dog1=Dog('Puppy','바둑이')
dog1.sound