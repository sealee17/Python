'''

나만의 게임을 만들기 위해 내 캐릭터를 만들 때 사용할 수 있는 player 클래스를 작성해봅시다.
(어떤 게임이 될 지, 클래스를 만들 때 어떤 값을 입력하여 만들 지는 여러분의 자유입니다!)
그리고 만들어진 객체가 사용할 만한 메서드를 __init__을 제외하고 최소 하나는 정의해봅시다.

'''
import random

class Player():
    def __init__(self):
        self.name = input('Your name:').capitalize()
        self.attack = random.randrange(10, 16) 
        self.health = random.randrange(50, 101)

    def attackM(self,monster):
        print(f'\n{monster.mName} appeared! Attack the {monster.mName}!\n')
        print(f'The monster is a {monster.mName}, be careful.\n')
        dam=self.attack
        monster.mHealth-=dam
        print(f'\n[{self.name} attacked {monster.mName}! DAMAGE: {dam}\n')
        if monster.mHealth<=0:
            print(f'{monster.mName} died! Congrats!')
        else:
            print(f'{monster.mName} health: {monster.mHealth} HP\n{self.name} health: {self.health} HP')

class Monster:
    def __init__(self, mName='Zombie'):
        self.mAttack=random.randrange(1, 5) 
        self.mHealth=random.randrange(10, 40) 
        self.mName=mName

    def attackP(self,player):
        mDam=self.mAttack
        player.mHealth-=mDam
        print(f'\n[{self.mName} attacked {player.name}! DAMAGE: {mDam}\n')
        if player.health<=0:
            print(f'Oh no, {player.name} died! \n[GAME OVER]')
        else:
            print(f'{player.name} health: {player.health} HP\n{self.mName} health: {self.mHealth} HP\n')