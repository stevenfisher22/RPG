# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
        self.alive = health > 0
    def attack(self, enemy):
        goblin.health() -= hero.power()
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

class Goblin:
    def _init__ (self, health, power):
        self.health = health
        self.power = power
        self.alive = health > 0
    def attack(self, enemy):
        hero.health() -= goblin.power()

hero = Hero(10, 5)
goblin = Goblin(6, 2)



# # ORIGINAL CODE:      
# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()