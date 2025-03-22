class Vehicle():
    
    def __init__(self,brand,name,speed):
        self.brand=brand
        self.name=name
        self.speed=speed

    def drive(self):
        print(f'{self.name}이(가) 시속 {self.speed}km/h 로 달립니다.')

class Electric:
    
    def __init__(self,batterycap):
        self.batterycap=batterycap
    
    def charge(self):
        print(f'배터리를 {self.batterycap}만큼 충전했습니다.')

class ElecCar(Electric,Vehicle):
   
    def __init__(self,batterycap,brand,name,speed): # 상속 받는 방법 / 서로 다른 class의 요소들을 조합해서 쓰는 방법
        Vehicle.__init__(self,brand,name,speed)
        Electric.__init__(self,batterycap)
    
    def drive(self):
        print(f'{self.name}이(가) {self.batterycap} 남았습니다.')
        print(f'매우 조용하게 {self.speed}로 움직입니다.')

bangbang=ElecCar('Tesla','CyberTruck', 300, 100)
bangbang.drive()