# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

from random import randint

# Basic Character class

class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        self.coins = 20
        self.name = 'Generic'

    # Is character alive? Checks that health is above 0
    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    # Basic attack function
    def attack(self, enemy):
        # Hero character can inflict double damage 20% of the time
        if self.name == 'Hero':
            heroProb = randint(1, 10)
            if heroProb <= 2:
                enemy.health -= (self.power * 2)
                print(f'{self.name} did double damage!')
        
        # Shadow character only damaged 10% of the time
        if enemy.name == 'Shadow' and randint(1, 10) > 1:
            print(f'Due to a fantastical anomaly, {enemy.name} was not damaged.')
        else:
            enemy.health -= self.power

        # Medic character can regain 2 health points 20% of the time after being attacked
        if enemy.name == 'Medic':
            enemyProb = randint(1, 10)
            if enemyProb >= 2:
                enemy.health += 2
            print(f'{enemy.name} recuperated 2 health points.')
        
        enemy.health -= self.power
        print(f'{self.name} does {self.power} damage to {enemy.name}')
        if enemy.health <= 0:
            print(f'{enemy.name} is dead.')
            self.coins += enemy.bounty
        if self.health <= 0:
            print(f'{self.name} is dead. Too bad you weren\'t good at this')
    
    def print_status(self):
        print(f'{self.name} has {self.health} health and {self.power} power.')

#Different characters available
class Hero(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Hero'

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Goblin'
        self.bounty = 5

class Medic(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Medic'
        self.bounty = 6

class Shadow(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Shadow'
        self.bounty = 7

class Zombie(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Zombie'
    def alive(self):
        return True

class Wizard(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Wizard'
        self.bounty = 10

class Orc(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Orc'
        self.bounty = 8

# The players:
hero1 = Hero(10, 5)
goblin1 = Goblin(6, 2)
medic1 = Medic(7, 1)
shadow1 = Shadow(1, 4)
zombie1 = Zombie(2, 1)
wizard1 = Wizard(9, 7)
orc1 = Orc(5, 5)

def main():

    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print('What do you want to do?')
        print('1. Fight goblin')
        print('2. Do nothing')
        print('3. Flee')
        print('> ', end=' ')
        input1 = input()
        if input1 == '1':
            hero1.attack(goblin1)
        elif input1 == '2':
            pass
        elif input1 == '3':
            print('Adios!')
            break
        else: 
            print(f'Invalid imput {input}')

        if goblin1.health > 0:
            goblin1.attack(hero1)

main()