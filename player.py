import random
from person import *

class Player():
    def __init__(self, name, attack_power, special_attack_power):
        self.name = name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
        self.inventory_size = 0
        self.attack_power = attack_power
        self.special_attack_power = special_attack_power
        self.special_attack_ready = True
        self.blocc = False
        self.places_been = []
        self.inventory_full = False
        self.fight = False
        self.aliveb= True
        # add more atributes as needed

    def talk(self,place):
        if place.name == "Kitchen":
            talk = input(f'''
                1) {self.name}: Why should I? I don't trust you!!
                         
                2) {self.name}: If that's what you think is best.
                  ''')
            while True:
                if talk == "1":
                    print(f'''
    {self.name}: Why should I? I don't trust you!!
    ''')
                    self.fight = True
                    return self.fight
                    
                elif talk == "2":
                    print(f'''
    {self.name}: If that's what you think is best.
    ''')
                    break
                else:
                    print("Invalid input. Try again")
                    continue

        if place.name == "Living Room":
            print(f'''
{self.name}: Oh. Okay. 

            *That was very strange. I had better listen to her.*
                  ''')
            
        if place.name == "Garden":
            print(f'''
                *Why are people speaking in riddles. This place is so strange*
                  ''')

        if place.name == "Entrance":
            print(f'''
{self.name}: *whispers* I hate this place. It's so creepy
                  ''')   
        
    def add_places_been(self,place):
        self.places_been.append(place.name)

    def calculate_inventory_size(self):
        for i in self.inventory:
            self.inventory_size = self.inventory_size + i.weight

        return self.inventory_size

    def add_item(self, item):
        if (self.inventory_size + item.weight) <= self.inventory_max_weight:
            self.inventory.append(item)
            print(f'You have now claimed the {item.name} item as yours!')
            size = self.calculate_inventory_size()
            print(f'Your inventory currently contains {size} of weight.')
        else:
            print("Your inventory is brimming; there is no space for more...")
            self.inventory_full = True

    def show_inventory(self):
        print("The artifacts within your inventory are: ")
        for i in range(0,len(self.inventory)):
            print(f'{i+1}.{self.inventory[i].name}')


    def check_inventory(self):
        print(' Your inventory contains a number of important items, such as:')
        for i  in range (0,len(self.inventory)):
            print(f'{i+1}. {self.inventory[i].name}')
        print(f'''
              Your inventory currently contains {self.inventory_size} of weight.
              Be careful to not extend it past it maximum of {self.inventory_max_weight}
''')
            
    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(damage)

    def special_attack(self, target):
        if self.special_attack_ready:
            damage = random.randint(self.special_attack_power // 2, self.special_attack_power)
            print(f"{self.name} uses Special Attack on {target.name}!")
            target.take_damage(damage)
            self.special_attack_ready = False  # After using special attack, it's on cooldown
        else:
            print(f"{self.name}'s Special Attack is not ready!")

    def block(self):
        print(f"{self.name} is preparing to block the next attack!")
        self.blocc = True  # Player blocks, reducing damage from the next attack

    def take_damage(self, damage):
        if self.blocc == True:
            # If the player blocked, reduce damage by half
            damage = damage // 2
            print(f"Blocked the attack! Damage reduced to {damage}.")
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
            self.blocc = False
        else:
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def reset_special_attack(self):
        self.special_attack_ready = True


        # add more code here

    # add more methods as needed
