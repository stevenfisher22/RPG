# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        self.name = 'Generic'

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print(f'{self.name} does {self.power} damage to {enemy.name}')
        if enemy.health <= 0:
            print(f'{enemy.name} is dead.')
        if self.health <= 0:
            print(f'{self.name} is dead.')

    def print_status(self):
        print(f'{self.name} has {self.health} health and {self.power} power.')

class Hero(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Hero'

class Goblin(Character):
    def __init__ (self, health, power):
        super().__init__(health, power)
        self.name = 'Goblin'

def main():
    hero1 = Hero(10, 5)
    goblin1 = Goblin(6, 2)

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