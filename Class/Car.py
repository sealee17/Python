# Define Class <Car>

class Car:
    def __init__(self,제조사,브랜드,연비,이름):
        self.제조사=제조사
        self.브랜드=브랜드
        self.연비=연비
        self.이름=이름

    def introduce(self):
        print(f'이 자동차는 {self.제조사}에서 제조된 {self.브랜드}의 {self.이름}이고, 연비는 {self.연비}mpg입니다.')

    def dist(self,fuel):
        print(f'{self.이름}은 {fuel}의 연료로 {fuel*self.연비} miles를 이동할 수 있습니다.')

    def needd(self,dist):
        print(f'{dist} miles를 이동하기 위해서 {(dist/self.연비)*1580}원의 금액이 필요합니다.')        

p911=Car('Porche AG','Porche',20,'Porsche 911')
p911.introduce()
p911.dist(17)
p911.needd(20)