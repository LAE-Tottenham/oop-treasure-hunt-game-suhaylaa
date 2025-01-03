import random
from time import sleep
from player import Player

class Boss:
    def __init__(self, name, health, attack_power, special_attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_attack_power = special_attack_power
        self.special_attack_ready = True  # Track if special attack is ready
        self.blockk = False

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {target.name}!")

        target.take_damage(damage)

    def special_attack(self, target):
        if self.special_attack_ready:
            damage = random.randint(self.special_attack_power // 2, self.special_attack_power)
            print(f"{self.name} uses Special Attack on {target.name}!")
            target.take_damage(damage)
            self.special_attack_ready = False 
        else:
            print(f"{self.name}'s Special Attack is not ready!")

    def block(self):
        print(f"{self.name} is preparing to block the next attack!")
        self.blockk = True # Boss blocks, reducing damage from the next attack

    def take_damage(self, damage):
        if self.blockk == True:
            # If the boss blocked, reduce damage by half
            damage = damage // 2
            print(f"Blocked the attack! Damage reduced to {damage}.")
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
            self.blockk = False
        else:
            self.health -= damage
            print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def reset_special_attack(self):
        self.special_attack_ready = True

# Function to start the boss fight
def boss_fight(player, boss):
    print(f"\nThe boss {boss.name} has appeared!\n")
    
    turn_count = 0  # To track turns for special attack cooldown
    while player.is_alive() and boss.is_alive():
        turn_count += 1

        # Player's turn
        print("\n--- Player's Turn ---")
        action = input("Choose action: (1) Attack (2) Special Attack (3) Block: ")

        if action == "1":
            player.attack(boss)
        elif action == "2":
            player.special_attack(boss)
        elif action == "3":
            player.block()
        else:
            print("Invalid choice, you attack!")
            player.attack(boss)
        
        # Check if the boss is defeated
        if not boss.is_alive():
            print(f"{boss.name} has been defeated! You win!")
            print('''
.------..------..------..------.     .------..------..------..------.
|G.--. ||A.--. ||M.--. ||E.--. |.-.  |O.--. ||V.--. ||E.--. ||R.--. |
| :/\: || (\/) || (\/) || (\/) ((5)) | :/\: || :(): || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: |'-.-.| :\/: || ()() || :\/: || ()() |
| '--'G|| '--'A|| '--'M|| '--'E| ((1)) '--'O|| '--'V|| '--'E|| '--'R|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'
                  ''')
            break
        
        # Boss's turn
        print("\n--- Boss's Turn ---")
        action = random.choice([1, 2, 3])  # Randomly decide the boss's action
        if action == 1:
            boss.attack(player)
        elif action == 2:
            boss.special_attack(player)
        elif action == 3:
            boss.block()

        # Check if the player is defeated
        if not player.is_alive():
            print(f"{player.name} has been defeated! You lose!")
            print('''
.------..------..------..------.     .------..------..------..------.
|G.--. ||A.--. ||M.--. ||E.--. |.-.  |O.--. ||V.--. ||E.--. ||R.--. |
| :/\: || (\/) || (\/) || (\/) ((5)) | :/\: || :(): || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: |'-.-.| :\/: || ()() || :\/: || ()() |
| '--'G|| '--'A|| '--'M|| '--'E| ((1)) '--'O|| '--'V|| '--'E|| '--'R|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'
                  

                  ''')
            sleep(2)
            print('Your body was buried in a ditch not too far away. No one ever found you.')
            break
        
        # Reset special attack if needed (after each turn)
        if turn_count % 3 == 0:
            player.reset_special_attack()
            boss.reset_special_attack()


