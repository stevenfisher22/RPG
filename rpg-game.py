# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        self.alive = health > 0
    def attack(self, enemy):
        self.health() -= enemy.power()
    def print_status(self):
        print(self.health)


class Hero(Character):
    def __init__ (self, health, power):
        Super() __init__ (health, power)
        self.name = 'hero'
    while goblin.alive() and hero.alive():
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        input = input()
        if input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print(f"You do {hero.power} damage to the goblin.")
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif input == "2":
            pass
        elif input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {input}".format)

        if goblin_health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print(f"The goblin does {goblin.power} damage to you.")
            if hero.health <= 0:
                print("You are dead.")

class Goblin(Character):
    def __init__ (self, health, power):
        Super() __init__ (health, power)
        self.name = 'goblin'

hero = Hero(10, 5)
goblin = Goblin(6, 2)