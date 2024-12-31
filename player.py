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
        # add more atributes as needed

    def calculate_inventory_size(self):
        for i in self.inventory:
            self.inventory_size = self.inventory_size + i.weight

    def add_item(self, item):
        if (self.inventory_size + item.weight) <= self.inventory_max_weight:
            self.inventory.append(item)
            print(f'You have now claimed the {item.name} item as yours!')
        else:
            print("Your inventory is brimming; there is no space for more...")


    def check_inventory(self):
        for i  in range (0,len(self.inventory)):
            print(' Your inventory contains a number of importan items, such as:')
            print(f'{i+1}. {self.inventory[i].name}')
            print(f'''Your inventory currently contains {self.inventory_size} of weight.
                      Be careful to not extend it past it maximum of {self.inventory_max_weight}''')
            
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
        return True  # Player blocks, reducing damage from the next attack

    def take_damage(self, damage, block):
        if block == True:
            # If the player blocked, reduce damage by half
            damage = damage // 2
            print(f"Blocked the attack! Damage reduced to {damage}.")
        else:
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def reset_special_attack(self):
        self.special_attack_ready = True


        # add more code here

    # add more methods as needed
